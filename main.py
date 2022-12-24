import requests
import json
from threading import Timer

cookies = {
    'odl_session': 'I4uK3ULS6WYILHjK3tN7U0NzGMG3oLMJi6iLyIHl',
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '973593%7Co3c6NMSCelPD4Jsis3DCEflQ280P7cdwS6WV9v04VyaR0JNxvg22ugs2Pr36%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24YnBNY1hGMTRwU3VpWG05Qw%24gt1914SeJeVouqS3x6fceNqhZjVkzQppt1Ke7AQbKu8',
    'XSRF-TOKEN': 'eyJpdiI6Ii9kSTdNSC9mZnBaRDZBeGJuQys2V2c9PSIsInZhbHVlIjoidUpVN2NSTFNCMFNVUXlxSnVNL3I4Y1F4ZHh1Vjl0dWNOWkN5Nll1MkUwdTloVGJ4aGhwUmcydHZVZkcvYWlLUlJJYkZ2MjdOWVY2bVNIeXlYQnR2RGdCZVJ3K29BckVnVVhjcGpWSlNSa1R3cWZwUmtOdHNvb1V5cGFTQXN0N2oiLCJtYWMiOiI2ODQ0ZGQ4NGRlNjQxMTFiNWE2NWFmYzdhODk1YjgwMWIzYzE1MjQ0YzdjN2ZjM2Q5OGNlYTU5N2E1YzAwMWYzIiwidGFnIjoiIn0%3D',
}

headers = {
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'odl_session=I4uK3ULS6WYILHjK3tN7U0NzGMG3oLMJi6iLyIHl; remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=973593%7Co3c6NMSCelPD4Jsis3DCEflQ280P7cdwS6WV9v04VyaR0JNxvg22ugs2Pr36%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24YnBNY1hGMTRwU3VpWG05Qw%24gt1914SeJeVouqS3x6fceNqhZjVkzQppt1Ke7AQbKu8; XSRF-TOKEN=eyJpdiI6Ii9kSTdNSC9mZnBaRDZBeGJuQys2V2c9PSIsInZhbHVlIjoidUpVN2NSTFNCMFNVUXlxSnVNL3I4Y1F4ZHh1Vjl0dWNOWkN5Nll1MkUwdTloVGJ4aGhwUmcydHZVZkcvYWlLUlJJYkZ2MjdOWVY2bVNIeXlYQnR2RGdCZVJ3K29BckVnVVhjcGpWSlNSa1R3cWZwUmtOdHNvb1V5cGFTQXN0N2oiLCJtYWMiOiI2ODQ0ZGQ4NGRlNjQxMTFiNWE2NWFmYzdhODk1YjgwMWIzYzE1MjQ0YzdjN2ZjM2Q5OGNlYTU5N2E1YzAwMWYzIiwidGFnIjoiIn0%3D',
    'Referer': 'https://applydl.dotm.gov.np/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'X-Inertia': 'true',
    'X-Inertia-Version': '29261dd93cf97c2e4a714179fe7a4a9b',
    'X-NewRelic-ID': 'VwMAWVNbCBAFVFVTDgEDX1U=',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'eyJpdiI6Ii9kSTdNSC9mZnBaRDZBeGJuQys2V2c9PSIsInZhbHVlIjoidUpVN2NSTFNCMFNVUXlxSnVNL3I4Y1F4ZHh1Vjl0dWNOWkN5Nll1MkUwdTloVGJ4aGhwUmcydHZVZkcvYWlLUlJJYkZ2MjdOWVY2bVNIeXlYQnR2RGdCZVJ3K29BckVnVVhjcGpWSlNSa1R3cWZwUmtOdHNvb1V5cGFTQXN0N2oiLCJtYWMiOiI2ODQ0ZGQ4NGRlNjQxMTFiNWE2NWFmYzdhODk1YjgwMWIzYzE1MjQ0YzdjN2ZjM2Q5OGNlYTU5N2E1YzAwMWYzIiwidGFnIjoiIn0=',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM1Nzg1ODAiLCJhcCI6IjUwNDE5MDUwOCIsImlkIjoiYzMzMTAzMGQyOWExMzYzYyIsInRyIjoiMWU2YWU3NDZmMmEwNTMwNDZmZmY5YjQ3NDg2N2EwYTAiLCJ0aSI6MTY3MTg0NDE5MzA0OX19',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'traceparent': '00-1e6ae746f2a053046fff9b474867a0a0-c331030d29a1363c-01',
    'tracestate': '3578580@nr=0-1-3578580-504190508-c331030d29a1363c----1671844193049',
}

def run():
    categories = [1, 2, 3, 8, 9]

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
            if parsed['ad'] == '2023-01-08':
                print(parsed['ad'] + '   BOOKED  ' + str(parsed['booked']))
                print(parsed['ad'] + '  RESERVED  ' + str(parsed['reserved']))
                print(parsed['ad'] + '  AVAILABLE  ' + str(parsed['available']))
        print('  ')


def startt():
    Timer(60, startt).start()
    run()


startt()
