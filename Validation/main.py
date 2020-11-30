import csv
import pandas as pd

data = pd.read_csv("country-codes.csv")

for col in data.columns:
    print(col)