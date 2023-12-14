

# A function which loads the credentials.yaml file and returns the data dictionary contained within. 

# This will be be passed to your RDSDatabaseConnector as an argument which the class will use to connect to the remote database.
def credentials_loader():
	import yaml
	with open("credentials.yaml", "r") as f:
		credentials_dictionary = yaml.safe_load(f)
	print(credentials_dictionary)
	return credentials_dictionary


