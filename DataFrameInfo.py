# After converting your columns to a more appropriate format you may want to develop a class to extract information from the DataFrame and its columns. Create a DataFrameInfo class which will contain methods that generate useful information about your DataFrame.


class DataFrameInfo:
# Some useful utility methods you might want to create that are often used for EDA tasks are:

    def describe_datatypes(self,df):
        #     Describe all columns in the DataFrame to check their data types
        return df.dtypes
    
    def statistics(self,df):
        #     Extract statistical values: median, standard deviation and mean from the columns and the DataFrame
        statistical_values = df.Describe()
        return statistical_values


    def count_distinct_values_in_categories(self, df):
        #     Count distinct values in categorical columns
        if df[column_Name].dtype =='category':
            print('The',column_name,'column only has', len(set(df[column_name])),'distinct values:')
            print(set(df[column_name]))
            print(column_name,'has datatype:',df[column_name].dtype,'\n')

    def shape_of_df(self,df):
        #     Print out the shape of the DataFrame
        shape = df.shape
        print('The shape of this dataframe is',shape)
        return shape

        
    def count_null_values(self,df):
        #     Generate a count/percentage count of NULL values in each column
        for column_name in df:
            NaN_count = df[column_name].isna().sum()
            NaN_percentage = NaN_count/df[column_name].sum()
            print(column_name, 'has ',NaN_count, 'NaN values, which is',NaN_percentage,'percent of the column.')




