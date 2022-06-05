# class Configuration:
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


class Configuration:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:password@pg:5432/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
