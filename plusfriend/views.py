from .decorators import bot

@bot
def on_init(request): # 채팅방 진입 시
    return {
        'type':'buttons',
        'buttons':[
            '시작하기',
        ]
    }

@bot
def on_message(request):
    user_key = request.JSON['user_key']
    type = request.JSON['type']
    content = request.JSON['content']
    print(content)
    return

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

