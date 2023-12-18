

class RDSDatabaseConnector:
	def ___init___(self, credentials_dictionary):
		'''Imports pandas library and initialises table required.
		'''
		import pandas as pd

		loan_payments = False
		
	def _SQLAlchemy_initialiser_(self):
		'''Initialises a SQLAlchemy engine from the credentials provided.
		   This engine object together with the Pandas library will extract data from the database. 
		'''
		from credentials_loader import credentials_loader
		credentials_dictionary = credentials_loader()
		print("Credentials dictionary is: ",credentials_dictionary)

		import psycopg2
		import sqlalchemy
		from sqlalchemy import create_engine
		from sqlalchemy.orm import sessionmaker

		engine_configuration = "postgresql://{RDS_USER}:{RDS_PASSWORD}@{RDS_HOST}:{RDS_PORT}/{RDS_DATABASE}".format(**credentials_dictionary)
		print("Engine configuration is: ",engine_configuration)
		
		engine = create_engine(engine_configuration)
		engine.execution_options(isolation_level='AUTOCOMMIT').connect()

		return engine

	def _RDS_data_extractor_(self, engine):
		'''Extracts data from the RDS database and returns it as a Pandas DataFrame. 
		   The data is stored in a table called loan_payments. 
		'''
		import pandas as pd

		self.loan_payments = pd.read_sql_table('loan_payments', engine)
		self.loan_payments.head(10)
		print(self.loan_payments)
		return self.loan_payments

	
	def _saver_(self, loan_payments):
		'''Saves the tabular data in an appropriate .csv  format to local machine. 
		   This should speed up loading up the data when performing  EDA/analysis tasks. 
		'''
		loan_payments.to_csv("loan_payments.csv", sep=',', index=False, encoding='utf-8')

if __name__ == "__main__":
	database_connection_instance = RDSDatabaseConnector()
	engine = database_connection_instance._SQLAlchemy_initialiser_()
	loan_payments = database_connection_instance._RDS_data_extractor_(engine)
	loan_payments
	database_connection_instance._saver_(loan_payments)