import pandas as pd
import csv

def read_dataframe(csv_path):

    dataframe = pd.read_csv(csv_path, sep=',')

    return dataframe

def extract_columns():
    
    df = read_dataframe(csv_path)

    best_player = df['Name'].head(11)

    nationality = df['Nationality'].head(11)

    rate = df['Rating'].head(11)

    return best_player, nationality, rate

def rate_players():

    best_player, _, _ = extract_columns()
    _, nationality, _ = extract_columns()
    _, _, rate = extract_columns()

    frames = [best_player, nationality, rate]

    result = pd.concat(frames, axis=1)

    print(result)

    return result

if __name__ == "__main__":
    csv_path = 'fifa/FullData.csv'
    read_dataframe(csv_path)
    rate_players()