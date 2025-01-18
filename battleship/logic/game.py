import asyncio
import json
from cache import AsyncTTL
from battleship.logic.cfparse import get_ranklist
from battleship.logic.calcstate import calc_state
import time

last_responses = {}
working = set()


def wait_if_same(f):
    async def wrapper(*args):
        if args in working:
            while args in working:
                await asyncio.sleep(0.5)
            return last_responses.get(args)
        else:
            working.add(args)
            res = await f(*args)
            working.remove(args)
            return res

    return wrapper


def save_if_not_none(f):
    async def wrapper(*args):
        res = await f(*args)
        if res is not None:
            last_responses[args] = res
        return last_responses.get(args)

    return wrapper


@AsyncTTL(maxsize=1, time_to_live=10)
async def get_config():
    with open('battleship/logic/config.json') as f:
        return json.load(f), time.time()


@wait_if_same
@AsyncTTL(maxsize=16, time_to_live=10)
@save_if_not_none
async def request_state(game_id):
    config, _ = await get_config()
    config = config.get(str(game_id))
    contest_id = config.get('contest_id')
    problem = config.get('problem')
    name_order = config.get('name_order')
    field = config.get('field')
    try:
        ranklist = await get_ranklist(contest_id)
    except:
        return None

    shots_table = [None, None]
    for team in (0, 1):
        shots_table[team] = [None] * len(name_order[team])
        for i, name in enumerate(name_order[team]):
            shots_table[team][i] = ranklist.get(name, [0] * len(problem))
    game = [None, None]
    stats = [None, None]
    for team in (0, 1):
        shots, injury, kills, game[team] = calc_state(shots_table[1 - team], field[team].strip().split('\n'))
        stats[team] = {'shots': shots, 'injury': injury, 'kills': kills}

    return problem, name_order, stats, game, time.time()


async def get_state(game_id):
    config, tm = await get_config()
    if str(game_id) not in config:
        return None
    return await request_state(game_id)
