class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_DATABASE_HOST = 'us-cdbr-east-06.cleardb.net'
    MYSQL_DATABASE_USER = 'b399f12758e8d9'
    MYSQL_DATABASE_PASSWORD = '647f571f'
    MYSQL_DATABASE_DB = 'heroku_69dc861d66128c1'


config = {
    'development': DevelopmentConfig
}

