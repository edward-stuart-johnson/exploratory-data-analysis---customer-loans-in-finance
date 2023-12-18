class DataTransform:
    '''Because there are columns which should be converted into a different format, we create a DataTransform class to handle these conversions. 
       We have added methods to the DataTransform class which we can apply to the DataFrame columns to perform any required conversions.
    '''
    def ___init___(self):
        pass

    def date_convert(self, data):
        import pandas as pd

        data['issue_date'] = pd.to_datetime(data['issue_date'])
        data['last_payment_date'] = pd.to_datetime(data['last_payment_date'])
        data['next_payment_date'] = pd.to_datetime(data['next_payment_date'])
        data['last_credit_pull_date'] = pd.to_datetime(data['last_credit_pull_date'])

