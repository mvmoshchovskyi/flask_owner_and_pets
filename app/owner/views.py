from flask import Blueprint, render_template, request, redirect, url_for
from .models import OwnerModel, PetModel
from .forms import RegisterPet, RegisterOwner

owner = Blueprint('owner', __name__, 'static', template_folder='templates', url_prefix='/owner')

@owner.route('/')
def show_all():
    owners = OwnerModel.query.all()
    return render_template('owner/show_all.html', owners=owners)


@owner.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterOwner(request.form)
    if request.method == 'POST ' and form.validate():
        data = dict(request.form)
        del data['save']
        owner = OwnerModel(**data)
        owner.save_to_db()
        return redirect(url_for('owner.show_all'))
    return render_template('owner/register.html', form=form)


@owner.route('/<int:index>/pets')
def show_pets(index):
    pets =PetModel.find_pets_by_user_id(index)
    if not pets:
        return redirect(url_for('owner.register_pet', index=index))
    return render_template('owner/show_pets.html', pets=pets, index=index)

@owner.route('/<int:index>/pets/register/',methods=['GET','POST'])
def register_pet(index):
    form = RegisterPet(request.form)
    if request =='POST ' and form.validate():
        data = dict(request.form)
        del data['save']
        owner=OwnerModel.query.get(index,)
        owner.pets.append(PetModel(**data))
        owner.save_to_db
        return redirect(url_for('owner.show_pets', index=index))
    return render_template('owner/register_pet.html', form= form)

