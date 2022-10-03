import requests
import json
from threading import Timer

cookies = {
    'odl_session': 'i94oucXMXa2sANNF5wMnQ2HKfIiBQZ2FLiH2tMgA',
    'XSRF-TOKEN': 'eyJpdiI6InhOMCtheGE0VmFGNkUra2J5NnFOM1E9PSIsInZhbHVlIjoiQm5GMndjU3Y5d0daem0zQnZicXhTTklqbU5JOXF6enpHZUlaRHpINHhod0ZXUmkxUEcyZFpSYXM4QTVrMWlzeFlLRGh1NkRQMTVONHphWlBDOGd5c3dqSHc2WFl3VG5wZm5VTjQzSWhBVGhNVG53T284aEVzZGd0MDFWbW1yeUoiLCJtYWMiOiI1MGI5NDU0M2MxMTliNTJkMzZjODllNmM5ODU4NzRiYjY4OTJlY2Y0NmM3OTM2NjRmZDEwMmFmNzAwMzQ3OTYyIiwidGFnIjoiIn0%3D',
}

headers = {
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'odl_session=i94oucXMXa2sANNF5wMnQ2HKfIiBQZ2FLiH2tMgA; XSRF-TOKEN=eyJpdiI6InhOMCtheGE0VmFGNkUra2J5NnFOM1E9PSIsInZhbHVlIjoiQm5GMndjU3Y5d0daem0zQnZicXhTTklqbU5JOXF6enpHZUlaRHpINHhod0ZXUmkxUEcyZFpSYXM4QTVrMWlzeFlLRGh1NkRQMTVONHphWlBDOGd5c3dqSHc2WFl3VG5wZm5VTjQzSWhBVGhNVG53T284aEVzZGd0MDFWbW1yeUoiLCJtYWMiOiI1MGI5NDU0M2MxMTliNTJkMzZjODllNmM5ODU4NzRiYjY4OTJlY2Y0NmM3OTM2NjRmZDEwMmFmNzAwMzQ3OTYyIiwidGFnIjoiIn0%3D',
    'Referer': 'https://applydl.dotm.gov.np/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'X-Inertia': 'true',
    'X-Inertia-Version': 'abfe0d2fb15763f4d5db4390a711e362',
    'X-NewRelic-ID': 'VwMAWVNbCBAFVFVTDgEDX1U=',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'eyJpdiI6InhOMCtheGE0VmFGNkUra2J5NnFOM1E9PSIsInZhbHVlIjoiQm5GMndjU3Y5d0daem0zQnZicXhTTklqbU5JOXF6enpHZUlaRHpINHhod0ZXUmkxUEcyZFpSYXM4QTVrMWlzeFlLRGh1NkRQMTVONHphWlBDOGd5c3dqSHc2WFl3VG5wZm5VTjQzSWhBVGhNVG53T284aEVzZGd0MDFWbW1yeUoiLCJtYWMiOiI1MGI5NDU0M2MxMTliNTJkMzZjODllNmM5ODU4NzRiYjY4OTJlY2Y0NmM3OTM2NjRmZDEwMmFmNzAwMzQ3OTYyIiwidGFnIjoiIn0=',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM1Nzg1ODAiLCJhcCI6IjUwNDE5MDUwOCIsImlkIjoiMjQzMTg2NWI5YTBkNGJjMyIsInRyIjoiN2VkMDZiZDAyZmUyMjhmMThiOGMyMjYyMDgwNDhjY2IiLCJ0aSI6MTY2NDc2NTgyODI5NH19',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'traceparent': '00-7ed06bd02fe228f18b8c226208048ccb-2431865b9a0d4bc3-01',
    'tracestate': '3578580@nr=0-1-3578580-504190508-2431865b9a0d4bc3----1664765828294',
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
