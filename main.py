import requests
import json
from threading import Timer

cookies = {
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '1046352%7CLsJujv0Gf3y8T3DzUIT1wmfpozQFb67n2XnbtRNjJtgeFNfmhbZoiuKPVZPN%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24YzduOEVXbnY1TUFsbGluLw%24hBadRUDwmRJLW3m%2B7C%2BGKxIpf0wxbtiL57GGIuIsYuI',
    'XSRF-TOKEN': 'eyJpdiI6InQwdERpQmc5N0gxM1IycjlyQTAvN3c9PSIsInZhbHVlIjoicDJNUnF0L0M3c0d3V1cwOWowMWVjdWZFV2dwakd2OEtpSFlMQUgvbTJlQ2xlTWcwcWdCMVFrWmkzanNMZEJ6UldWTTRzWUI1NjI4V2toUk8vU2NmT081VGdlYjQ3Q0lhVzU3clNDNmhHbTNCRWhGUGpubThUQUYwdGRPV0VFVlQiLCJtYWMiOiI5YmIzYzJlYzNmNmFlZGUxZjNlMzM4ODMzZjkyM2EzNWZjZjQ0MjE2ZGE0MzRlZjg5MmQ2ZGI2YjA2ZGE1OGQzIiwidGFnIjoiIn0%3D',
    'odl_session': 'D2HHe8Tlvilo4FHXeHCss8blPgekBfF6TXGbOTui',
}

headers = {
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=1046352%7CLsJujv0Gf3y8T3DzUIT1wmfpozQFb67n2XnbtRNjJtgeFNfmhbZoiuKPVZPN%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24YzduOEVXbnY1TUFsbGluLw%24hBadRUDwmRJLW3m%2B7C%2BGKxIpf0wxbtiL57GGIuIsYuI; XSRF-TOKEN=eyJpdiI6InQwdERpQmc5N0gxM1IycjlyQTAvN3c9PSIsInZhbHVlIjoicDJNUnF0L0M3c0d3V1cwOWowMWVjdWZFV2dwakd2OEtpSFlMQUgvbTJlQ2xlTWcwcWdCMVFrWmkzanNMZEJ6UldWTTRzWUI1NjI4V2toUk8vU2NmT081VGdlYjQ3Q0lhVzU3clNDNmhHbTNCRWhGUGpubThUQUYwdGRPV0VFVlQiLCJtYWMiOiI5YmIzYzJlYzNmNmFlZGUxZjNlMzM4ODMzZjkyM2EzNWZjZjQ0MjE2ZGE0MzRlZjg5MmQ2ZGI2YjA2ZGE1OGQzIiwidGFnIjoiIn0%3D; odl_session=D2HHe8Tlvilo4FHXeHCss8blPgekBfF6TXGbOTui',
    'Referer': 'https://applydl.dotm.gov.np/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'X-Inertia': 'true',
    'X-Inertia-Version': 'abfe0d2fb15763f4d5db4390a711e362',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'eyJpdiI6InQwdERpQmc5N0gxM1IycjlyQTAvN3c9PSIsInZhbHVlIjoicDJNUnF0L0M3c0d3V1cwOWowMWVjdWZFV2dwakd2OEtpSFlMQUgvbTJlQ2xlTWcwcWdCMVFrWmkzanNMZEJ6UldWTTRzWUI1NjI4V2toUk8vU2NmT081VGdlYjQ3Q0lhVzU3clNDNmhHbTNCRWhGUGpubThUQUYwdGRPV0VFVlQiLCJtYWMiOiI5YmIzYzJlYzNmNmFlZGUxZjNlMzM4ODMzZjkyM2EzNWZjZjQ0MjE2ZGE0MzRlZjg5MmQ2ZGI2YjA2ZGE1OGQzIiwidGFnIjoiIn0=',
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
            if parsed['ad'] == '2022-10-18':
                print(parsed['ad'] + '   BOOKED  ' + str(parsed['booked']))
                print(parsed['ad'] + '  RESERVED  ' + str(parsed['reserved']))
                print(parsed['ad'] + '  AVAILABLE  ' + str(parsed['available']))
        print('  ')


def startt():
    Timer(120, startt).start()
    run()


startt()
