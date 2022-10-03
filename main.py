import requests
import json
from threading import Timer

cookies = {
    'odl_session': 'Hpbit3cNiFBcKP2J1Oxvec5vNtjXgchFtElGwKKx',
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '874073%7CJuM4fyU8fzff9PguAM4V9AAhdMRAz5qCr78sSkDdr2ivsIqYRiXdh69wOPi9%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24Lm9TUGhXdVd1QTFMdEtLbg%24KeH5EUKErS%2F2H1hdpJFP0A8w%2FSE02PPhjY03mVO8imM',
    'XSRF-TOKEN': 'eyJpdiI6InR6d2FBNWk1cUZzS3BTb253bmhDSHc9PSIsInZhbHVlIjoiK1c3NFRTSnN3WloyOHF0ZTd0UG5iTkdOSkJ4ZDh0UEc4TStWbTJyaXZacUZMY2swZGRmT1lMckhQQzZ5c0hyU1BSa25LSjZ0VitFSXo5ZUY1Q2RXMHViWUVoRzNWbzBsR0dRT0pmak1oVGhXUE01RDhHNXo0M2N4TmJPZjJMNkUiLCJtYWMiOiIyZjljYWEwY2I0MTczNTI2NWM0NjQ5MmIyZTY1ZjI4YzZmNjI2NDA5OWI4NmNmYzJjZDhkODM0ZDI4ZjBmYTk5IiwidGFnIjoiIn0%3D',
}

headers = {
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'odl_session=Hpbit3cNiFBcKP2J1Oxvec5vNtjXgchFtElGwKKx; remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=874073%7CJuM4fyU8fzff9PguAM4V9AAhdMRAz5qCr78sSkDdr2ivsIqYRiXdh69wOPi9%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24Lm9TUGhXdVd1QTFMdEtLbg%24KeH5EUKErS%2F2H1hdpJFP0A8w%2FSE02PPhjY03mVO8imM; XSRF-TOKEN=eyJpdiI6InR6d2FBNWk1cUZzS3BTb253bmhDSHc9PSIsInZhbHVlIjoiK1c3NFRTSnN3WloyOHF0ZTd0UG5iTkdOSkJ4ZDh0UEc4TStWbTJyaXZacUZMY2swZGRmT1lMckhQQzZ5c0hyU1BSa25LSjZ0VitFSXo5ZUY1Q2RXMHViWUVoRzNWbzBsR0dRT0pmak1oVGhXUE01RDhHNXo0M2N4TmJPZjJMNkUiLCJtYWMiOiIyZjljYWEwY2I0MTczNTI2NWM0NjQ5MmIyZTY1ZjI4YzZmNjI2NDA5OWI4NmNmYzJjZDhkODM0ZDI4ZjBmYTk5IiwidGFnIjoiIn0%3D',
    'Referer': 'https://applydl.dotm.gov.np/licence/category',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'X-Inertia': 'true',
    'X-Inertia-Version': 'abfe0d2fb15763f4d5db4390a711e362',
    'X-NewRelic-ID': 'VwMAWVNbCBAFVFVTDgEDX1U=',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'eyJpdiI6InR6d2FBNWk1cUZzS3BTb253bmhDSHc9PSIsInZhbHVlIjoiK1c3NFRTSnN3WloyOHF0ZTd0UG5iTkdOSkJ4ZDh0UEc4TStWbTJyaXZacUZMY2swZGRmT1lMckhQQzZ5c0hyU1BSa25LSjZ0VitFSXo5ZUY1Q2RXMHViWUVoRzNWbzBsR0dRT0pmak1oVGhXUE01RDhHNXo0M2N4TmJPZjJMNkUiLCJtYWMiOiIyZjljYWEwY2I0MTczNTI2NWM0NjQ5MmIyZTY1ZjI4YzZmNjI2NDA5OWI4NmNmYzJjZDhkODM0ZDI4ZjBmYTk5IiwidGFnIjoiIn0=',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM1Nzg1ODAiLCJhcCI6IjUwNDE5MDUwOCIsImlkIjoiNDI5MmExNWMwZDBlZWE2ZiIsInRyIjoiMDNjYzAyNTY3ODI1ZmRjYWNiMTRlOGQzNTNiYTkwNzciLCJ0aSI6MTY2NDc2MDAwMzY2OX19',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'traceparent': '00-03cc02567825fdcacb14e8d353ba9077-4292a15c0d0eea6f-01',
    'tracestate': '3578580@nr=0-1-3578580-504190508-4292a15c0d0eea6f----1664760003669',
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
