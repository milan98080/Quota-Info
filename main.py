import requests
import json
from threading import Timer

cookies = {
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '968507%7Cl8wSiDJ8zv8v4x9RHzbWRW66wxoN9mmw0NofCjwmRLR6iGRhJiLdxMsRADmn%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24bVd4akptNTIuY2xua3pDZQ%24FYu70tCWa%2FRgTkV8aUT%2BypX1akzTskzELKjwW7WAMvI',
    'odl_session': 'O9UA2hgWNkWyKZ4BdzlrP5g1QeHqsseGpWnWO5mg',
    'XSRF-TOKEN': 'eyJpdiI6InU2Y1BUaTdlaEI5VGdyZ2ZLTzRxc2c9PSIsInZhbHVlIjoidDdEWGpxdlhrRTNWY0ZJSS8wVk1hbUkvNDRPY1NWazB5cUNBeldxU2N1RTBVTnBlSi9hbWtiOGpLa3B4RVdoWlI0UXoxMGJaZEM0cmZ5eFNiaGZsc0VjUTY2N1U1cmJ5Qk9PKytyL1pSNmJFUEg0d2VOZm9YZ3MyQWxUaE1NMngiLCJtYWMiOiI3MTVkNzg2MWIxMDFmNTZkYmFkYzAwMjA3ZjU5NDFjNTZlMjU3NmU4MzBjMzMyNjBkM2ZiZDcxZWJlMjZkNDhiIiwidGFnIjoiIn0%3D',
}

headers = {
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=968507%7Cl8wSiDJ8zv8v4x9RHzbWRW66wxoN9mmw0NofCjwmRLR6iGRhJiLdxMsRADmn%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24bVd4akptNTIuY2xua3pDZQ%24FYu70tCWa%2FRgTkV8aUT%2BypX1akzTskzELKjwW7WAMvI; odl_session=O9UA2hgWNkWyKZ4BdzlrP5g1QeHqsseGpWnWO5mg; XSRF-TOKEN=eyJpdiI6InU2Y1BUaTdlaEI5VGdyZ2ZLTzRxc2c9PSIsInZhbHVlIjoidDdEWGpxdlhrRTNWY0ZJSS8wVk1hbUkvNDRPY1NWazB5cUNBeldxU2N1RTBVTnBlSi9hbWtiOGpLa3B4RVdoWlI0UXoxMGJaZEM0cmZ5eFNiaGZsc0VjUTY2N1U1cmJ5Qk9PKytyL1pSNmJFUEg0d2VOZm9YZ3MyQWxUaE1NMngiLCJtYWMiOiI3MTVkNzg2MWIxMDFmNTZkYmFkYzAwMjA3ZjU5NDFjNTZlMjU3NmU4MzBjMzMyNjBkM2ZiZDcxZWJlMjZkNDhiIiwidGFnIjoiIn0%3D',
    'Referer': 'https://applydl.dotm.gov.np/licence/category',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'X-Inertia': 'true',
    'X-Inertia-Version': 'abfe0d2fb15763f4d5db4390a711e362',
    'X-NewRelic-ID': 'VwMAWVNbCBAFVFVTDgEDX1U=',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'eyJpdiI6InU2Y1BUaTdlaEI5VGdyZ2ZLTzRxc2c9PSIsInZhbHVlIjoidDdEWGpxdlhrRTNWY0ZJSS8wVk1hbUkvNDRPY1NWazB5cUNBeldxU2N1RTBVTnBlSi9hbWtiOGpLa3B4RVdoWlI0UXoxMGJaZEM0cmZ5eFNiaGZsc0VjUTY2N1U1cmJ5Qk9PKytyL1pSNmJFUEg0d2VOZm9YZ3MyQWxUaE1NMngiLCJtYWMiOiI3MTVkNzg2MWIxMDFmNTZkYmFkYzAwMjA3ZjU5NDFjNTZlMjU3NmU4MzBjMzMyNjBkM2ZiZDcxZWJlMjZkNDhiIiwidGFnIjoiIn0=',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM1Nzg1ODAiLCJhcCI6IjUwNDE5MDUwOCIsImlkIjoiY2RmOGJhNGQwZmYxNmU2MiIsInRyIjoiMTAwZGQwZmIxZDFjMTY2NjYzMmU2NWFlN2Q3NDVhMGMiLCJ0aSI6MTY2NDc2MTk3NDk1MX19',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'traceparent': '00-100dd0fb1d1c1666632e65ae7d745a0c-cdf8ba4d0ff16e62-01',
    'tracestate': '3578580@nr=0-1-3578580-504190508-cdf8ba4d0ff16e62----1664761974951',
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
            if parsed['ad'] == '2022-10-18':
                print(parsed['ad'] + '   BOOKED  ' + str(parsed['booked']))
                print(parsed['ad'] + '  RESERVED  ' + str(parsed['reserved']))
                print(parsed['ad'] + '  AVAILABLE  ' + str(parsed['available']))
        print('  ')


def startt():
    Timer(120, startt).start()
    run()


startt()
