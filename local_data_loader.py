
def local_data_loader():
    # a function which loads the data from local machine into a Pandas DataFrame.
    import pandas as pd
    from pathlib import Path
    filepath = Path(__file__).with_name("loan_payments.csv")
    print(filepath)
    with filepath.open("r") as f:
        df = pd.read_csv(f) 
    return df

import pandas as pd
df = local_data_loader()
print(df)