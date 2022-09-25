import requests
import json
from threading import Timer

cookies = {
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '700903%7Cux7XZ6fwluJnZP9ZavvL0LxxiViZJgYctJPaztKNaDqGd9KFUUPXZqz03zZ0%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24eVQ3cll0ZmkweE84MWNicA%24BeDPuvur0h50eRHSpvK4bH1xO%2BPGvUkZb5ahYBoUvKc',
    'odl_session': 'mkA7qJYSSFWTVCsJHlIGaTJCw6mYfQi5IC8wXWoz',
    'XSRF-TOKEN': 'eyJpdiI6IjJPNmpBUVV2TFBidHJqeTZGcUdJZkE9PSIsInZhbHVlIjoiMlAwZHZMUmhyRVhicHBnUUJ3UjU5czNkUk5Kdk5TYzBLbklCb2Jya2JZMFdZRDJjWitqYlk5azZ3NVZjTmpnMU1Oc2xQUVFuZXptNm5BMU9hQTNxcEdDdU5PMUVWaGh4SnFqZEUyNnV2cFNwV0xaOWx6c2FWY0hWYW4vSHVpczciLCJtYWMiOiIzYmYzZDgyMGRmZDc1ZGIwNzI3YjAwZDY5ZjRlMDkzOGE4YzFkMDgxYzA2MWJlYjUwYzQwOGY1YTM4ZDM1ZjViIiwidGFnIjoiIn0%3D',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=700903%7Cux7XZ6fwluJnZP9ZavvL0LxxiViZJgYctJPaztKNaDqGd9KFUUPXZqz03zZ0%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24eVQ3cll0ZmkweE84MWNicA%24BeDPuvur0h50eRHSpvK4bH1xO%2BPGvUkZb5ahYBoUvKc; odl_session=mkA7qJYSSFWTVCsJHlIGaTJCw6mYfQi5IC8wXWoz; XSRF-TOKEN=eyJpdiI6IjJPNmpBUVV2TFBidHJqeTZGcUdJZkE9PSIsInZhbHVlIjoiMlAwZHZMUmhyRVhicHBnUUJ3UjU5czNkUk5Kdk5TYzBLbklCb2Jya2JZMFdZRDJjWitqYlk5azZ3NVZjTmpnMU1Oc2xQUVFuZXptNm5BMU9hQTNxcEdDdU5PMUVWaGh4SnFqZEUyNnV2cFNwV0xaOWx6c2FWY0hWYW4vSHVpczciLCJtYWMiOiIzYmYzZDgyMGRmZDc1ZGIwNzI3YjAwZDY5ZjRlMDkzOGE4YzFkMDgxYzA2MWJlYjUwYzQwOGY1YTM4ZDM1ZjViIiwidGFnIjoiIn0%3D',
    'Origin': 'https://applydl.dotm.gov.np',
    'Referer': 'https://applydl.dotm.gov.np/license/category',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-XSRF-TOKEN': 'eyJpdiI6IjJPNmpBUVV2TFBidHJqeTZGcUdJZkE9PSIsInZhbHVlIjoiMlAwZHZMUmhyRVhicHBnUUJ3UjU5czNkUk5Kdk5TYzBLbklCb2Jya2JZMFdZRDJjWitqYlk5azZ3NVZjTmpnMU1Oc2xQUVFuZXptNm5BMU9hQTNxcEdDdU5PMUVWaGh4SnFqZEUyNnV2cFNwV0xaOWx6c2FWY0hWYW4vSHVpczciLCJtYWMiOiIzYmYzZDgyMGRmZDc1ZGIwNzI3YjAwZDY5ZjRlMDkzOGE4YzFkMDgxYzA2MWJlYjUwYzQwOGY1YTM4ZDM1ZjViIiwidGFnIjoiIn0=',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Chromium";v="106"',
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
            if parsed['ad'] == '2022-09-11':
                print(parsed['ad'] + '   BOOKED  ' + str(parsed['booked']))
                print(parsed['ad'] + '  RESERVED  ' + str(parsed['reserved']))
                print(parsed['ad'] + '  AVAILABLE  ' + str(parsed['available']))
        print('  ')


def startt():
    Timer(120, startt).start()
    run()


startt()
