import os

class Config:
    email configurations
    MAIL_SERVER = 'iank299@gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ian:sawasawa@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options ={"production":ProdConfig,
"development":DevConfig,"testing":TestConfig

}

