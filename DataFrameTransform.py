class DataFrameTransform:
    # a class to perform EDA transformations on your data
    def __init__(self) -> None:
        pass
    
    def impute(self,df,column_name,average):
        # a method which can impute your DataFrame columns. Decide whether the column should be imputed with the median or the mean and impute the NULL values. 
        if average == 'median':
            df[column_name] = df[column_name].fillna(df[column_name].median())
            # df['no_of_bathrooms'] = df['no_of_bathrooms'].fillna(df['no_of_bathrooms'].median())
        elif average == 'mean':
            df[column_name] = df[column_name].fillna(df[column_name].mean())
        elif average == 'mode':
            if df[column_name].dtype != 'category':
                df[column_name] = df[column_name].fillna(df[column_name].mode())
            elif df[column_name].dtype == 'category':
                df[column_name] = df[column_name].fillna(df[column_name].value_counts().index[0])
            else:
                return ValueError
        else:
            return ValueError
        return df
    
    def log_transform(self,df,column_name):
        import numpy as np
        # from Plotter import Plotter
        # import seaborn as sns
        # print('Before log transformation:')
        # o=sns.histplot(df,label="Skewness: %.2f"%(df[column_name].skew()), kde=True )
        # o.legend
        log_transformed_data = df[column_name].map(lambda i: np.log(i) if i > 0 else 0)
        # print('After log transformation:')
        # t=sns.histplot(log_transformed_data,label="Skewness: %.2f"%(log_transformed_data[column_name].skew()), kde=True )
        # t.legend()
        # qq_plot = Plotter.qq_plot(log_transformed_data , scale=1 ,line='q', fit=True)
        # plt.show()  
        return log_transformed_data
    
    def log_transform_skewed_numeric_columns(self,df,skewnessthreshold = 3):
        numeric_features = self.create_numeric_features_list(df)
        df_to_be_transformed = df.copy()
        log_transformed_df = df.copy()
        for column_name in numeric_features:
        # .skew(axis=0,skipna=True,numeric_only=True):
            # print(df[column_name])    
            if df_to_be_transformed[column_name].skew(axis=0,skipna=True,numeric_only=True) > skewnessthreshold:
                original_skew = df_to_be_transformed[column_name].skew(axis=0,skipna=True,numeric_only=True)
                print(column_name,'has a skewness of',original_skew)
                print(column_name,'is very skewed')
            # if df[column_name][1].skew() > 3:
            # # df[column_name].skew(axis=0,skipna=True,numeric_only=True) > 3:
                # log_transformed_data = self.log_transform(df,column_name)
                import numpy as np
                log_transformed_df[column_name] = log_transformed_df[column_name].map(lambda i: np.log(i) if i > 0 else 0)
                transformed_skew = log_transformed_df[column_name].skew(axis=0,skipna=True,numeric_only=True)
                print(column_name,'has a new skewness after a log transformation of',transformed_skew)
                print('This is a change in skewness of', original_skew - transformed_skew)     
                print('\n') 
        return log_transformed_df
    
    def inverse_log_transform_column(self,df,column_name):
        import numpy as np
        df[column_name].map(lambda i: np.exp(i) if i > 0 else 0)

    def create_numeric_features_list(self, df):
        numeric_features = list()
        for column_name in df:
            # Set numeric (ie. continuous or ordinal category) features:
            if df[column_name].dtype in ('int64', 'float64'):
                numeric_features.append(column_name)    
        return numeric_features
    
    def box_cox_transform(self,df,column_name):
        # from scipy import stats
        from scipy.stats import boxcox
        import numpy as np
        transformed_df = df.copy()
        transformed_df[column_name] = boxcox(transformed_df[column_name],lmbda=None)
        return transformed_df
