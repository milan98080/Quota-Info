import requests

cookies = {
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '869111%7CSIlD7wOH5YNpUJQ25PN24y9F6KUHD1e6IDscJjb8EB42UwG5gGMf7BMdBZSt%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24OGQ0Z0hRMTdGNC52Sk5TUQ%24P%2BcUsvppt318xbw4aGQW2KZCGXUDNlOiCGNli%2FXpnYk',
    'XSRF-TOKEN': 'eyJpdiI6IkRJc0tEVVlBU0FWRzJreWY3aW5MNVE9PSIsInZhbHVlIjoiKzc3U3JQWFhMKzFmRU1iR1UwSFlhN3IzY1oycGxYeGlLK0lCdUpaOXNkbDBoK3l2TEgxTTJzbGVCeUtkc1NJWjl1T01nSm96YmYxaS9wd3FlVEFsSWVIdjZsQ2xGMS9OR3F6NDhkWVFZdER0K3NCZk1aNUlBNGc5eTZQQWh2cy8iLCJtYWMiOiI4NWJhNWIzODliZDRhYTY3NThhYzllY2NkMzY5M2EzNjE1NmE0ZGY4MGIzOTRmZjdjYzg4YWE1YmEyZjg4ZjBiIiwidGFnIjoiIn0%3D',
    'odl_session': 'kjgsDZtq06XWqOfJGvUvYGwMenGtT30DqYDEmEFy',
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
    'X-XSRF-TOKEN': 'eyJpdiI6IkRJc0tEVVlBU0FWRzJreWY3aW5MNVE9PSIsInZhbHVlIjoiKzc3U3JQWFhMKzFmRU1iR1UwSFlhN3IzY1oycGxYeGlLK0lCdUpaOXNkbDBoK3l2TEgxTTJzbGVCeUtkc1NJWjl1T01nSm96YmYxaS9wd3FlVEFsSWVIdjZsQ2xGMS9OR3F6NDhkWVFZdER0K3NCZk1aNUlBNGc5eTZQQWh2cy8iLCJtYWMiOiI4NWJhNWIzODliZDRhYTY3NThhYzllY2NkMzY5M2EzNjE1NmE0ZGY4MGIzOTRmZjdjYzg4YWE1YmEyZjg4ZjBiIiwidGFnIjoiIn0=',
    'Origin': 'https://applydl.dotm.gov.np',
    'Connection': 'keep-alive',
    'Referer': 'https://applydl.dotm.gov.np/change/password/verification',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=869111%7CSIlD7wOH5YNpUJQ25PN24y9F6KUHD1e6IDscJjb8EB42UwG5gGMf7BMdBZSt%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24OGQ0Z0hRMTdGNC52Sk5TUQ%24P%2BcUsvppt318xbw4aGQW2KZCGXUDNlOiCGNli%2FXpnYk; XSRF-TOKEN=eyJpdiI6IkRJc0tEVVlBU0FWRzJreWY3aW5MNVE9PSIsInZhbHVlIjoiKzc3U3JQWFhMKzFmRU1iR1UwSFlhN3IzY1oycGxYeGlLK0lCdUpaOXNkbDBoK3l2TEgxTTJzbGVCeUtkc1NJWjl1T01nSm96YmYxaS9wd3FlVEFsSWVIdjZsQ2xGMS9OR3F6NDhkWVFZdER0K3NCZk1aNUlBNGc5eTZQQWh2cy8iLCJtYWMiOiI4NWJhNWIzODliZDRhYTY3NThhYzllY2NkMzY5M2EzNjE1NmE0ZGY4MGIzOTRmZjdjYzg4YWE1YmEyZjg4ZjBiIiwidGFnIjoiIn0%3D; odl_session=kjgsDZtq06XWqOfJGvUvYGwMenGtT30DqYDEmEFy',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

json_data = {
    'password': 'Pokhara@123',
    'current_password': 'Pokhara@123',
    'password_confirmation': 'Pokhara@123',
    'otp': '000000',
    'verification': 'eyJpdiI6IkdGSGNRU2t0L29TUW4vNkNDT0NIR0E9PSIsInZhbHVlIjoib0s4NzNITmx5anMxUE54bS9vRnl1SUxnd0gza1hVWWFvSVhqMi9sQTc3TT0iLCJtYWMiOiIyNmU1YTIwMGY4ZTgyMzk5M2FhNTUwMGRiNzdlMDEzNTNjYTg2ZTk0YzBiMGE2MzE1NzQ4NTE1OTA3NWEzYWMxIiwidGFnIjoiIn0=',
}

response = requests.post('https://applydl.dotm.gov.np/change/password', cookies=cookies, headers=headers, json=json_data)
