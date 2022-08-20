import requests
import json
from threading import Timer

cookies = {
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '694691%7CGdkDFZaSj2zNcW1zMMFERRPRBYxi5vLliweNp6fhiA7E0CImxddlKQDHDjWU%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24T1laYXEyNVphZUszaDJBWg%241e%2FFwRiaaYOGIxxNvJfYrWlO0rVRfvocmN3vKrIhQNs',
    'XSRF-TOKEN': 'eyJpdiI6InhqcXpqTmh6VlE3cGVQUWZGNkpHcFE9PSIsInZhbHVlIjoiNlFLMVVQdUNvMWtlSjhKOFJ3K3lwT3AxdU5oL3d5OXh6ZDNrTjVGMWpXK2VnK2RmVWhoRHFXRkcra1NsTnpVcEQ5eUpGZnNKQ1BSWkFTWGR3N3kvSEk2Z0psTzl5b2MydjN5Yi9qZlVnK3BqejREMFZyZ1pVZk1NNjEzc2d2M2EiLCJtYWMiOiJkYjc4NWQxYWE1YjliOTdmMmQ2ZWI4MDQyMWQxNjUyZGE4YzNkYjRkYWQ0MzU4MDliNDM3YzFlZWQ3ZTVkYWVmIiwidGFnIjoiIn0%3D',
    'odl_session': 'adVyA6NsfLJOkI8vWJpN2X2n8NGsiK9JqhiAIs49',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'X-XSRF-TOKEN': 'eyJpdiI6InhqcXpqTmh6VlE3cGVQUWZGNkpHcFE9PSIsInZhbHVlIjoiNlFLMVVQdUNvMWtlSjhKOFJ3K3lwT3AxdU5oL3d5OXh6ZDNrTjVGMWpXK2VnK2RmVWhoRHFXRkcra1NsTnpVcEQ5eUpGZnNKQ1BSWkFTWGR3N3kvSEk2Z0psTzl5b2MydjN5Yi9qZlVnK3BqejREMFZyZ1pVZk1NNjEzc2d2M2EiLCJtYWMiOiJkYjc4NWQxYWE1YjliOTdmMmQ2ZWI4MDQyMWQxNjUyZGE4YzNkYjRkYWQ0MzU4MDliNDM3YzFlZWQ3ZTVkYWVmIiwidGFnIjoiIn0=',
    'Origin': 'https://applydl.dotm.gov.np',
    'Connection': 'keep-alive',
    'Referer': 'https://applydl.dotm.gov.np/license/category',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=694691%7CGdkDFZaSj2zNcW1zMMFERRPRBYxi5vLliweNp6fhiA7E0CImxddlKQDHDjWU%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24T1laYXEyNVphZUszaDJBWg%241e%2FFwRiaaYOGIxxNvJfYrWlO0rVRfvocmN3vKrIhQNs; XSRF-TOKEN=eyJpdiI6InhqcXpqTmh6VlE3cGVQUWZGNkpHcFE9PSIsInZhbHVlIjoiNlFLMVVQdUNvMWtlSjhKOFJ3K3lwT3AxdU5oL3d5OXh6ZDNrTjVGMWpXK2VnK2RmVWhoRHFXRkcra1NsTnpVcEQ5eUpGZnNKQ1BSWkFTWGR3N3kvSEk2Z0psTzl5b2MydjN5Yi9qZlVnK3BqejREMFZyZ1pVZk1NNjEzc2d2M2EiLCJtYWMiOiJkYjc4NWQxYWE1YjliOTdmMmQ2ZWI4MDQyMWQxNjUyZGE4YzNkYjRkYWQ0MzU4MDliNDM3YzFlZWQ3ZTVkYWVmIiwidGFnIjoiIn0%3D; odl_session=adVyA6NsfLJOkI8vWJpN2X2n8NGsiK9JqhiAIs49',
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
            if parsed['ad'] == '2022-09-05':
                print(parsed['ad'] + '  AVAILABLE  ' + str(parsed['available']))
        print('  ')


def startt():
    Timer(5, startt).start()
    run()


startt()
