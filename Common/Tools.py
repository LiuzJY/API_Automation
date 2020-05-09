from Common import Request
import datetime
from Common import Mysql


def acttime():
    """
    生成活动时间
    """
    today = datetime.date.today()
    yesterday = today + datetime.timedelta(days=-1)
    tomorrowday = today + datetime.timedelta(days=+1)
    lastmonth = today + datetime.timedelta(days=-30)
    outact = str(lastmonth) + " 00:00::00" + "|" + str(yesterday) + " 23:59:59"  # 不包含当前日期的活动时间
    inact = str(lastmonth) + " 00:00::00" + "|" + str(tomorrowday) + " 23:59:59"  # 包含当前日期的活动时间
    # print(outact)
    return outact, inact


def refresh():
    """
    刷新配置项
    """
    url = "http://10.25.246.28:18089/MACMS_SERVICE/flush/config"

    params = {"address": "10.25.246.28:3099",
              "referer": "http://10.25.246.34:8080/ms-admin/manage/index"}

    headers = {"Host": "10.25.246.28:18089",
               "Origin": "http://10.25.246.28:18089",
               "Referer": "http://10.25.246.28:18089/MACMS/flushList?type=config"}

    request = Request.Request("activity")
    rsp = request.post_request(url=url, data=params, header=headers)
    print(rsp)


if __name__ == '__main__':
    # refresh()
    # outtime()
    mysql = Mysql.Mysql()
    time = acttime()
    sql = "update t_migu_mac_config set `value` = '%s' where `key` = 'activity.MAC_SKH_KF_MGXZPMJZ.show.validperiod'" % time[1]
    mysql.update(sql)

    print(sql)
