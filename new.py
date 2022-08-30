import requests
import json
from threading import Timer

cookies = {
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '700903%7Cux7XZ6fwluJnZP9ZavvL0LxxiViZJgYctJPaztKNaDqGd9KFUUPXZqz03zZ0%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24eVQ3cll0ZmkweE84MWNicA%24BeDPuvur0h50eRHSpvK4bH1xO%2BPGvUkZb5ahYBoUvKc',
    'odl_session': 'O7tiqVM22meXr9Mx4dWy3VRpfisjGJhBGgpYeEn7',
    'XSRF-TOKEN': 'eyJpdiI6Ik1JK3dhemR2WWgycWpLcDd5bG92cmc9PSIsInZhbHVlIjoienJXWGlCZHRuTDE0b1RwYTFWeGpveGdwVXdUMkt4amtxbXc3MkVHRklkRU5XY0JiMlU3YjE0WndjV2FHcDdrOUFEZzRKOWJna284VTVVYmRHWEkrMC9tNTU0aHFyNjY0VHpTZGpYTXl2WDhIMmR1OW9FRVZmUC9vTGlsUlRRaC8iLCJtYWMiOiI3MDc2M2MxYmNmY2M2YTA5YmNmOGJiMzBjMTg5YWM4NmNkOWMwYzkzMDU1MzBkZmQyMjY0NGQxMGNlZmY5MDU3IiwidGFnIjoiIn0%3D',
}

headers = {
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=700903%7Cux7XZ6fwluJnZP9ZavvL0LxxiViZJgYctJPaztKNaDqGd9KFUUPXZqz03zZ0%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24eVQ3cll0ZmkweE84MWNicA%24BeDPuvur0h50eRHSpvK4bH1xO%2BPGvUkZb5ahYBoUvKc; odl_session=O7tiqVM22meXr9Mx4dWy3VRpfisjGJhBGgpYeEn7; XSRF-TOKEN=eyJpdiI6Ik1JK3dhemR2WWgycWpLcDd5bG92cmc9PSIsInZhbHVlIjoienJXWGlCZHRuTDE0b1RwYTFWeGpveGdwVXdUMkt4amtxbXc3MkVHRklkRU5XY0JiMlU3YjE0WndjV2FHcDdrOUFEZzRKOWJna284VTVVYmRHWEkrMC9tNTU0aHFyNjY0VHpTZGpYTXl2WDhIMmR1OW9FRVZmUC9vTGlsUlRRaC8iLCJtYWMiOiI3MDc2M2MxYmNmY2M2YTA5YmNmOGJiMzBjMTg5YWM4NmNkOWMwYzkzMDU1MzBkZmQyMjY0NGQxMGNlZmY5MDU3IiwidGFnIjoiIn0%3D',
    'Referer': 'https://applydl.dotm.gov.np',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-Inertia': 'true',
    'X-Inertia-Version': '26f5d68a49eb03710177f0ba3873ab38',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'eyJpdiI6Ik1JK3dhemR2WWgycWpLcDd5bG92cmc9PSIsInZhbHVlIjoienJXWGlCZHRuTDE0b1RwYTFWeGpveGdwVXdUMkt4amtxbXc3MkVHRklkRU5XY0JiMlU3YjE0WndjV2FHcDdrOUFEZzRKOWJna284VTVVYmRHWEkrMC9tNTU0aHFyNjY0VHpTZGpYTXl2WDhIMmR1OW9FRVZmUC9vTGlsUlRRaC8iLCJtYWMiOiI3MDc2M2MxYmNmY2M2YTA5YmNmOGJiMzBjMTg5YWM4NmNkOWMwYzkzMDU1MzBkZmQyMjY0NGQxMGNlZmY5MDU3IiwidGFnIjoiIn0=',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Chromium";v="106"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def run():
        response = requests.post('https://applydl.dotm.gov.np/license/apply', cookies=cookies, headers=headers)
        x = response.ststus_code
        if x == 200:
            print('running')
        else:
            print('not running')


def startt():
    Timer(120, startt).start()
    run()


startt()
