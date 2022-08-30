import requests
import json
from threading import Timer

cookies = {
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '744619%7CmRNCABneb9FAFKF23CNiStLaRPrtj5XxxFIiTptQ0llSO33mQuh7FBHarDOB%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24VE5vL0k5dS5vV21SeTJhTw%24TKLwj8rrdnv2lqJZuiLFx%2FbJXPtt3TCfyL62kAELId8',
    'XSRF-TOKEN': 'eyJpdiI6IkRRYjFrNzZvaktsZURpTWtoRGlMVFE9PSIsInZhbHVlIjoiQnAvVGxlTDVvZVhXTjhnbDZkdlV2T2pHbmZ4MkhTMENWMVBpQzBsSmkrZ0xUbDRxdCt5RFhqYWN2R1Q0UXJ1N3YyMkNzLzlUSWNkVlJRd1k1cGlmaXEySG1JQllYeVpoWTBma3RBMVBwdDkxWkVFZFVkdnk1R0s5S2xTeGNleDgiLCJtYWMiOiI4ZGMxYTgwOTY3NzQzOWRkYmE1ZmU2YzE3MzU3ZDUyMDA4ODE1NjBhMGYyYTY4OGQyYjFiOTJkMDc4NTE3N2Y2IiwidGFnIjoiIn0%3D',
    'odl_session': 'P1rq4HQMFpQfeank06laeQJKnfrKSnqj0KvlVWsO',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Inertia': 'true',
    'X-Inertia-Version': '26f5d68a49eb03710177f0ba3873ab38',
    'Content-Type': 'application/json',
    'X-XSRF-TOKEN': 'eyJpdiI6IkRRYjFrNzZvaktsZURpTWtoRGlMVFE9PSIsInZhbHVlIjoiQnAvVGxlTDVvZVhXTjhnbDZkdlV2T2pHbmZ4MkhTMENWMVBpQzBsSmkrZ0xUbDRxdCt5RFhqYWN2R1Q0UXJ1N3YyMkNzLzlUSWNkVlJRd1k1cGlmaXEySG1JQllYeVpoWTBma3RBMVBwdDkxWkVFZFVkdnk1R0s5S2xTeGNleDgiLCJtYWMiOiI4ZGMxYTgwOTY3NzQzOWRkYmE1ZmU2YzE3MzU3ZDUyMDA4ODE1NjBhMGYyYTY4OGQyYjFiOTJkMDc4NTE3N2Y2IiwidGFnIjoiIn0=',
    'Connection': 'keep-alive',
    'Referer': 'https://applydl.dotm.gov.np/',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=744619%7CmRNCABneb9FAFKF23CNiStLaRPrtj5XxxFIiTptQ0llSO33mQuh7FBHarDOB%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24VE5vL0k5dS5vV21SeTJhTw%24TKLwj8rrdnv2lqJZuiLFx%2FbJXPtt3TCfyL62kAELId8; XSRF-TOKEN=eyJpdiI6IkRRYjFrNzZvaktsZURpTWtoRGlMVFE9PSIsInZhbHVlIjoiQnAvVGxlTDVvZVhXTjhnbDZkdlV2T2pHbmZ4MkhTMENWMVBpQzBsSmkrZ0xUbDRxdCt5RFhqYWN2R1Q0UXJ1N3YyMkNzLzlUSWNkVlJRd1k1cGlmaXEySG1JQllYeVpoWTBma3RBMVBwdDkxWkVFZFVkdnk1R0s5S2xTeGNleDgiLCJtYWMiOiI4ZGMxYTgwOTY3NzQzOWRkYmE1ZmU2YzE3MzU3ZDUyMDA4ODE1NjBhMGYyYTY4OGQyYjFiOTJkMDc4NTE3N2Y2IiwidGFnIjoiIn0%3D; odl_session=P1rq4HQMFpQfeank06laeQJKnfrKSnqj0KvlVWsO',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}



def run():
        response = requests.get('https://applydl.dotm.gov.np/license/category', cookies=cookies, headers=headers)
        x = response.status_code
        while x!= 200:
            print('not running')
        if x == 200:
            print('running')
            run();


run()
