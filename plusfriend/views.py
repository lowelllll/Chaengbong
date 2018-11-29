from .decorators import bot
from .omygirl_schedule_crawler import ScheduleCrawler 

@bot
def on_init(request): # 채팅방 진입 시
    return {
        'type':'buttons',
        'buttons':[
            '오마이걸 스케줄',
        ]        
    }


@bot
def on_message(request):
    user_key = request.JSON['user_key']
    type = request.JSON['type']
    content = request.JSON['content']
    
    if content == '오마이걸 스케줄':
        sc = ScheduleCrawler()
        res = sc.process()

        return {
            'message':{
                'text':res,
            },
            'keyboard':{
                'type':'buttons',
                'buttons':[
                    '비투비 스케줄'
                ]
            }
        }
    else:
        return {
            'message':{
                'text':'안녕하세여 저는 예진이를 위한 챗봇 챙봉이에요'
            }        
        }


@bot
def on_added(request):
    pass


@bot
def on_block(request, user_key):
    if request.mehod == 'DELETE':
        pass


@bot
def on_leave(request, user_key):
    if request.method == 'DELETE':
        pass

