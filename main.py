import requests
import json
from pushbullet import Pushbullet

API_KEY = "o.HsKFaNxD4pvOo3cZUu2fyALu4Fq3pUEM"
pb = Pushbullet(API_KEY)

cookies = {
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '694691%7CMXrNqUx2OKmIcJCWaoCUxO1ajJAhKslAQ6jt0iVP0pONhPrYNha2z2TEzyy0%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24T1laYXEyNVphZUszaDJBWg%241e%2FFwRiaaYOGIxxNvJfYrWlO0rVRfvocmN3vKrIhQNs',
    'XSRF-TOKEN': 'eyJpdiI6Iit0NWFIZ2Exdk96TkNMSnZtUUpmQnc9PSIsInZhbHVlIjoiTktBMGcyZUpBY0JJNXRLMUk1b25qb2R1QmwzTW1RM3lFRjYrelJoNXpxMVFPTUlkNlpFVy9Vd2hJR2krU254VnhmaUszM2xJQVc3eVlwZXIvWkhudnB5K0NLMEVROG5pQklmNWh1RmtWNkhXSWxsK1FuN1JNTXdtSHhqem9rbzMiLCJtYWMiOiIwNjdlMzVlNDcyYzhhZjQ4YTVjNjE5MzYzOTc3OWE5OTcwZWE2ODI2MTcxZjA0Y2IwYjUyNjE4NThlYjg4NjZjIiwidGFnIjoiIn0%3D',
    'odl_session': 'sppcBrX1agTqMUNGBOCh68ZWdfGSViZIdUp3YDAx',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-GB,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://applydl.dotm.gov.np/license/apply',
    'Origin': 'https://applydl.dotm.gov.np',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=694691%7CMXrNqUx2OKmIcJCWaoCUxO1ajJAhKslAQ6jt0iVP0pONhPrYNha2z2TEzyy0%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24T1laYXEyNVphZUszaDJBWg%241e%2FFwRiaaYOGIxxNvJfYrWlO0rVRfvocmN3vKrIhQNs; XSRF-TOKEN=eyJpdiI6Iit0NWFIZ2Exdk96TkNMSnZtUUpmQnc9PSIsInZhbHVlIjoiTktBMGcyZUpBY0JJNXRLMUk1b25qb2R1QmwzTW1RM3lFRjYrelJoNXpxMVFPTUlkNlpFVy9Vd2hJR2krU254VnhmaUszM2xJQVc3eVlwZXIvWkhudnB5K0NLMEVROG5pQklmNWh1RmtWNkhXSWxsK1FuN1JNTXdtSHhqem9rbzMiLCJtYWMiOiIwNjdlMzVlNDcyYzhhZjQ4YTVjNjE5MzYzOTc3OWE5OTcwZWE2ODI2MTcxZjA0Y2IwYjUyNjE4NThlYjg4NjZjIiwidGFnIjoiIn0%3D; odl_session=sppcBrX1agTqMUNGBOCh68ZWdfGSViZIdUp3YDAx',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'X-NewRelic-ID': 'VwMAWVNbCBAFVFVTDgEDX1U=',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM1Nzg1ODAiLCJhcCI6IjUwNDE5MDUwOCIsImlkIjoiNTFiYTEyZmYyMWM0ZDM1OCIsInRyIjoiY2E2YzMzNjlmMmYwYTg1YzA4OTI5ZmE2MGUwZDQ4MWIiLCJ0aSI6MTY2MDEwMTMzMzc4OH19',
    'traceparent': '00-ca6c3369f2f0a85c08929fa60e0d481b-51ba12ff21c4d358-01',
    'tracestate': '3578580@nr=0-1-3578580-504190508-51ba12ff21c4d358----1660101333788',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'X-XSRF-TOKEN': 'eyJpdiI6Iit0NWFIZ2Exdk96TkNMSnZtUUpmQnc9PSIsInZhbHVlIjoiTktBMGcyZUpBY0JJNXRLMUk1b25qb2R1QmwzTW1RM3lFRjYrelJoNXpxMVFPTUlkNlpFVy9Vd2hJR2krU254VnhmaUszM2xJQVc3eVlwZXIvWkhudnB5K0NLMEVROG5pQklmNWh1RmtWNkhXSWxsK1FuN1JNTXdtSHhqem9rbzMiLCJtYWMiOiIwNjdlMzVlNDcyYzhhZjQ4YTVjNjE5MzYzOTc3OWE5OTcwZWE2ODI2MTcxZjA0Y2IwYjUyNjE4NThlYjg4NjZjIiwidGFnIjoiIn0=',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

categories = [1, 2, 3]

for cat in categories:
    json_data = {
        'is_urgent': False,
        'office_id': 19,
        'category_id': cat,
    }
    if cat == 1:
        cate = 'SCOOTER'
    if cat == 2:
        cate = 'BIKE'
    if cat == 3:
        cate = 'CAR'
    print(cat)
    response = requests.post('https://applydl.dotm.gov.np/license/quota', cookies=cookies, headers=headers,
                             json=json_data)
    data = json.loads(response.text)
    new = data['quotas']
    for every in data['quotas']:
        parsed = new[every]
        if parsed['available'] > 0:
            print(parsed['ad'])
            push = pb.push_note(cate, parsed['ad'] + '    ' + str(parsed['available']))
