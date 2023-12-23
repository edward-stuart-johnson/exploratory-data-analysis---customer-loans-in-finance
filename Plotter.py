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
        plt.figure(figsize=(10,6))
        sns.heatmap(df.isna().transpose(),
                    cmap='YlGnBu',
                    cbar_kws={'label':'Missing Data'})
        plt.savefig('visualing_null_values.png',
                    dpi=100)
