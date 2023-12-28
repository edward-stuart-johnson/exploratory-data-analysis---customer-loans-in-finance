class Plotter:
    # a class to visualise insights from the data
    def __init__(self) -> None:
        pass

    def visualise_null_values(self, df):
        '''This method visualises the removal of null values.'''
        import pandas as pd
        import seaborn as sns
        import matplotlib.pyplot as plt
        # heatmap
        # plt.figure(figsize=(10,6)) # iS THSI OPTIONAL? CAN I MAKE IT AUTOFIT ALL COLUMNNAMES?
        sns.heatmap(df.isna().transpose(),
                    cmap='YlGnBu',
                    cbar_kws={'label':'Missing Data'})
        plt.savefig('visualing_null_values.png',
                    dpi=100)
        sns.displot(
            data=df.isna().melt(value_name='missing'),
                                y='variable',
                                hue='missing',
                                multiple='fill',
                                aspect=1.25
            )
        plt.savefig('visualising_missing_data.png',
                        dpi=100)

    def skewness(self, df):
        import pandas as pd
        import seaborn as sns

        numeric_features = list()
        for column_name in df:
            # Set numeric (ie. continuous or ordinal category) features:
            if df[column_name].dtype in ('int64', 'float64'):
                numeric_features.append(column_name)

        # categorical_features = [col for col in df.columns if col not in numeric_features]
        sns.set(font_scale=0.7)
        f = pd.melt(df, value_vars=numeric_features)
        g = sns.FacetGrid(f, col="variable",  col_wrap=3, sharex=False, sharey=False)
        g = g.map(sns.histplot, "value", kde=True)

    def qq_plot(self,df,column_name):
        import matplotlib.pyplot as plt
        from statsmodels.graphics.gofplots import qqplot
        qq_plot = qqplot(df[column_name] , scale=1 ,line='q', fit=True)
        plt.show()
        df[column_name].describe()

    def box_plot(self,df,column_name):
        pass
            # import plotly.graph_objects as go

            # for column_name in df.iteritems():
            #         fig = go.Figure()
            #         fig.add_trace(go.Box(
            #             y=[df.[column_name]],
            #             name='Only Mean',
            #             marker_color='darkblue',
            #             boxmean=True # represent mean
            #         ))
            #         fig.add_trace(go.Box(
            #             y=[df.[column_name]],
            #             name='Mean & SD',
            #             marker_color='royalblue',
            #             boxmean='sd' # represent mean and standard deviation
            #         ))

            #         fig.show()    

    def pair_plot(self,df):
        import seaborn as sns
        sns.pairplot(df[numeric_features])

    def correlation_matrix(self,df):
        import seaborn as sns
        import matplotlib.pyplot as plt

        corr = df.corr()
        # Draw the heatmap
        sns.heatmap(corr, mask=mask,
                    square=True, linewidths=.5, annot=True, cmap=cmap)
        plt.yticks(rotation=0)
        plt.title('Correlation Matrix of all Numerical Variables')
        plt.show()

        
