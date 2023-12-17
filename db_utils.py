# from winreg import ConnectRegistry


class RDSDatabaseConnector:
	def ___init___(self, credentials_dictionary):
		# initialises
		# from credentials_loader import credentials_loader
		# credentials_loader()

		loan_payments = False
		
	def SQLAlchemy_initialiser(self):
		# initialises a SQLAlchemy engine from the credentials provided to your class. 
		# This engine object together with the Pandas library will allow you to extract data from the database. 

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

		# from sqlalchemy import inspect
		# inspector = inspect(engine)
		# inspector.get_table_names()

		# from sqlachemy import text
		# with engine.connect() as connection:
		# 	result = connection.execute(text("SELECT * "))
		# 	for row in result:
		# 		print(row)

		# # # # # # # # # # # # # # # # # # # # # # # # 
        
		# meta = MetaData(engine)
		# my_table = Table(
		# 'my_table',
		# meta,
		# autoload=True,
		# schema=db_name
		# )

		# dbsession = sessionmaker(bind=engine)
		# session = dbsession()

		# # example query to table
		# results = session.query(my_table).filter(my_table.columns.id >=1)
		# results.all()

	def RDS_data_extractor(self, engine):
		# Develop a method which extracts data from the RDS database and returns it as a Pandas DataFrame. 
		# The data is stored in a table called loan_payments. 
		# example query to table
		import pandas as pd

		# self.SQLAlchemy_initialiser()

		# with self.SQLAlchemy_initialiser.engine.execution_options(isolation_level='AUTOCOMMIT').connect() as conn:
		self.loan_payments = pd.read_sql_table('loan_payments', engine)
		self.loan_payments.head(10)
		print(self.loan_payments_df)
		# pd.df(session.query(my_table).filter(my_table.columns.id >=1))
		return self.loan_payments

	
	def saver(self, loan_payments):
		# saves the data to an appropriate file format to your local machine. 
		# This should speed up loading up the data when you're performing your EDA/analysis tasks. 
		# The function should save the data in .csv format, since we're dealing with tabular data.

		# self.RDS_data_extractor()

		import pandas as pd

		loan_payments.to_csv("loan_payments.csv", sep=',', index=False, encoding='utf-8')

if __name__ == "__main__":
	import pandas as pd
	database_connection_instance = RDSDatabaseConnector()
	engine = database_connection_instance.SQLAlchemy_initialiser()
	loan_payments = database_connection_instance.RDS_data_extractor(engine)
	loan_payments
	database_connection_instance.saver(loan_payments)