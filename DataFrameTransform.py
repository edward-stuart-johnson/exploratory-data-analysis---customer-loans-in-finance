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
    
    def box_cox_transform(self,df,skewnessthreshold = 3):
        from scipy.stats import boxcox
        import numpy as np
        
        numeric_features = self.create_numeric_features_list(df)
        # Box_Cox_transformed_df = to_be_Box_Cox_transformed_df.copy()
        Box_Cox_transformed_df = df.copy()

        for column_name in numeric_features:
            if Box_Cox_transformed_df[column_name].skew(axis=0,skipna=True,numeric_only=True) > skewnessthreshold:
                original_skew = Box_Cox_transformed_df[column_name].skew(axis=0,skipna=True,numeric_only=True)
                print(column_name,'has a skewness of',original_skew)
                Box_Cox_transformed_df[column_name] = boxcox(Box_Cox_transformed_df[column_name])[0]
                transformed_skew = Box_Cox_transformed_df[column_name].skew(axis=0,skipna=True,numeric_only=True)
                print(column_name,'has a new skewness after a Box-Cox transformation of',transformed_skew)
                print('This is a change in skewness of', original_skew - transformed_skew)  
                print('\n')
        return Box_Cox_transformed_df
    
    def Yeo_Johnson_transform(self,df,skewnessthreshold = 3):
        from scipy.stats import yeojohnson
        import numpy as np
        
        numeric_features = self.create_numeric_features_list(df)
        Yeo_Johnson_transformed_df = df.copy()

        for column_name in numeric_features:
            if Yeo_Johnson_transformed_df[column_name].skew(axis=0,skipna=True,numeric_only=True) > skewnessthreshold:
                original_skew = Yeo_Johnson_transformed_df[column_name].skew(axis=0,skipna=True,numeric_only=True)
                print(column_name,'has a skewness of',original_skew)
                Yeo_Johnson_transformed_df[column_name] = yeojohnson(Yeo_Johnson_transformed_df[column_name])[0]
                transformed_skew = Yeo_Johnson_transformed_df[column_name].skew(axis=0,skipna=True,numeric_only=True)
                print(column_name,'has a new skewness after a Yeo-Johnson transformation of',transformed_skew)
                print('This is a change in skewness of', original_skew - transformed_skew)  
                print('\n')
        return Yeo_Johnson_transformed_df    

    def remove_collinear_features(self, df, threshold):
        '''
        Objective:
            Remove collinear features in a dataframe with a correlation coefficient
            greater than the threshold. Removing collinear features can help a model 
            to generalize and improves the interpretability of the model.

        Inputs: 
            x: features dataframe
            threshold: features with correlations greater than this value are removed

        Output: 
            dataframe that contains only the non-highly-collinear features
        '''

        # Calculate the correlation matrix
        corr_matrix = df.corr()
        iters = range(len(corr_matrix.columns) - 1)
        drop_cols = []

        # Iterate through the correlation matrix and compare correlations
        for i in iters:
            for j in range(i+1):
                item = corr_matrix.iloc[j:(j+1), (i+1):(i+2)]
                col = item.columns
                row = item.index
                val = abs(item.values)

                # If correlation exceeds the threshold
                if val >= threshold:
                    # Print the correlated features and the correlation value
                    print(col.values[0], "|", row.values[0], "|", round(val[0][0], 2))
                    drop_cols.append(col.values[0])

        # Drop one of each pair of correlated columns
        drops = set(drop_cols)
        df = df.drop(columns=drops)

        return df