import pandas as pd

def create_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
