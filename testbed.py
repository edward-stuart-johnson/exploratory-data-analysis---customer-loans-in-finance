import psycopg2

import yaml
with open("/home/edward/exploratory-data-analysis---customer-loans-in-finance954/credentials.yaml", "r") as f:
    credentials_dictionary = yaml.safe_load(f)
print(credentials_dictionary)

print("Credentials dictionary is: ",credentials_dictionary)

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine_configuration = "postgresql://{RDS_USER}:{RDS_PASSWORD}@{RDS_HOST}:{RDS_PORT}/{RDS_DATABASE}".format(**credentials_dictionary)
print("Engine configuration is: ",engine_configuration)

engine = create_engine(engine_configuration)

engine.execution_options(isolation_level='AUTOCOMMIT').connect()

import pandas as pd

# self.SQLAlchemy_initialiser()

with engine.execution_options(isolation_level='AUTOCOMMIT').connect() as conn:
    loan_payments = pd.read_sql_table('loan_payments', engine)
    # loan_payments.head(10)
    print(loan_payments)
