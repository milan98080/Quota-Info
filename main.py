import requests
import json
from threading import Timer

cookies = {
    'odl_session': 'p3Ld2HhjUc3VVtwrDK2goyw4fEHWbSYcIsWcGtHx',
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '678005%7Cgmd4fkv7Iy5bUtNu5oH4RVO9AcNfjKvOAjh5ZVH6DJhaReDJRPhYrWNWcJWi%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24eUlQT3lWOGtoS1hyajNpQg%24HYq0OdAqpS7J1ePbFobvUyGNsS69ZN56qfu%2BaYp9SSo',
    'XSRF-TOKEN': 'eyJpdiI6IktOWTRBMlZZdDZIWDRGTVhobE45TUE9PSIsInZhbHVlIjoid0NqWUdYcE50K2lLeHhlN1VIWTdDOVhjWDcyRENLdHdOT3RDYlZPYnJDVDVGcGxNZnVXUEVnRU5yU2JwVUord2o1OWRoWHVrSHRXVDJtd253bWhKLzZTajRmRFZzTFR6ZHY1Qll2L2VueXdaT1JlbDJjQlIwVWtraDluWEF1cjkiLCJtYWMiOiJjODk2NGQyZmViMTEyMjRjMDA0ZDRlN2MxMjMyMzRhYWY1YmNlNzA2ZjQ3MzI3NTQ5ZDAwNWQwODA2ZTdiNzUyIiwidGFnIjoiIn0%3D',
}

headers = {
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'odl_session=p3Ld2HhjUc3VVtwrDK2goyw4fEHWbSYcIsWcGtHx; remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=678005%7Cgmd4fkv7Iy5bUtNu5oH4RVO9AcNfjKvOAjh5ZVH6DJhaReDJRPhYrWNWcJWi%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24eUlQT3lWOGtoS1hyajNpQg%24HYq0OdAqpS7J1ePbFobvUyGNsS69ZN56qfu%2BaYp9SSo; XSRF-TOKEN=eyJpdiI6IktOWTRBMlZZdDZIWDRGTVhobE45TUE9PSIsInZhbHVlIjoid0NqWUdYcE50K2lLeHhlN1VIWTdDOVhjWDcyRENLdHdOT3RDYlZPYnJDVDVGcGxNZnVXUEVnRU5yU2JwVUord2o1OWRoWHVrSHRXVDJtd253bWhKLzZTajRmRFZzTFR6ZHY1Qll2L2VueXdaT1JlbDJjQlIwVWtraDluWEF1cjkiLCJtYWMiOiJjODk2NGQyZmViMTEyMjRjMDA0ZDRlN2MxMjMyMzRhYWY1YmNlNzA2ZjQ3MzI3NTQ5ZDAwNWQwODA2ZTdiNzUyIiwidGFnIjoiIn0%3D',
    'Referer': 'https://applydl.dotm.gov.np/licence/category',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'X-Inertia': 'true',
    'X-Inertia-Version': 'abfe0d2fb15763f4d5db4390a711e362',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'eyJpdiI6IktOWTRBMlZZdDZIWDRGTVhobE45TUE9PSIsInZhbHVlIjoid0NqWUdYcE50K2lLeHhlN1VIWTdDOVhjWDcyRENLdHdOT3RDYlZPYnJDVDVGcGxNZnVXUEVnRU5yU2JwVUord2o1OWRoWHVrSHRXVDJtd253bWhKLzZTajRmRFZzTFR6ZHY1Qll2L2VueXdaT1JlbDJjQlIwVWtraDluWEF1cjkiLCJtYWMiOiJjODk2NGQyZmViMTEyMjRjMDA0ZDRlN2MxMjMyMzRhYWY1YmNlNzA2ZjQ3MzI3NTQ5ZDAwNWQwODA2ZTdiNzUyIiwidGFnIjoiIn0=',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

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
        if cat == 8:
            cate = 'MINI'
        if cat == 9:
            cate = 'HEAVY'
        response = requests.post('https://applydl.dotm.gov.np/license/quota', cookies=cookies, headers=headers,
                                 json=json_data)
        data = json.loads(response.text)
        new = data['quotas']
        print(cate)
        for every in data['quotas']:
            parsed = new[every]
            if parsed['ad'] == '2022-10-12':
                print(parsed['ad'] + '   BOOKED  ' + str(parsed['booked']))
                print(parsed['ad'] + '  RESERVED  ' + str(parsed['reserved']))
                print(parsed['ad'] + '  AVAILABLE  ' + str(parsed['available']))
        print('  ')


def startt():
    Timer(120, startt).start()
    run()


startt()
