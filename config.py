class Config:
    DEBUG = False


class DevConfig(Config):
    DEBUG = True



    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:wer45012@localhost/owners_and_pets'


