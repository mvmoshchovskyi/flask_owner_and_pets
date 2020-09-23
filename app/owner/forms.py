from wtforms import Form, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, length, NumberRange


class RegisterOwner(Form):
    name = StringField('Name', [DataRequired(), length(2, 20, 'name must be 2-20 characters')])
    age = IntegerField('Age', [DataRequired(), NumberRange(18, 100, 'age must be 2-20 characters')])
    city = StringField('City', [DataRequired(), length(2, 20, 'city must be 2-20 characters')])
    save = SubmitField('Save')


class RegisterPet(Form):
    name = StringField('Name', [DataRequired(), length(2, 20, 'name must be 2-20 characters')])
    age = IntegerField('Age', [DataRequired(), NumberRange(1, 50, 'age must be 2-20 characters')])
    animal_type = StringField('Animal Type',[DataRequired(), length(2, 20, 'name must be 2-20 characters')])
    save = SubmitField('Save')
