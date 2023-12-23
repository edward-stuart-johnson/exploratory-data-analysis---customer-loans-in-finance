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
        log_transformed_data= df[column_name].map(lambda i: np.log(i) if i > 0 else 0)
        t=sns.histplot(log_transformed_data,label="Skewness: %.2f"%(log_transformed_data.skew()), kde=True )
        t.legend()
        qq_plot = qqplot(log_transformed_data , scale=1 ,line='q', fit=True)
        plt.show()  