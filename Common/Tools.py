from Common import Request
import datetime


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
    url = "http://**.***.**.**:18089/*******/flush/config"

    params = {"address": "**.***.**.**:3099",
              "referer": "http://**.***.**.**:8080/*************/manage/index"}

    headers = {"Host": "**.***.**.**:18089",
               "Origin": "http://**.***.**.**:18089",
               "Referer": "http://**.***.**.**:18089/*****/flushList?type=config"}

    request = Request.Request("activity")
    rsp = request.post_request(url=url, data=params, header=headers)
    print(rsp)