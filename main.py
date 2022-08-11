import requests
import json
from pushbullet import Pushbullet
from threading import Timer

API_KEY = ""
pb = Pushbullet(API_KEY)
cookies = {}

headers = {}


def run():
    categories = [1, 2, 3]

    for cat in categories:
        json_data = {
            'is_urgent': False,
            'office_id': 17,
            'category_id': cat,
        }
        if cat == 1:
            cate = 'SCOOTER'
        if cat == 2:
            cate = 'BIKE'
        if cat == 3:
            cate = 'CAR'
        response = requests.post('https://applydl.dotm.gov.np/license/quota', cookies=cookies, headers=headers,
                                 json=json_data)
        data = json.loads(response.text)
        new = data['quotas']
        for every in data['quotas']:
            parsed = new[every]
            if parsed['available'] > 0:
                push = pb.push_note(cate, parsed['ad'] + '    ' + str(parsed['available']))


def startt():
    Timer(5, startt).start()
    run()


startt()
