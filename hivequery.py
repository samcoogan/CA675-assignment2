from pyhive import hive
import pandas as pd

class Hivequery:

    host= "127.0.0.1"
    port = 10000
    username="cluster-ba28"
    password="b200be4b-b98e-44a8-a348-5bb9763efa6f"
    sam_hive = hive.Connection(host, port, username, password)


    def hive_q(self,query):
        data = pd.read_sql(query,self.sam_hive)
        return data
