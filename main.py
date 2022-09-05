import requests
import json
from threading import Timer

cookies = {
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '700903%7Cux7XZ6fwluJnZP9ZavvL0LxxiViZJgYctJPaztKNaDqGd9KFUUPXZqz03zZ0%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24eVQ3cll0ZmkweE84MWNicA%24BeDPuvur0h50eRHSpvK4bH1xO%2BPGvUkZb5ahYBoUvKc',
    'odl_session': 'BHCIuQetAV90w2Pc1okgoBt99iKofcBGUSjax9Ik',
    'XSRF-TOKEN': 'eyJpdiI6IkVkMndzNlhkeVJTT2w0enVLV3JWRXc9PSIsInZhbHVlIjoiOW92clEwMzZ3b0RhOFA3T1dKUlhnQzZIZ2NCbnZOcUkzRHlVL0tlNUQrRC9XeEh2QVozZnVMc2JhTm5kUXd5R05KQXI2dCsxbmhIZEZQQ1VCZGxJdUpBeHNJNEEzWG9Cekw1c1NWTVhXZi9CYnJ0Q2xIY0xxN28wbEIwOEpBRmoiLCJtYWMiOiI4NDE2NGM0OWMxNDczMjY4YjgyNTFiODI4ODFiZjliOTViMWIyZjg2NmY3MjFkYTc0ZjkyOTQ3NTkyYThjMGZhIiwidGFnIjoiIn0%3D',
}

headers = {
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=700903%7Cux7XZ6fwluJnZP9ZavvL0LxxiViZJgYctJPaztKNaDqGd9KFUUPXZqz03zZ0%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24eVQ3cll0ZmkweE84MWNicA%24BeDPuvur0h50eRHSpvK4bH1xO%2BPGvUkZb5ahYBoUvKc; odl_session=BHCIuQetAV90w2Pc1okgoBt99iKofcBGUSjax9Ik; XSRF-TOKEN=eyJpdiI6IkVkMndzNlhkeVJTT2w0enVLV3JWRXc9PSIsInZhbHVlIjoiOW92clEwMzZ3b0RhOFA3T1dKUlhnQzZIZ2NCbnZOcUkzRHlVL0tlNUQrRC9XeEh2QVozZnVMc2JhTm5kUXd5R05KQXI2dCsxbmhIZEZQQ1VCZGxJdUpBeHNJNEEzWG9Cekw1c1NWTVhXZi9CYnJ0Q2xIY0xxN28wbEIwOEpBRmoiLCJtYWMiOiI4NDE2NGM0OWMxNDczMjY4YjgyNTFiODI4ODFiZjliOTViMWIyZjg2NmY3MjFkYTc0ZjkyOTQ3NTkyYThjMGZhIiwidGFnIjoiIn0%3D',
    'Referer': 'https://applydl.dotm.gov.np/category',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-Inertia': 'true',
    'X-Inertia-Version': '16361033bc8dabc69ba761dce03df65e',
    'X-NewRelic-ID': 'VwMAWVNbCBAFVFVTDgEDX1U=',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'eyJpdiI6IkVkMndzNlhkeVJTT2w0enVLV3JWRXc9PSIsInZhbHVlIjoiOW92clEwMzZ3b0RhOFA3T1dKUlhnQzZIZ2NCbnZOcUkzRHlVL0tlNUQrRC9XeEh2QVozZnVMc2JhTm5kUXd5R05KQXI2dCsxbmhIZEZQQ1VCZGxJdUpBeHNJNEEzWG9Cekw1c1NWTVhXZi9CYnJ0Q2xIY0xxN28wbEIwOEpBRmoiLCJtYWMiOiI4NDE2NGM0OWMxNDczMjY4YjgyNTFiODI4ODFiZjliOTViMWIyZjg2NmY3MjFkYTc0ZjkyOTQ3NTkyYThjMGZhIiwidGFnIjoiIn0=',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM1Nzg1ODAiLCJhcCI6IjUwNDE5MDUwOCIsImlkIjoiNDZlMjM3YmIxODI2NTk2MSIsInRyIjoiN2U1NDkxNjA0YWE0M2ZlNDgzMzFhNjhhNTYyYjY5M2QiLCJ0aSI6MTY2MjM0MTgzOTAwOH19',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Chromium";v="106"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'traceparent': '00-7e5491604aa43fe48331a68a562b693d-46e237bb18265961-01',
    'tracestate': '3578580@nr=0-1-3578580-504190508-46e237bb18265961----1662341839008',
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
            if parsed['ad'] == '2022-09-11':
                print(parsed['ad'] + '   BOOKED  ' + str(parsed['booked']))
                print(parsed['ad'] + '  RESERVED  ' + str(parsed['reserved']))
                print(parsed['ad'] + '  AVAILABLE  ' + str(parsed['available']))
        print('  ')


def startt():
    Timer(120, startt).start()
    run()


startt()
