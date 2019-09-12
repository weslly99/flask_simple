import os

class Config(object):
    project_dir = os.path.dirname(os.path.abspath(__file__))
    database_file = 'sqlite:///{}'.format(os.path.join(project_dir,'books.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = database_file
    SECRET_KEY = 'si3mple_aplication3'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING=True
    DEBUG=True
    project_dir = os.path.dirname(os.path.abspath(__file__))
    database_file = 'sqlite:///{}'.format(os.path.join(project_dir,'books_test.db'))
    SQLALCHEMY_DATABASE_URI = database_file
    SECRET_KEY = 'si3mple_aplication3'


app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
	'testing': TestingConfig
}