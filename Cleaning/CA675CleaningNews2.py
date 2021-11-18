#Code taken from the following data cleaning guide
#https://towardsdatascience.com/data-cleaning-in-python-the-ultimate-guide-2020-c63b88bf0a0d



import pandas as pd
import os, glob
from datetime import datetime
import numpy as np


path = r'C:\Users\kiera\OneDrive\Documents\NewCovidNewsData'
all_files = glob.glob(os.path.join(path, "*.csv"))
df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
df_merged   = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv( "merged.csv")

df = pd.read_csv("merged.csv")

df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
df.url = df.url.str.replace(r"\/", r"\\")
df.url = df.url.str.replace(r"\\\\", r"\\")


columns = ["ID", "headline", "publisher"]
df1 = df.drop(columns, axis=1)

for col in df1.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))

df2 = df1.drop_duplicates()

print(df1.shape)
print(df2.shape)

print(df2.head())

df2.to_csv("CleanCOVIDVaccineNews.csv")
