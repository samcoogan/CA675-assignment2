import ijson
import json
import pandas as pd
import csv
import pandas as pd
import io
import os
import sys

from glob import glob

chunks = pd.read_json(r'C:\Users\kiera\Downloads\aylien_covid_news_data.jsonl', lines=True, chunksize = 1000)
for i, c in enumerate(chunks):
    c.to_json('Covid_chunk_{}.jsonl'.format(i), orient="records", lines=True)


def csv(path):
    i=0
    for filename in glob.glob(os.path.join(path, '*.jsonl')):
        df = pd.read_json(filename, lines=True)
        df.to_csv('Covid_chunk_{}.csv'.format(i), index=False, encoding='utf-8')
        i+=1

#csv(path)

def get_df():
    df=pd.DataFrame()
    path = r'C:\Users\kiera\AppData\Local\Programs\Python\Python310\Covid_news'
    for file in glob(os.path.join(path, '*.csv')):
        a=pd.read_csv(file, error_bad_lines=False)
        aux = a.drop(['body', 'categories', 'entities', 'media', 'characters_count', 'paragraphs_count', 'sentences_count', 'social_shares_count', 'summary'], axis = 1)
        df=df.append(aux)
    df.to_csv(r'C:\Users\kiera\Downloads\merged_COVID_News.csv', index=False)


#df=get_df()


