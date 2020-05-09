# -*- coding: utf-8 -*-
"""
封装执行shell语句方法
"""

import subprocess

# from Conf import Config


class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        e = errors.decode("gbk")
        return o, e


if __name__ == '__main__':
    # conf = Config.Config()
    xml_report_path = "C:/Users/admin/Desktop/AP I_Automation-master/Report/xml"
    html_report_path = "C:/Users/admin/Desktop/API_Automation-master/Report/html"
    # s = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    s = "dfsdf"
    shell = Shell()

    print(shell.invoke(s))
