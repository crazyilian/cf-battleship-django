import hashlib
import os
import random
import time
import httpx
import string

CF_API_KEY = os.environ.get('CF_API_KEY')
CF_API_SECRET = os.environ.get('CF_API_SECRET')


async def get_codeforces_group_standings(contest_id, api_key, api_secret):
    base_url = f'https://codeforces.com/api//contest.standings'

    current_time = int(time.time())
    rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    params = {
        'contestId': contest_id,
        'apiKey': api_key,
        'time': current_time,
        'showUnofficial': 'false'
    }

    param_str = '&'.join(f'{k}={v}' for k, v in sorted(params.items()))
    sig_str = f'{rand_str}/contest.standings?{param_str}#{api_secret}'
    api_sig = rand_str + hashlib.sha512(sig_str.encode('utf-8')).hexdigest()

    params['apiSig'] = api_sig
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(base_url, params=params)
        if response.status_code != 200:
            print('base_url:', base_url)
            print('params:', params)
            print('response:', response.text)
            raise Exception('failed to get standings')
    return response.json()


async def get_ranklist(contest_id):
    print('requesting ranklist', contest_id, time.time())
    standings = await get_codeforces_group_standings(contest_id, CF_API_KEY, CF_API_SECRET)
    ranklist = {}
    for row in standings["result"]['rows']:
        name = row['party']['members'][0]['name']
        tasks = []
        for i in row['problemResults']:
            tasks.append(int(i['points']))
        ranklist[name] = tasks
    return ranklist
