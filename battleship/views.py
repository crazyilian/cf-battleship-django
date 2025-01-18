from django.shortcuts import render
from battleship.logic.game import get_state
import json


async def index(request, game_id):
    try:
        problems, names, stats, game, tm = await get_state(game_id)
    except Exception as e:
        print(e)
        return render(request, 'battleship/no_game.html', {'GAME_ID': game_id}, status=200)
    game_state = json.dumps({'problems': problems, 'names': names, 'game': game, 'stats': stats}, ensure_ascii=False)
    context = {'GAME_STATE': game_state, 'TIME': tm, 'GAME_ID': game_id}
    return render(request, 'battleship/index.html', context)
