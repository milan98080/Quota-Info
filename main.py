import requests
import json
from pushbullet import Pushbullet
from threading import Timer

<<<<<<< HEAD
API_KEY = "o.53fergJdWezg7vDwJNVIQOh1oxzEAMp4"
=======
API_KEY = ""
>>>>>>> 9381a87d44094fdada823c2b1abde3192fad9f8e
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
            if parsed['ad'] == '2022-08-29' and parsed['available'] != 100:
                print(cate + '  AVAILABLE  ' + str(parsed['available']))
                push = pb.push_note(cate, '  AVAILABLE  ' + str(parsed['available']))


def startt():
    Timer(30, startt).start()
    run()


startt()
