# -*- coding: utf-8 -*-

import allure
import pytest

from Params.params import MyTest
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert
from Common import Mysql, Tools


class TestBasic:

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('MyTest')
    def test_basic_01(self, action):
        """
            不在活动时间内
        """
        mysql = Mysql.Mysql()
        time = Tools.acttime()
        outtime = time[0]
        print(outtime)
        sql = "update t_migu_mac_config set `value` = '%s' where `key` = 'activity.MAC_SKH_KF_MGXZPMJZ.show.validperiod'" % outtime
        mysql.update(sql)  # 更改活动时间
        Tools.refresh()  # 刷新配置项

        print("hello")
        conf = Config()
        data = MyTest()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_test
        req_url = 'http://' + host
        print(req_url)
        urls = data.url
        params = data.data
        print(params)
        headers = data.header
        api_url = req_url + urls[0]

        response = request.get_request(api_url, params[0], headers[0])
        print(response)

        # assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'code', '600000')
        # assert test.assert_time(response['time_consuming'], 100)
        Consts.RESULT_LIST.append('True')
    #
    # @allure.feature('Home')
    # @allure.severity('blocker')
    # @allure.story('Basic')
    # def test_basic_02(self, action):
    #     """
    #         用例描述：登陆状态下查看基础设置
    #     """
    #     conf = Config()
    #     data = Basic()
    #     test = Assert.Assertions()
    #     request = Request.Request(action)
    #
    #     host = conf.host_debug
    #     req_url = 'http://' + host
    #     urls = data.url
    #     params = data.data
    #     headers = data.header
    #
    #     api_url = req_url + urls[1]
    #     response = request.post_request(api_url, params[1], headers[1])
    #
    #     assert test.assert_code(response['code'], 401)
    #     assert test.assert_text(response['text'], '{"error":"继续操作前请注册或者登录."}')
    #     Consts.RESULT_LIST.append('True')


if __name__ == '__main__':
    pytest.main(["test_basic"])
