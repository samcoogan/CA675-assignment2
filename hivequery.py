from pyhive import hive
import pandas as pd

class Hivequery:

    # connect to hive on the hdfs cluster
    host = "127.0.0.1"
    port = 10000
    username = "cluster-ba28"
    password = "2453984341495751881"
    sam_hive = hive.Connection(host, port, username, password)

    # retrieve query from hive tweets table, return string
    def hive_tq(self,query):
        data = pd.read_sql(query,self.sam_hive)
        twstring = str(data.iloc[0]['covid_tweets.user_name']) +"\n\n"+ str(data.iloc[0]['covid_tweets.post_text']) +"\n\n"+ str(data.iloc[0]['covid_tweets.user_location']) +" | " + str(data.iloc[0]['covid_tweets.post_date'])
        return twstring

    # retrieve query from hive news table, return string
    def hive_nq(self,query):
        data = pd.read_sql(query,self.sam_hive)
        nwstring = str(data.iloc[0]['covid_news.title']) +"\n" + str(data.iloc[0]['covid_news.post_date']) + "\n" + str(data.iloc[0]['covid_news.url']) #+"\n<a href="+ str(data.iloc[0]['covid_news.url']) +">" +str(data.iloc[0]['covid_news.url'])+"</a>"    
        return nwstring
