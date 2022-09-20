import requests

cookies = {
    'odl_session': 'eEbUakH1QeWiqwBsitE8SQzhYdvqYVmb8MGkN1xc',
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '869111%7COwnXsjEI4Nt02tXi2PoMPLFeIQu9NfWGaUe365jRtUMAgKxIRZDHqWVUwSdm%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24WTlGbnI0N1lZNkVHT0pQQg%24NL7W7OPIn2KLUx1Tuka541sMGgdxzEec7sx6Ff2LsEg',
    'XSRF-TOKEN': 'eyJpdiI6IncrR0M1UHY0aXh5VzdLSkovT2JsRmc9PSIsInZhbHVlIjoiVklmMUFVZHdDYmpWYVdGWVRQVFU3Z0dZYXdVQ0FBU2VKQ2VJbW93TFVIWXdEdnhJNWVra2VMTDJwWHFieEJJV3lTVlJFYnd6L1h0L1Ixb1kyQWxQeThCdk1WQytTK01kdUNKQm5VeFQ2aEhHRzdEM3RxMkMvcUtoaThUd1lXZWwiLCJtYWMiOiI3MjU5MDM4ZmYyZjJlZjFkYTk4ZTJhYmUwNzY3MWJiNjExMTE1YTJmZTc3NTI3MWJlMGNmODY3YzgxMmFmNzgyIiwidGFnIjoiIn0%3D',
}

headers = {
    'Accept': 'text/html, application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'odl_session=eEbUakH1QeWiqwBsitE8SQzhYdvqYVmb8MGkN1xc; remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=869111%7COwnXsjEI4Nt02tXi2PoMPLFeIQu9NfWGaUe365jRtUMAgKxIRZDHqWVUwSdm%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24WTlGbnI0N1lZNkVHT0pQQg%24NL7W7OPIn2KLUx1Tuka541sMGgdxzEec7sx6Ff2LsEg; XSRF-TOKEN=eyJpdiI6IncrR0M1UHY0aXh5VzdLSkovT2JsRmc9PSIsInZhbHVlIjoiVklmMUFVZHdDYmpWYVdGWVRQVFU3Z0dZYXdVQ0FBU2VKQ2VJbW93TFVIWXdEdnhJNWVra2VMTDJwWHFieEJJV3lTVlJFYnd6L1h0L1Ixb1kyQWxQeThCdk1WQytTK01kdUNKQm5VeFQ2aEhHRzdEM3RxMkMvcUtoaThUd1lXZWwiLCJtYWMiOiI3MjU5MDM4ZmYyZjJlZjFkYTk4ZTJhYmUwNzY3MWJiNjExMTE1YTJmZTc3NTI3MWJlMGNmODY3YzgxMmFmNzgyIiwidGFnIjoiIn0%3D',
    'Origin': 'https://applydl.dotm.gov.np',
    'Referer': 'https://applydl.dotm.gov.np/change/password/verification',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-Inertia': 'true',
    'X-Inertia-Version': 'c7f6cd80bbaaa326d1c96774af7f4434',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'eyJpdiI6IncrR0M1UHY0aXh5VzdLSkovT2JsRmc9PSIsInZhbHVlIjoiVklmMUFVZHdDYmpWYVdGWVRQVFU3Z0dZYXdVQ0FBU2VKQ2VJbW93TFVIWXdEdnhJNWVra2VMTDJwWHFieEJJV3lTVlJFYnd6L1h0L1Ixb1kyQWxQeThCdk1WQytTK01kdUNKQm5VeFQ2aEhHRzdEM3RxMkMvcUtoaThUd1lXZWwiLCJtYWMiOiI3MjU5MDM4ZmYyZjJlZjFkYTk4ZTJhYmUwNzY3MWJiNjExMTE1YTJmZTc3NTI3MWJlMGNmODY3YzgxMmFmNzgyIiwidGFnIjoiIn0=',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Chromium";v="106"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'password': 'Pokhara@321',
    'current_password': 'Pokhara@123',
    'password_confirmation': 'Pokhara@321',
    'otp': '290865',
    'verification': 'eyJpdiI6ImVaeEFESmdaV0lpRCt5Y2QvVHptVXc9PSIsInZhbHVlIjoiWnVVSmpUejF5Y3NKaC9NMk5yTTRRZ2w1Y0lHR3g3SEtXMEhjOXhNcUtIUT0iLCJtYWMiOiIwNzAwYWU2NzdhZWMyMTQ2YmY1MzQ0ZWJiNmZkNDJjNTdlMjdkNzNiNTE2YzQ4MDU4ODE4ZDIwZTY0OTk1OGUzIiwidGFnIjoiIn0=',
}

response = requests.post('https://applydl.dotm.gov.np/change/password', cookies=cookies, headers=headers, json=json_data)
print(response)
