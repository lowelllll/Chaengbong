from .decorators import bot
from .module.omygirl_schedule_crawler import ScheduleCrawler
from .module.lunch_choice import MenuChoice

action_method = {
        '오마이걸 스케줄':ScheduleCrawler.process,
        '뭐 먹을까?':MenuChoice.choice,
    }

@bot
def on_init(request): # 채팅방 진입 시
    return {
        'type':'buttons',
        'buttons':list(action_method.keys())
    }


@bot
def on_message(request):
    content = request.JSON['content']
    return action(content)


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


def action(content):
    res = action_method[content]()

    return {
        'message': {
            'text': res,
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': list(action_method.keys())
        }
    }
