import requests
import json
from threading import Timer

cookies = {
    'odl_session': 'MqnLNPXq2qGa7OIuesukh7BfPJwqOP6o5IVAlClN',
    'XSRF-TOKEN': 'eyJpdiI6IndvYmxMeHlkejYrQmpVTjdPaFRrREE9PSIsInZhbHVlIjoid3pvL1NLN0xROUhGejNMMVZNczRwV2ZJKy9XV0ZzVVIrVGhlOXA0R3ZKUVlVdlFpUS9EbktVK0V3KzJGTG51Rm12VFRVTjhDcmFaTWcvSWVoUU1vSktOM0ZJUFBHZzloQndZRUNjTitDTFZrN3hXSmd3TFA4R0pFZGJ6RVBRYkYiLCJtYWMiOiIzMTcxOGNhMmVhN2QzOTdiZTMwNjJiZDcwNzlkZDg3ODM4MWQ0ZGExMGM3MzFlYWMyOWYxOTc0YThhZGQ1MjI5IiwidGFnIjoiIn0%3D',
}

headers = {
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'odl_session=MqnLNPXq2qGa7OIuesukh7BfPJwqOP6o5IVAlClN; XSRF-TOKEN=eyJpdiI6IndvYmxMeHlkejYrQmpVTjdPaFRrREE9PSIsInZhbHVlIjoid3pvL1NLN0xROUhGejNMMVZNczRwV2ZJKy9XV0ZzVVIrVGhlOXA0R3ZKUVlVdlFpUS9EbktVK0V3KzJGTG51Rm12VFRVTjhDcmFaTWcvSWVoUU1vSktOM0ZJUFBHZzloQndZRUNjTitDTFZrN3hXSmd3TFA4R0pFZGJ6RVBRYkYiLCJtYWMiOiIzMTcxOGNhMmVhN2QzOTdiZTMwNjJiZDcwNzlkZDg3ODM4MWQ0ZGExMGM3MzFlYWMyOWYxOTc0YThhZGQ1MjI5IiwidGFnIjoiIn0%3D',
    'Referer': 'https://applydl.dotm.gov.np/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'X-Inertia': 'true',
    'X-Inertia-Version': 'abfe0d2fb15763f4d5db4390a711e362',
    'X-NewRelic-ID': 'VwMAWVNbCBAFVFVTDgEDX1U=',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'eyJpdiI6IndvYmxMeHlkejYrQmpVTjdPaFRrREE9PSIsInZhbHVlIjoid3pvL1NLN0xROUhGejNMMVZNczRwV2ZJKy9XV0ZzVVIrVGhlOXA0R3ZKUVlVdlFpUS9EbktVK0V3KzJGTG51Rm12VFRVTjhDcmFaTWcvSWVoUU1vSktOM0ZJUFBHZzloQndZRUNjTitDTFZrN3hXSmd3TFA4R0pFZGJ6RVBRYkYiLCJtYWMiOiIzMTcxOGNhMmVhN2QzOTdiZTMwNjJiZDcwNzlkZDg3ODM4MWQ0ZGExMGM3MzFlYWMyOWYxOTc0YThhZGQ1MjI5IiwidGFnIjoiIn0=',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM1Nzg1ODAiLCJhcCI6IjUwNDE5MDUwOCIsImlkIjoiMjhlZmI1MTJiZDA1NTU1ZCIsInRyIjoiOTcwNGI1YTBiN2Y1YmJkOTQzYmY2Y2VkN2MxOGYwMDciLCJ0aSI6MTY2NDc2OTU4MTk3N319',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'traceparent': '00-9704b5a0b7f5bbd943bf6ced7c18f007-28efb512bd05555d-01',
    'tracestate': '3578580@nr=0-1-3578580-504190508-28efb512bd05555d----1664769581977',
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
