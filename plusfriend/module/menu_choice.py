import random

class MenuChoice():
    food = [
        '파스타', '스테이크', '분식', '떡볶이', '피자', '치킨',
        '중식', '닭갈비', '삼겹살', '양념갈비', '불고기', '부대찌개',
        '김치찌개', '햄버거', '샤브샤브', '뷔페', '초밥', '우동',
        '칼국수', '청국장', '보쌈', '족발', '한식당', '카레',
        '치즈등갈비', '순댓국', '설렁탕', '갈비탕', '찜닭',
    ]

    @staticmethod
    def choice():
        return random.choice(MenuChoice.food) + '!'

