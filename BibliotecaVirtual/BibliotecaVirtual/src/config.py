class Config:
    SECRET_KEY = '$$ENCRIPTACION$$'


class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '28325882$Ruben'
    MYSQL_DB = 'biblioteca'

config = {
    'development':DevelopmentConfig
}