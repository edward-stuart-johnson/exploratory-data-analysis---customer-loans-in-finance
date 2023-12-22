class DataTransform:
    '''Because there are columns which should be converted into a different format, we create a dfTransform class to handle these conversions. 
       We have added methods to the dfTransform class which we can apply to the dfFrame columns to perform any required conversions.
    '''
    def ___init___(self):
        pass

    def date_convert(self, df, column_name):
        import pandas as pd

        # for column_name in ('issue_date', 'last_payment_date', 'next_payment_date', 'last_credit_pull_date'):
            #  month_and_year_only_format = dict(
            #      year = df[column_name].str[3:],
            #      month = df[column_name].str[:3],
            #      day = 1
            #         )
            #  df[column_name] = pd.to_datetime(month_and_year_only_format)
        df[column_name] = pd.to_datetime(df[column_name], format='mixed')

            #  print(pd.to_datetime(rawdata['input'], format='mixed'))

            #  .split('-')
        return df

       

        # df['issue_date'] = pd.to_datetime(df['issue_date'])
        # df['last_payment_date'] = pd.to_datetime(df['last_payment_date'])
        # df['next_payment_date'] = pd.to_datetime(df['next_payment_date'])
        # df['last_credit_pull_date'] = pd.to_datetime(df['last_credit_pull_date'])
    
    def convert_to_int(self, df, column_name):
        df[column_name] = df[column_name].astype(int, errors='ignore')
        return df
    
    def convert_to_category(self, df, column_name):
        df[column_name] = df[column_name].astype('category', errors='ignore')
        return df
    
    def convert_to_boolean(self, df, column_name):
        df[column_name] = df[column_name].astype('boolean')# , errors='ignore')
        return df

    def convert_to_numerical(self, df):
        import pandas as pd

        df[''] = pd.to_numerical(df[''])

    

if __name__ == '__main__':
    import pandas as pd
    dt = DataTransform()
    rawdata = pd.DataFrame({'input':['Jul-2013']})
    print(pd.to_datetime(rawdata['input'], format='mixed'))


    # # print(dt.date_convert(input))
    # month_and_year_only_format = dict(
    #              year = input[3:],
    #              month = input[:3],
    #              day = 1
    #                 )
    # print(
    #     pd.to_datetime(month_and_year_only_format)
    # )