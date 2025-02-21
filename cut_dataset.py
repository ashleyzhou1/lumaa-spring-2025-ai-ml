import pandas as pd

#load CSV file and print first 45 rows to 'movies_45.csv'
def load_data(file_path):
    df = pd.read_csv(file_path, nrows=45)
    df.to_csv('movies_45.csv', index=False)

    return df[['title', 'overview']]
