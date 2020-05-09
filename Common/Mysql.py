import pymysql
import pandas as pd
import datetime


class Mysql:
    def __init__(self):
        self.content = pymysql.connect(
            host='10.25.246.61',
            port=3306,
            user='music_pro',
            passwd='music_pro',
            db='activity_pro',
            charset="utf8")
        # self.content = pymysql.connect(
        #     host='10.25.193.180',
        #     port=1521,
        #     user='dev',
        #     passwd='dev',
        #     db='music',
        #     charset="utf8")
        self.cursor = self.content.cursor()

    def query(self, sql):
        # sql = "SELECT * FROM t_migu_mac_config"
        # self.cursor.execute(sql)
        # for row in self.cursor.fetchall():
        #     print("name:%s\t url:%s" % row)
        # print(f"一共查找到：{self.cursor.rowcount}")
        df = pd.read_sql(sql, self.content)
        return df
        print(df)

    def update(self, sql):
        # sql = 'UPDATE t_migu_mac_config ' \
        #       'SET `value` = \'true\' ' \
        #       'WHERE `key` = \'activity.MAC_TD_KF_SNLHHYNB.mongodb.h5ContainerInvoke.flag\''
        # df = pd.read_sql_query(sql1, self.content)
        # print(df)
        self.cursor.execute(sql)
        self.content.commit()

    def insert(self, sql):
        # sql = "INSERT INTO t_migu_activity_prize_history" \
        #       "(`prize_id`, `prize_name`, `user_key`, `activity_id`, `accept_time`) " \
        #       "VALUES ('MYSQLTEST', 'TEST', '15892914011', 'XCYXBJNB', '2018-07-11 14:23:35')"
        self.cursor.execute(sql)
        self.content.commit()

    def delete(self, sql):
        # sql = "DELETE FROM t_migu_activity_prize_history WHERE prize_id='MYSQLTEST'"
        self.cursor.execute(sql)
        self.content.commit()

    def end(self):
        self.cursor.close()
        self.content.close()


if __name__ == '__main__':
    # mysql = Mysql()
    # # mysql.query()
    # # mysql.end()
    # refresh()
    today = datetime.date.today()
    yesterday = today + datetime.timedelta(days=-1)
    lastmonth = today + datetime.timedelta(days=-30)
    activitytime = str(lastmonth) + " 00:00::00" + "|" + str(yesterday) + " 23:59:59"
    print(activitytime)


# import pandas as pd
# import pymysql
# # import sqlalchemy
# # from sqlalchemy import create_engine
# DB_USER='music_pro';
# DB_PASS='music_pro';
# DB_HOST='10.25.246.61';
# DB_PORT='3306';
# DATABASE='activity_pro';
# # 1. 用sqlalchemy构建数据库链接engine
# # connect_info = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)  #1
# # engine = create_engine(connect_info)
# # sql 命令
# sql_cmd = "SELECT * FROM t_migu_mac_config"
# # df = pd.read_sql(sql=sql_cmd, con=engine)
# #print(df)
# # 2. 用DBAPI构建数据库链接engine
# # con = pymysql.connect(host='10.25.246.61', port=3306, user='music_pro', passwd='music_pro', db='activity_pro', charset="utf8")
# con = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DATABASE, charset='utf8')
# df = pd.read_sql(sql_cmd, con)
# print(df)
# #
# # def conn_sql():
# #     DB_USER = 'dev';
# #     DB_PASS = 'dev';
# #     DB_HOST = '10.25.193.180';
# #     DB_PORT = '1521';
# #     DATABASE = 'music';
# #     # 1. 用sqlalchemy构建数据库链接engine
# #     # connect_info = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)  #1
# #     # engine = create_engine(connect_info)
# #     # sql 命令
# #     sql_cmd = "SELECT * FROM t_migu_activity_risk_st_1902 WHERE id=1245"
# #     # df = pd.read_sql(sql=sql_cmd, con=engine)
# #     # print(df)
# #     # 2. 用DBAPI构建数据库链接engine
# #     con = pymysql.connect(host='10.25.193.180', port=1521, user='dev', passwd='dev', db='music', charset="utf8")
# #     # con = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, detabase=DATABASE, charset='utf8')
# #     df = pd.read_sql(sql_cmd, con)
# #     return df
