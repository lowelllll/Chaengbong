import datetime
import requests
from xml.etree import ElementTree

class Weather():
    weather = []

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
    def _calc_time():
        now_hour = datetime.datetime.now().hour
        hour = now_hour if now_hour % 3 == 0 else now_hour+(3-(now_hour%3))
        return hour

    @staticmethod
    def _create_message(hour):
        idx = hour // 3 if hour != 3 else 0
        w_data = Weather.weather[idx]

        msg = """관악구 신림동 실시간 날씨 예보\n{hour}시 기준\n최고 기온은 {tmn} 이고, 최저 기온은 {tmx} 입니다.\n날씨는 {comment}입니다.""".\
            format(hour=hour, tmn=w_data['tmn'], tmx=w_data['tmx'], comment=w_data['comment'])

        return msg

    @staticmethod
    def process():
        Weather._xml_parse()
        hour = Weather._calc_time()
        return Weather._create_message(hour)
