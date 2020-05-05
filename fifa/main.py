import requests
import pandas as pd
import csv
from io import StringIO

df = pd.read_csv('FullData.csv', sep=',')

rating = df.sort_values(by=['Rating']).apply(lambda x: ','.join(set(str(x).split(','))))

nationality = df[['Nationality']] + df.sort_values(by=['Rating'])

nationality.to_csv('output.csv')
