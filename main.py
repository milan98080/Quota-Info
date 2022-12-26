import requests
import json
from threading import Timer

cookies = {
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '973593%7Co3c6NMSCelPD4Jsis3DCEflQ280P7cdwS6WV9v04VyaR0JNxvg22ugs2Pr36%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24YnBNY1hGMTRwU3VpWG05Qw%24gt1914SeJeVouqS3x6fceNqhZjVkzQppt1Ke7AQbKu8',
    'odl_session': 'zqZnix6DONkjZkFEbx0zarWoJLHBjHdSrICoS6lt',
    'XSRF-TOKEN': 'eyJpdiI6IjhxQXpxQVNOTUxIK25FQ1lqUHRoaUE9PSIsInZhbHVlIjoidmhtTzhrZTAzSlNrV2dydjcwekx4anNlYmtoNFM5SlQrSGYxK3ZUM0o5aHltaWZuMU9tTk9uNWdENHFzSXpGRG1CbEJiRkx5VDRpb2FKcGxOTHA4QVczUFo5OEhzaFR6UzB5cFVuMms2dmpIdnUySGpkY3NjdFlYSmIrckszOXEiLCJtYWMiOiIyNmQ4YWVhZmM4Mjc5YzFjOGMwMDBlODhjNzBjZDQ4Njk4N2I1YTkyNjVhZWJhMDhmYTFiZDE1MzY4NjAzODBiIiwidGFnIjoiIn0%3D',
}

headers = {
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=973593%7Co3c6NMSCelPD4Jsis3DCEflQ280P7cdwS6WV9v04VyaR0JNxvg22ugs2Pr36%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24YnBNY1hGMTRwU3VpWG05Qw%24gt1914SeJeVouqS3x6fceNqhZjVkzQppt1Ke7AQbKu8; odl_session=zqZnix6DONkjZkFEbx0zarWoJLHBjHdSrICoS6lt; XSRF-TOKEN=eyJpdiI6IjhxQXpxQVNOTUxIK25FQ1lqUHRoaUE9PSIsInZhbHVlIjoidmhtTzhrZTAzSlNrV2dydjcwekx4anNlYmtoNFM5SlQrSGYxK3ZUM0o5aHltaWZuMU9tTk9uNWdENHFzSXpGRG1CbEJiRkx5VDRpb2FKcGxOTHA4QVczUFo5OEhzaFR6UzB5cFVuMms2dmpIdnUySGpkY3NjdFlYSmIrckszOXEiLCJtYWMiOiIyNmQ4YWVhZmM4Mjc5YzFjOGMwMDBlODhjNzBjZDQ4Njk4N2I1YTkyNjVhZWJhMDhmYTFiZDE1MzY4NjAzODBiIiwidGFnIjoiIn0%3D',
    'Referer': 'https://applydl.dotm.gov.np/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'X-Inertia': 'true',
    'X-Inertia-Version': '29261dd93cf97c2e4a714179fe7a4a9b',
    'X-NewRelic-ID': 'VwMAWVNbCBAFVFVTDgEDX1U=',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'eyJpdiI6IjhxQXpxQVNOTUxIK25FQ1lqUHRoaUE9PSIsInZhbHVlIjoidmhtTzhrZTAzSlNrV2dydjcwekx4anNlYmtoNFM5SlQrSGYxK3ZUM0o5aHltaWZuMU9tTk9uNWdENHFzSXpGRG1CbEJiRkx5VDRpb2FKcGxOTHA4QVczUFo5OEhzaFR6UzB5cFVuMms2dmpIdnUySGpkY3NjdFlYSmIrckszOXEiLCJtYWMiOiIyNmQ4YWVhZmM4Mjc5YzFjOGMwMDBlODhjNzBjZDQ4Njk4N2I1YTkyNjVhZWJhMDhmYTFiZDE1MzY4NjAzODBiIiwidGFnIjoiIn0=',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM1Nzg1ODAiLCJhcCI6IjUwNDE5MDUwOCIsImlkIjoiZTI3NmIzNmJmYzMzOGQzZiIsInRyIjoiNTBhZThjZWMzMzMwOGU1ZmM4MzFmYzEwODMxZDdhYjAiLCJ0aSI6MTY3MjAxOTkxMjM5M319',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'traceparent': '00-50ae8cec33308e5fc831fc10831d7ab0-e276b36bfc338d3f-01',
    'tracestate': '3578580@nr=0-1-3578580-504190508-e276b36bfc338d3f----1672019912393',
}

def run():
    categories = [1, 2, 3, 8, 9]

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
            if parsed['ad'] == '2023-01-08':
                print(parsed['ad'] + '   BOOKED  ' + str(parsed['booked']))
                print(parsed['ad'] + '  RESERVED  ' + str(parsed['reserved']))
                print(parsed['ad'] + '  AVAILABLE  ' + str(parsed['available']))
        print('  ')


def startt():
    Timer(60, startt).start()
    run()


startt()
