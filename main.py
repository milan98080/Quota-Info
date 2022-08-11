import requests
import json
from pushbullet import Pushbullet
from threading import Timer

API_KEY = "o.HsKFaNxD4pvOo3cZUu2fyALu4Fq3pUEM"
pb = Pushbullet(API_KEY)
cookies = {
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '694691%7CSFooPAzLOCxbX0aXaDFbtENONBllgMJlMraTxeAYNqK2WqrGPoHRkk0t4IC2%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24T1laYXEyNVphZUszaDJBWg%241e%2FFwRiaaYOGIxxNvJfYrWlO0rVRfvocmN3vKrIhQNs',
    'XSRF-TOKEN': 'eyJpdiI6Im5MOFFCSVI1V0xBZVRwRUVOUG1qRUE9PSIsInZhbHVlIjoiVktwUU5CTFNSOG1oM1ZtMllhakpsWDJpTm5mQmVZdVNpQWRZai83Z3l3NzhrOW04bWxVTDYvOHhqOWVZVXhIaHAvWDRFMUJLdzRMaStCTTlabXBBdEM0WjVzQWk1czlwWEw1dEgrUlRxNmxjMVhSWUtLcUsyVlRwZGRqRzNBUHAiLCJtYWMiOiIyODUzNDNhMWVlNmJmOTczMzJlNzY5ODhkNDg3NTY1YjEzZmI0Y2UxNjA5Nzk2Mzg2NmFjNDBhY2NhOGQ1NjBjIiwidGFnIjoiIn0%3D',
    'odl_session': '3zkFWPCxNpemkQeSJRPlOPYgVoW9Gm4K8quzKd1v',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-GB,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-NewRelic-ID': 'VwMAWVNbCBAFVFVTDgEDX1U=',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM1Nzg1ODAiLCJhcCI6IjUwNDE5MDUwOCIsImlkIjoiM2UwMWZkNGY2OWNkN2IxMSIsInRyIjoiZDRkODYyMzllNDc3MzA0Y2U3N2Q1YzliMWUzYzExMDkiLCJ0aSI6MTY2MDIwNTQyODAwMH19',
    'traceparent': '00-d4d86239e477304ce77d5c9b1e3c1109-3e01fd4f69cd7b11-01',
    'tracestate': '3578580@nr=0-1-3578580-504190508-3e01fd4f69cd7b11----1660205428000',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'X-XSRF-TOKEN': 'eyJpdiI6Im5MOFFCSVI1V0xBZVRwRUVOUG1qRUE9PSIsInZhbHVlIjoiVktwUU5CTFNSOG1oM1ZtMllhakpsWDJpTm5mQmVZdVNpQWRZai83Z3l3NzhrOW04bWxVTDYvOHhqOWVZVXhIaHAvWDRFMUJLdzRMaStCTTlabXBBdEM0WjVzQWk1czlwWEw1dEgrUlRxNmxjMVhSWUtLcUsyVlRwZGRqRzNBUHAiLCJtYWMiOiIyODUzNDNhMWVlNmJmOTczMzJlNzY5ODhkNDg3NTY1YjEzZmI0Y2UxNjA5Nzk2Mzg2NmFjNDBhY2NhOGQ1NjBjIiwidGFnIjoiIn0=',
    'Origin': 'https://applydl.dotm.gov.np',
    'Connection': 'keep-alive',
    'Referer': 'https://applydl.dotm.gov.np/license/category',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=694691%7CSFooPAzLOCxbX0aXaDFbtENONBllgMJlMraTxeAYNqK2WqrGPoHRkk0t4IC2%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24T1laYXEyNVphZUszaDJBWg%241e%2FFwRiaaYOGIxxNvJfYrWlO0rVRfvocmN3vKrIhQNs; XSRF-TOKEN=eyJpdiI6Im5MOFFCSVI1V0xBZVRwRUVOUG1qRUE9PSIsInZhbHVlIjoiVktwUU5CTFNSOG1oM1ZtMllhakpsWDJpTm5mQmVZdVNpQWRZai83Z3l3NzhrOW04bWxVTDYvOHhqOWVZVXhIaHAvWDRFMUJLdzRMaStCTTlabXBBdEM0WjVzQWk1czlwWEw1dEgrUlRxNmxjMVhSWUtLcUsyVlRwZGRqRzNBUHAiLCJtYWMiOiIyODUzNDNhMWVlNmJmOTczMzJlNzY5ODhkNDg3NTY1YjEzZmI0Y2UxNjA5Nzk2Mzg2NmFjNDBhY2NhOGQ1NjBjIiwidGFnIjoiIn0%3D; odl_session=3zkFWPCxNpemkQeSJRPlOPYgVoW9Gm4K8quzKd1v',
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
            if parsed['available'] > 0:
                push = pb.push_note(cate, parsed['ad'] + '    ' + str(parsed['available']))


def startt():
    Timer(5, startt).start()
    run()


startt()
