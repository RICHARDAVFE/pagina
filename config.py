class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_DATABASE_HOST = 'us-cdbr-east-06.cleardb.net'
    MYSQL_DATABASE_USER = 'bd9cd3ea9bc91f'
    MYSQL_DATABASE_PASSWORD = '7a3f87d6'
    MYSQL_DATABASE_DB = 'heroku_83179bffa1e45ff'


config = {
    'development': DevelopmentConfig
}

