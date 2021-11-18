#Code sourced from the following data cleaning guide
#https://towardsdatascience.com/data-cleaning-in-python-the-ultimate-guide-2020-c63b88bf0a0d

import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None



# read the data
df = pd.read_csv(r'C:\Users\kiera\Downloads\US COVID-19 Tweets.csv', engine='python')

"""
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))
"""
# clean the data
dfclean = df.drop('has_media', axis=1)
dfclean = dfclean.drop('medias', axis=1)


# we know that column 'id' is unique, but what if we drop it?
df_dedupped = dfclean.drop('tweet_id', axis=1).drop_duplicates()

# there were duplicate rows
#print(dfclean.shape)
#print(df_dedupped.shape)
#print(dfclean['is_retweet'].value_counts())

df_relevant = df_dedupped.drop('is_reply', axis=1)
df_relevant = df_relevant.drop('nbr_reply', axis=1)
df_relevant = df_relevant.drop('is_retweet', axis=1)
df_relevant = df_relevant.drop('mentions', axis=1)

'''
# select numeric columns
df_numeric = df_relevant.select_dtypes(include=[np.number])
numeric_cols = df_numeric.columns.values
print(numeric_cols)

# select non numeric columns
df_non_numeric = df_relevant.select_dtypes(exclude=[np.number])
non_numeric_cols = df_non_numeric.columns.values
print(non_numeric_cols)
'''

df_relevant.to_csv('USTweetsClean.csv')
