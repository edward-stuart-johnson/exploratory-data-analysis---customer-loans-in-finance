def credentials_loader():
	'''A function which loads the credentials.yaml file and returns the data dictionary contained within. 
	   This will be be passed to  RDSDatabaseConnector as an argument which the class will use to connect to the remote database.
	'''
	import yaml
	from pathlib import Path

	filepath = Path(__file__).with_name("credentials.yaml")
	print(filepath)
	with filepath.open("r") as f:
		credentials_dictionary = yaml.safe_load(f)
	print(credentials_dictionary)
	return credentials_dictionary

if __name__ == "__main__":
	credentials_loader()