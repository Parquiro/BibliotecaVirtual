class Config:
    SECRET_KEY = '$$ENCRIPTACION$$'


class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'biblioteca'

config = {
    'development':DevelopmentConfig
}