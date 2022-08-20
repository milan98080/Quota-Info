import requests
import json
from pushbullet import Pushbullet
from threading import Timer

API_KEY = "o.53fergJdWezg7vDwJNVIQOh1oxzEAMp4"
pb = Pushbullet(API_KEY)
cookies = {
    'odl_session': 'r40OC13wexXRfq5vdsGReSOhsEBo2cdY07nuiCgr',
    'XSRF-TOKEN': 'eyJpdiI6IklSaHMxdm03MFZtMTMrWXVnRzBDU3c9PSIsInZhbHVlIjoiSGNUYVJTWDNjM0dCWUxna3JrWFI4ampHMFh5VjBBckJKMTQwaEpUaExabVp4TGNISXRLWDFmUnJ6NUJnVmVlZGZtY2pxM2FFaTNkdks5WG1tTXVrRUlYU2NrdXIvanhsWHBGems1d1hQb2FxQ1AxZFBNeEJsN0s1eXQ0QzRxVnEiLCJtYWMiOiI5YWE3OTgwNGNkYmI2N2I5ZmRiZGRiZjcyY2M5ZTY4YjZhNDZmZTlmYWJjZTI0NDM4YTA2ODg5OTY2YmE5NDFhIiwidGFnIjoiIn0%3D',
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '776653%7CZiGzgUaFnjy6afetK7HyZ4F4BGog2BRuioi67E3L5rEBP1Fzc68do2jNukIb%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24aEwvY3N5S0wvanVIaFJkQw%24NmYohpLyTc9cUSKbSgIhmvyXMeYRqSe52eqmxNVqYz4',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-NewRelic-ID': 'VwMAWVNbCBAFVFVTDgEDX1U=',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM1Nzg1ODAiLCJhcCI6IjUwNDE5MDUwOCIsImlkIjoiMDdlODU4ZWY4OTE0MTEzOSIsInRyIjoiZDQ0ZmRjOTBmYzkyNmY0NDAwYTM1YWU5Mzg3ZmI0N2UiLCJ0aSI6MTY2MDk2MDQ5NjYyMX19',
    'traceparent': '00-d44fdc90fc926f4400a35ae9387fb47e-07e858ef89141139-01',
    'tracestate': '3578580@nr=0-1-3578580-504190508-07e858ef89141139----1660960496621',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Inertia': 'true',
    'X-Inertia-Version': 'cdb50dac51654840c8749340fa358a8d',
    'Content-Type': 'application/json',
    'X-XSRF-TOKEN': 'eyJpdiI6IklSaHMxdm03MFZtMTMrWXVnRzBDU3c9PSIsInZhbHVlIjoiSGNUYVJTWDNjM0dCWUxna3JrWFI4ampHMFh5VjBBckJKMTQwaEpUaExabVp4TGNISXRLWDFmUnJ6NUJnVmVlZGZtY2pxM2FFaTNkdks5WG1tTXVrRUlYU2NrdXIvanhsWHBGems1d1hQb2FxQ1AxZFBNeEJsN0s1eXQ0QzRxVnEiLCJtYWMiOiI5YWE3OTgwNGNkYmI2N2I5ZmRiZGRiZjcyY2M5ZTY4YjZhNDZmZTlmYWJjZTI0NDM4YTA2ODg5OTY2YmE5NDFhIiwidGFnIjoiIn0=',
    'Connection': 'keep-alive',
    'Referer': 'https://applydl.dotm.gov.np/category',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'odl_session=r40OC13wexXRfq5vdsGReSOhsEBo2cdY07nuiCgr; XSRF-TOKEN=eyJpdiI6IklSaHMxdm03MFZtMTMrWXVnRzBDU3c9PSIsInZhbHVlIjoiSGNUYVJTWDNjM0dCWUxna3JrWFI4ampHMFh5VjBBckJKMTQwaEpUaExabVp4TGNISXRLWDFmUnJ6NUJnVmVlZGZtY2pxM2FFaTNkdks5WG1tTXVrRUlYU2NrdXIvanhsWHBGems1d1hQb2FxQ1AxZFBNeEJsN0s1eXQ0QzRxVnEiLCJtYWMiOiI5YWE3OTgwNGNkYmI2N2I5ZmRiZGRiZjcyY2M5ZTY4YjZhNDZmZTlmYWJjZTI0NDM4YTA2ODg5OTY2YmE5NDFhIiwidGFnIjoiIn0%3D; remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=776653%7CZiGzgUaFnjy6afetK7HyZ4F4BGog2BRuioi67E3L5rEBP1Fzc68do2jNukIb%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24aEwvY3N5S0wvanVIaFJkQw%24NmYohpLyTc9cUSKbSgIhmvyXMeYRqSe52eqmxNVqYz4',
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
        response = requests.post('https://applydl.dotm.gov.np/license/quota', cookies=cookies, headers=headers,
                                 json=json_data)
        data = json.loads(response.text)
        new = data['quotas']
        for every in data['quotas']:
            parsed = new[every]
            if parsed['ad'] == '2022-08-29' and parsed['available'] != 100:
                print(cate + '  AVAILABLE  ' + str(parsed['available']))
                #push = pb.push_note(cate, '  AVAILABLE  ' + str(parsed['available']))


def startt():
    Timer(30, startt).start()
    run()


startt()
