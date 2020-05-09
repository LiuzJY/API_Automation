import requests

url = "http://10.25.246.28:18089/MAC/activity3/model/v2.0/queryMyPrizeList"
params = {
              "activityId":"MAC_LHX_KF_DRHLC",
              "activiType":"1",
            }
response = requests.get(url=url, params=params)
print(response.text)

if __name__ == '__main__':
    print(response.text)