import datetime
import requests
from bs4 import BeautifulSoup


class ScheduleCrawler():
    ROOT_URL = "http://ohmy-girl.com/omg_official/schedule.php"

    @staticmethod
    def _crawling():
        """
        해당 날짜의 오마이걸의 월간 스케줄을 알려줍니다.
        :return:
        """
        response = requests.get(ScheduleCrawler.ROOT_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        schedule = soup.find_all('img')

        results = {}
        for sc in schedule:
            prev = sc.find_previous_sibling('span')
            if prev:
                if prev.text in results:
                    results[prev.text].append(sc['data-legend'])
                else:
                    results[prev.text] = [sc['data-legend']]

        return results

    @staticmethod
    def _parsing(schedule):
        dt = datetime.datetime.now()
        day = dt.day
        month = dt.month

        result = ''
        result += "{}월의 오마이걸 스케줄 \n".format(month)
        for day in schedule.keys():
            result += "{}월 {}일 \n".format(month, day)
            for sc in schedule[day]:
                result += "    - {}\n".format(sc.replace('<br />', ''))

        return result

    @staticmethod
    def process():
        schedule = ScheduleCrawler._crawling()
        return ScheduleCrawler._parsing(schedule)
