import requests
import json
from threading import Timer

cookies = {
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '776653%7CZiGzgUaFnjy6afetK7HyZ4F4BGog2BRuioi67E3L5rEBP1Fzc68do2jNukIb%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24aEwvY3N5S0wvanVIaFJkQw%24NmYohpLyTc9cUSKbSgIhmvyXMeYRqSe52eqmxNVqYz4',
    'XSRF-TOKEN': 'eyJpdiI6IksxWk1MYnRIMGpuSlg0c2E1VGRiQWc9PSIsInZhbHVlIjoiOTY5OXJVK3U2eE5wUFM2QzM2T0ZSd0xMUEtFTzBWWGNIS20yZVlxVUIwYWdUZVJvTzJYbDg2WEpNUXljR1RUd1lzZ3gwWFhmVURkUWwxSWNzdDZnRXlBazNkU0V0QXgzL3NESC95SWtmMFlQQXVqc3BuMFI4dlRGU2hMc253OEgiLCJtYWMiOiIyNzM1ODA3MGY0NmVjNWFkYjY3Y2RjZTc4ODkwNTYxZmVlZTI4NzI4NjczYThiMTBlOTU1NWQxZTExOTM3MGFkIiwidGFnIjoiIn0%3D',
    'odl_session': 'upRKaZvmmpJViwLW7LW9WafJatmpt28a3a6Zn6cw',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'X-XSRF-TOKEN': 'eyJpdiI6IksxWk1MYnRIMGpuSlg0c2E1VGRiQWc9PSIsInZhbHVlIjoiOTY5OXJVK3U2eE5wUFM2QzM2T0ZSd0xMUEtFTzBWWGNIS20yZVlxVUIwYWdUZVJvTzJYbDg2WEpNUXljR1RUd1lzZ3gwWFhmVURkUWwxSWNzdDZnRXlBazNkU0V0QXgzL3NESC95SWtmMFlQQXVqc3BuMFI4dlRGU2hMc253OEgiLCJtYWMiOiIyNzM1ODA3MGY0NmVjNWFkYjY3Y2RjZTc4ODkwNTYxZmVlZTI4NzI4NjczYThiMTBlOTU1NWQxZTExOTM3MGFkIiwidGFnIjoiIn0=',
    'Origin': 'https://applydl.dotm.gov.np',
    'Connection': 'keep-alive',
    'Referer': 'https://applydl.dotm.gov.np/license/apply',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=776653%7CZiGzgUaFnjy6afetK7HyZ4F4BGog2BRuioi67E3L5rEBP1Fzc68do2jNukIb%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24aEwvY3N5S0wvanVIaFJkQw%24NmYohpLyTc9cUSKbSgIhmvyXMeYRqSe52eqmxNVqYz4; XSRF-TOKEN=eyJpdiI6IksxWk1MYnRIMGpuSlg0c2E1VGRiQWc9PSIsInZhbHVlIjoiOTY5OXJVK3U2eE5wUFM2QzM2T0ZSd0xMUEtFTzBWWGNIS20yZVlxVUIwYWdUZVJvTzJYbDg2WEpNUXljR1RUd1lzZ3gwWFhmVURkUWwxSWNzdDZnRXlBazNkU0V0QXgzL3NESC95SWtmMFlQQXVqc3BuMFI4dlRGU2hMc253OEgiLCJtYWMiOiIyNzM1ODA3MGY0NmVjNWFkYjY3Y2RjZTc4ODkwNTYxZmVlZTI4NzI4NjczYThiMTBlOTU1NWQxZTExOTM3MGFkIiwidGFnIjoiIn0%3D; odl_session=upRKaZvmmpJViwLW7LW9WafJatmpt28a3a6Zn6cw',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}


def run():
    categories = [1, 2, 3, 9]

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
        if cat == 9:
            cate = 'HEAVY'
        response = requests.post('https://applydl.dotm.gov.np/license/quota', cookies=cookies, headers=headers,
                                 json=json_data)
        data = json.loads(response.text)
        new = data['quotas']
        for every in data['quotas']:
            parsed = new[every]
            print(parsed['ad'] + cate + '  AVAILABLE  ' + str(parsed['available']))


def startt():
    Timer(30, startt).start()
    run()


startt()
