import requests

cookies = {
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '869111%7CsdSsoXvNAwnDPae2PGYRyAKcePrUuBUoUehLQdn0bOcpNme6AnNMyUbjdDP1%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24OGQ0Z0hRMTdGNC52Sk5TUQ%24P%2BcUsvppt318xbw4aGQW2KZCGXUDNlOiCGNli%2FXpnYk',
    'XSRF-TOKEN': 'eyJpdiI6Ik9Wd1pKSkZ3Rmd5ZE1haEkxTDBkUmc9PSIsInZhbHVlIjoiWFY4WVZRSzR3WDlZTnV6ZHU1R0ZhUk8yZ0NQQm5FRlJWTGs1czlpakFGSThhbnl4ZlVsU21aaUJ1Mi9DeEVVWXpoc3JKdmU0ZnZQUXRvenhWNXpqMEJwRkF5LzNEME05SHBtbllNbkJ1VUZUMUtSdk9tNDN2ZnB1blAvb2UxY3YiLCJtYWMiOiI5YjI0YTY3YTZkMWI4OTExYjhlNmIxNjY1NmRmYTBiMzIxMjlhODRhMTM3MDk5MWU4OWEyY2ExYTQzNTU2YTFmIiwidGFnIjoiIn0%3D',
    'odl_session': 'wQMVlrgsOWk8ENjsxxxoKKCfuQCi6j39QZrcaiFq',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Inertia': 'true',
    'X-Inertia-Version': 'c7f6cd80bbaaa326d1c96774af7f4434',
    'X-XSRF-TOKEN': 'eyJpdiI6Ik9Wd1pKSkZ3Rmd5ZE1haEkxTDBkUmc9PSIsInZhbHVlIjoiWFY4WVZRSzR3WDlZTnV6ZHU1R0ZhUk8yZ0NQQm5FRlJWTGs1czlpakFGSThhbnl4ZlVsU21aaUJ1Mi9DeEVVWXpoc3JKdmU0ZnZQUXRvenhWNXpqMEJwRkF5LzNEME05SHBtbllNbkJ1VUZUMUtSdk9tNDN2ZnB1blAvb2UxY3YiLCJtYWMiOiI5YjI0YTY3YTZkMWI4OTExYjhlNmIxNjY1NmRmYTBiMzIxMjlhODRhMTM3MDk5MWU4OWEyY2ExYTQzNTU2YTFmIiwidGFnIjoiIn0=',
    'Origin': 'https://applydl.dotm.gov.np',
    'Connection': 'keep-alive',
    'Referer': 'https://applydl.dotm.gov.np/change/password/verification',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=869111%7CsdSsoXvNAwnDPae2PGYRyAKcePrUuBUoUehLQdn0bOcpNme6AnNMyUbjdDP1%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24OGQ0Z0hRMTdGNC52Sk5TUQ%24P%2BcUsvppt318xbw4aGQW2KZCGXUDNlOiCGNli%2FXpnYk; XSRF-TOKEN=eyJpdiI6Ik9Wd1pKSkZ3Rmd5ZE1haEkxTDBkUmc9PSIsInZhbHVlIjoiWFY4WVZRSzR3WDlZTnV6ZHU1R0ZhUk8yZ0NQQm5FRlJWTGs1czlpakFGSThhbnl4ZlVsU21aaUJ1Mi9DeEVVWXpoc3JKdmU0ZnZQUXRvenhWNXpqMEJwRkF5LzNEME05SHBtbllNbkJ1VUZUMUtSdk9tNDN2ZnB1blAvb2UxY3YiLCJtYWMiOiI5YjI0YTY3YTZkMWI4OTExYjhlNmIxNjY1NmRmYTBiMzIxMjlhODRhMTM3MDk5MWU4OWEyY2ExYTQzNTU2YTFmIiwidGFnIjoiIn0%3D; odl_session=wQMVlrgsOWk8ENjsxxxoKKCfuQCi6j39QZrcaiFq',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

json_data = {
    'password': 'Pokhara@123',
    'current_password': 'Pokhara@1234',
    'password_confirmation': 'Pokhara@123',
    'otp': '759891',
    'verification': 'eyJpdiI6Ik9XdWdIYnRyemxUWnVTbzRPd2NjSmc9PSIsInZhbHVlIjoiQTVxb3NYcHBWakJ4aXdwQk5HYXF0d1RINHA0bHIvOWZpOXN4N1d1SlZBQT0iLCJtYWMiOiIwYWFjNDM4ZDM0ZGViOWE2MDM5YmUyOWUzMmNlOWMyN2FiZWE5YmRiOWUxM2U1MTc2ZDNjODcxZDcxZGE5MmMzIiwidGFnIjoiIn0=',
}

response = requests.post('https://applydl.dotm.gov.np/change/password', cookies=cookies, headers=headers, json=json_data)
print(response)
