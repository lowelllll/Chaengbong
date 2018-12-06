import datetime
import requests
from xml.etree import ElementTree
from bs4 import BeautifulSoup

class Weather():
    weathers = [] # 예보
    now_weather = {} # 현재 날씨

    @staticmethod
    def _xml_parse():
        response = requests.get('http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1162069500')
        root = ElementTree.fromstring(response.content)
        body = root[0][6].find('description')[1]

        for data in body[-8:]:
            dic = dict()
            dic['hour'] =  int(data[0].text)
            dic['comment'] = data[7].text
            dic['tmn'] = data[3].text+'도' if data[3].text != '-999.0' else '알 수 없음'
            dic['tmx'] = data[4].text+'도' if data[4].text != '-999.0' else '알 수 없음'
            Weather.weather.append(dic)

        Weather.weather.sort(key=lambda x:x['hour'])

    @staticmethod
    def _crawler():
        res = requests.get('http://www.weather.go.kr/weather/process/timeseries-dfs-body-ajax.jsp?myPointCode=1162069500&unit=M')
        soup = BeautifulSoup(res.text, 'html.parser')
        data = soup.select(
            'dl > dd.now_weather1_center'
        )
        print(data)

        Weather.now_weather['hour'] = datetime.datetime.now().hour
        Weather.now_weather['temp'] = data[0].text
        # now['humidity'] = data[2].text 습도

        datas = soup.find_all('dl','time_weather1_dl3')
        for data in datas:
            w = {}
            w['hour'] = data.find('dt','w_hour2').text
            w['comment'] = data.find('img').get('alt')
            w['temp'] = data.find('dd','temp2').text
            Weather.weathers.append(w)

    @staticmethod
    def _create_message():
        msg = '관악구 신림동 현재 {}시\n기온은 {} 입니다.\n'.format(Weather.now_weather['hour'], Weather.now_weather['temp'])
        msg += '날씨 예보!\n'
        for weather in Weather.weathers:
            msg += '{}입니다. \n예상 기온 {}, 날씨 {}입니다.\n'.format(weather['hour'], weather['temp'], weather['comment'])

        return msg

    @staticmethod
    def process():
        Weather._crawler()
        print(Weather._create_message())

Weather.process()