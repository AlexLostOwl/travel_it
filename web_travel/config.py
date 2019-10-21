import os

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
database = os.environ['POSTGRES_DB']
port = os.environ['POSTGRES_PORT']

SQLALCHEMY_DATABASE_URI = f'postgres+psycopg2://{user}:{password}@{host}:{port}/{database}'

SQLALCHEMY_TRACK_MODIFICATIONS = False