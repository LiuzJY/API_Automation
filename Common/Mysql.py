import pymysql
import pandas as pd


class Mysql:
    def __init__(self):
        self.content = pymysql.connect(
            host='10.**.**.**',
            port=3306,
            user='*****',
            passwd='****',
            db='*****',
            charset="utf8")
        self.cursor = self.content.cursor()

    def query(self, query_sql):

        df = pd.read_sql(query_sql, self.content)
        print(df)
        return df

    def update(self, update_sql):

        self.cursor.execute(update_sql)
        self.content.commit()

    def insert(self, insert_sql):

        self.cursor.execute(insert_sql)
        self.content.commit()

    def delete(self, delete_sql):

        self.cursor.execute(delete_sql)
        self.content.commit()

    def end(self):
        self.cursor.close()
        self.content.close()
