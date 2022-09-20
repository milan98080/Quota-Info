import requests

cookies = {
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '869111%7COwnXsjEI4Nt02tXi2PoMPLFeIQu9NfWGaUe365jRtUMAgKxIRZDHqWVUwSdm%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24WTlGbnI0N1lZNkVHT0pQQg%24NL7W7OPIn2KLUx1Tuka541sMGgdxzEec7sx6Ff2LsEg',
    'odl_session': 'RaBiSR4ujfhv4NTVzO9O19FnyOwrsNaR67r4H5Te',
    'XSRF-TOKEN': 'eyJpdiI6IjBmWEpCMFJ1bERmdld4aFkxZDlRL1E9PSIsInZhbHVlIjoiOGRJdlhoVnhSNXZCZEQ3dEx6TWtEQnI3R2tEb0t2T2dUT2x6WjlYSUtMVUdRRDlFRlF3N0VKUEk1dU1udFNKL0xUUVZkRkx0UGZ0aVFyVHVzV3RFZStiVWVKYzdJREpoQVFqWmEwWGltd1RkUlFRUFdrcUgwdUR5VUtJVENvSngiLCJtYWMiOiIwZDQzN2Y5ZmM1ZTVlODk3ZDIzMzA0OTY0YWNhOTdiZjJlZmJmY2E3NmY1NzJmNWQ2M2Q1MGI5OWJiMTJjZDIxIiwidGFnIjoiIn0%3D',
}

headers = {
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=869111%7COwnXsjEI4Nt02tXi2PoMPLFeIQu9NfWGaUe365jRtUMAgKxIRZDHqWVUwSdm%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24WTlGbnI0N1lZNkVHT0pQQg%24NL7W7OPIn2KLUx1Tuka541sMGgdxzEec7sx6Ff2LsEg; odl_session=RaBiSR4ujfhv4NTVzO9O19FnyOwrsNaR67r4H5Te; XSRF-TOKEN=eyJpdiI6IjBmWEpCMFJ1bERmdld4aFkxZDlRL1E9PSIsInZhbHVlIjoiOGRJdlhoVnhSNXZCZEQ3dEx6TWtEQnI3R2tEb0t2T2dUT2x6WjlYSUtMVUdRRDlFRlF3N0VKUEk1dU1udFNKL0xUUVZkRkx0UGZ0aVFyVHVzV3RFZStiVWVKYzdJREpoQVFqWmEwWGltd1RkUlFRUFdrcUgwdUR5VUtJVENvSngiLCJtYWMiOiIwZDQzN2Y5ZmM1ZTVlODk3ZDIzMzA0OTY0YWNhOTdiZjJlZmJmY2E3NmY1NzJmNWQ2M2Q1MGI5OWJiMTJjZDIxIiwidGFnIjoiIn0%3D',
    'Origin': 'https://applydl.dotm.gov.np',
    'Referer': 'https://applydl.dotm.gov.np/change/password/verification',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-Inertia': 'true',
    'X-Inertia-Version': 'c7f6cd80bbaaa326d1c96774af7f4434',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'eyJpdiI6IjBmWEpCMFJ1bERmdld4aFkxZDlRL1E9PSIsInZhbHVlIjoiOGRJdlhoVnhSNXZCZEQ3dEx6TWtEQnI3R2tEb0t2T2dUT2x6WjlYSUtMVUdRRDlFRlF3N0VKUEk1dU1udFNKL0xUUVZkRkx0UGZ0aVFyVHVzV3RFZStiVWVKYzdJREpoQVFqWmEwWGltd1RkUlFRUFdrcUgwdUR5VUtJVENvSngiLCJtYWMiOiIwZDQzN2Y5ZmM1ZTVlODk3ZDIzMzA0OTY0YWNhOTdiZjJlZmJmY2E3NmY1NzJmNWQ2M2Q1MGI5OWJiMTJjZDIxIiwidGFnIjoiIn0=',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Chromium";v="106"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'password': 'Pokhara@123',
    'current_password': 'Pokhara@321',
    'password_confirmation': 'Pokhara@123',
    'otp': '536620',
    'verification': 'eyJpdiI6InRKZ29rTmtMOGEyK1p3SnNhZ0pQWWc9PSIsInZhbHVlIjoiSmMrSDZKYVc2dWwxMGludE1OTzRiZ1V3bWx5NjQ5WkcxMUE0R1dYbVFLYz0iLCJtYWMiOiI0MmQ2NGE2M2Q0ZDYzODIxZGExYmMwNzUxNmQ2YjcwZmZhYzY1NGQ5NjdlODE2MmE3YTBhN2U2OWMyNDFhMDRiIiwidGFnIjoiIn0=',
}

response = requests.post('https://applydl.dotm.gov.np/change/password', cookies=cookies, headers=headers, json=json_data)
print(response)
