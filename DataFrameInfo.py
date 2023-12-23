# After converting your columns to a more appropriate format you may want to develop a class to extract information from the DataFrame and its columns. Create a DataFrameInfo class which will contain methods that generate useful information about your DataFrame.


class DataFrameInfo:
# Some useful utility methods you might want to create that are often used for EDA tasks are:
    def ___init___(self):
        pass
    
    def describe_datatypes(self,df):
        #     Describe all columns in the DataFrame to check their data types
        return df.dtypes
    
    def statistics(self,df):
        #     Extract statistical values: median, standard deviation and mean from the columns and the DataFrame
        # statistical_values = df.Describe()
        mean = []
        median = []
        for column_name in df.iteritems():
            mean[column_name] = df[column_name].mean()
            median[column_name] = df[column_name].median()
        return mean, median


    def count_distinct_values_in_categories(self, df):
        #     Count distinct values in categorical columns
        for column_name in df.iteritems():
            if df[column_name].dtype =='category':
                print('The',column_name,'column only has', len(set(df[column_name])),'distinct values:')
                print(set(df[column_name]))
                print(column_name,'has datatype:',df[column_name].dtype,'\n')

    def shape_of_df(self,df):
        #     Print out the shape of the DataFrame
        shape = df.shape
        print('The shape of this dataframe is',shape)
        return shape
    
    def calculate_percentages_of_null_values(self,df):
    #     Generate a count/percentage count of NULL values in each column
        for column_name in df:
            # if df[column_name].dtype != 'category':
            null_count = df[column_name].isna().sum()
            column_length = len(df[column_name])
            null_percentage = 100*null_count/column_length 
            rounded_null_percentage = round(null_percentage,2)
            print(column_name, 'has',null_count, 'null values out of', column_length,'values, which is',rounded_null_percentage,'percent of the column.')

    def count_amounts_of_null_values(self,df):
        null_counts = df.isnull().sum()
        null_counts[null_counts > 0].sort_values(ascending=False)
        return null_counts
        
    def find_extreme_amounts_of_null_values(self,df):
        #     Generate a count/percentage count of NULL values in each column
        for column_name in df:
            # if df[column_name].dtype != 'category':
            null_count = df[column_name].isna().sum()
            if null_count > 0:
                column_length = len(df[column_name])
                null_percentage = 100*null_count/column_length 
                rounded_null_percentage = round(null_percentage,2)
                if null_percentage > 50:
                    print(column_name, 'has',null_count, 'null values out of', column_length,'values, which is',rounded_null_percentage,'percent of the column.')
                    print('This column should be removed, because most of it is null values.')
        print('The rest of the columns have less than 50% null values.')


        




