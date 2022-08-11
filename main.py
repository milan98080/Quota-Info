import requests
import json
from pushbullet import Pushbullet
from threading import Timer

API_KEY = "o.HsKFaNxD4pvOo3cZUu2fyALu4Fq3pUEM"
pb = Pushbullet(API_KEY)

cookies = {
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '694691%7CMXrNqUx2OKmIcJCWaoCUxO1ajJAhKslAQ6jt0iVP0pONhPrYNha2z2TEzyy0%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24T1laYXEyNVphZUszaDJBWg%241e%2FFwRiaaYOGIxxNvJfYrWlO0rVRfvocmN3vKrIhQNs',
    'XSRF-TOKEN': 'eyJpdiI6IlpkS1RCYVZ6ZGFpczhQdmUvK3I4Ync9PSIsInZhbHVlIjoiMUI5VU5vemE1aDFjVVJnNzRFQ0hWQU1FQklXMndFd045UmxtdVdnTjVEMlVBbmhhalUwZGYzMGY1c0c4dmhqd3c4QTBtM21GK1lGNjROVXNOVTRGdW01OWhmOXBtbUlNVURhbEpMZGNwYWErSFIrSjZrY3U1NkVSZ0VHS0M3UWYiLCJtYWMiOiJkMzc4NzQzMjFiNzM2YWI0MmRlNGU4MDM1OWNjNGIwY2U3MzAxMTM5M2VkMDJkNzZmMWY2OWQ1MmYxZDUyOTZmIiwidGFnIjoiIn0%3D',
    'odl_session': 'l1qxH4kS93Fg3qGnPe4YgTE2AdbxjHYNleVLqbfy',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-GB,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-NewRelic-ID': 'VwMAWVNbCBAFVFVTDgEDX1U=',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM1Nzg1ODAiLCJhcCI6IjUwNDE5MDUwOCIsImlkIjoiNDk2NGE3YmYwNmEwMTUzNyIsInRyIjoiNzlkMjcyOTc5NjI5NjdmYWM5Yzk3ZjhiOTUwZGFhMWQiLCJ0aSI6MTY2MDE4NDczNjg0NX19',
    'traceparent': '00-79d27297962967fac9c97f8b950daa1d-4964a7bf06a01537-01',
    'tracestate': '3578580@nr=0-1-3578580-504190508-4964a7bf06a01537----1660184736845',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'X-XSRF-TOKEN': 'eyJpdiI6IlpkS1RCYVZ6ZGFpczhQdmUvK3I4Ync9PSIsInZhbHVlIjoiMUI5VU5vemE1aDFjVVJnNzRFQ0hWQU1FQklXMndFd045UmxtdVdnTjVEMlVBbmhhalUwZGYzMGY1c0c4dmhqd3c4QTBtM21GK1lGNjROVXNOVTRGdW01OWhmOXBtbUlNVURhbEpMZGNwYWErSFIrSjZrY3U1NkVSZ0VHS0M3UWYiLCJtYWMiOiJkMzc4NzQzMjFiNzM2YWI0MmRlNGU4MDM1OWNjNGIwY2U3MzAxMTM5M2VkMDJkNzZmMWY2OWQ1MmYxZDUyOTZmIiwidGFnIjoiIn0=',
    'Origin': 'https://applydl.dotm.gov.np',
    'Connection': 'keep-alive',
    'Referer': 'https://applydl.dotm.gov.np/license/category',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=694691%7CMXrNqUx2OKmIcJCWaoCUxO1ajJAhKslAQ6jt0iVP0pONhPrYNha2z2TEzyy0%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24T1laYXEyNVphZUszaDJBWg%241e%2FFwRiaaYOGIxxNvJfYrWlO0rVRfvocmN3vKrIhQNs; XSRF-TOKEN=eyJpdiI6IlpkS1RCYVZ6ZGFpczhQdmUvK3I4Ync9PSIsInZhbHVlIjoiMUI5VU5vemE1aDFjVVJnNzRFQ0hWQU1FQklXMndFd045UmxtdVdnTjVEMlVBbmhhalUwZGYzMGY1c0c4dmhqd3c4QTBtM21GK1lGNjROVXNOVTRGdW01OWhmOXBtbUlNVURhbEpMZGNwYWErSFIrSjZrY3U1NkVSZ0VHS0M3UWYiLCJtYWMiOiJkMzc4NzQzMjFiNzM2YWI0MmRlNGU4MDM1OWNjNGIwY2U3MzAxMTM5M2VkMDJkNzZmMWY2OWQ1MmYxZDUyOTZmIiwidGFnIjoiIn0%3D; odl_session=l1qxH4kS93Fg3qGnPe4YgTE2AdbxjHYNleVLqbfy',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}


def run():
    pb.push_note('________________________________________', '_________________________________________')
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
    Timer(30, run).start()


run()
