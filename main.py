import requests
import json
from threading import Timer

cookies = {
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '700903%7C4MZ4dSv2841wO97KiollSWbInCHEtHGefdig8T7HdMUIJcjTmrzbtNWQaSg3%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24eVQ3cll0ZmkweE84MWNicA%24BeDPuvur0h50eRHSpvK4bH1xO%2BPGvUkZb5ahYBoUvKc',
    'odl_session': 'SJGfQ1zInnNmIkWa7mZDNUSeGqB3a2EcfEl9wMye',
    'XSRF-TOKEN': 'eyJpdiI6IllQVlNWd2NMa1NrRG54UUtRTFozMWc9PSIsInZhbHVlIjoiYi85VGRZZlh6UGhmZURkT0xwNFgwOUViWk9wR2ZiM2IwM01uc0lIN2VhWFJybTEvNHJMdFNMUFF0WDRGdTJrSFg4V2l1MDZobkFINCtzeE5VTnppWHd6bEtHZjllZ3lHaXNxRDBPQ3hoc3pxWUR0S05CVVBkd1lkalpiRjNobzQiLCJtYWMiOiI3ZTNlYzQ1MDNlYjQyNTU4YzQ4MjgzMGMzNTMxNWFkZjBiY2NiZmNiZWNiYTI0MmZiYmU2Yjg5MDY2N2VlZmE0IiwidGFnIjoiIn0%3D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Inertia': 'true',
    'X-Inertia-Version': '26f5d68a49eb03710177f0ba3873ab38',
    'Content-Type': 'application/json',
    'X-XSRF-TOKEN': 'eyJpdiI6IllQVlNWd2NMa1NrRG54UUtRTFozMWc9PSIsInZhbHVlIjoiYi85VGRZZlh6UGhmZURkT0xwNFgwOUViWk9wR2ZiM2IwM01uc0lIN2VhWFJybTEvNHJMdFNMUFF0WDRGdTJrSFg4V2l1MDZobkFINCtzeE5VTnppWHd6bEtHZjllZ3lHaXNxRDBPQ3hoc3pxWUR0S05CVVBkd1lkalpiRjNobzQiLCJtYWMiOiI3ZTNlYzQ1MDNlYjQyNTU4YzQ4MjgzMGMzNTMxNWFkZjBiY2NiZmNiZWNiYTI0MmZiYmU2Yjg5MDY2N2VlZmE0IiwidGFnIjoiIn0=',
    'Connection': 'keep-alive',
    'Referer': 'https://applydl.dotm.gov.np/category',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=700903%7C4MZ4dSv2841wO97KiollSWbInCHEtHGefdig8T7HdMUIJcjTmrzbtNWQaSg3%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24eVQ3cll0ZmkweE84MWNicA%24BeDPuvur0h50eRHSpvK4bH1xO%2BPGvUkZb5ahYBoUvKc; odl_session=SJGfQ1zInnNmIkWa7mZDNUSeGqB3a2EcfEl9wMye; XSRF-TOKEN=eyJpdiI6IllQVlNWd2NMa1NrRG54UUtRTFozMWc9PSIsInZhbHVlIjoiYi85VGRZZlh6UGhmZURkT0xwNFgwOUViWk9wR2ZiM2IwM01uc0lIN2VhWFJybTEvNHJMdFNMUFF0WDRGdTJrSFg4V2l1MDZobkFINCtzeE5VTnppWHd6bEtHZjllZ3lHaXNxRDBPQ3hoc3pxWUR0S05CVVBkd1lkalpiRjNobzQiLCJtYWMiOiI3ZTNlYzQ1MDNlYjQyNTU4YzQ4MjgzMGMzNTMxNWFkZjBiY2NiZmNiZWNiYTI0MmZiYmU2Yjg5MDY2N2VlZmE0IiwidGFnIjoiIn0%3D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
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
