class Configuration:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:password@localhost:5432/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
