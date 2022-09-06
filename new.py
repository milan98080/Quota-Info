import requests

cookies = {
    'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d': '862186%7Cm5OJHdNZeknnaFFivrejU5WGeOmewZvR3jo1S9PMWRIdfJ40LX3Gwuv4MXxs%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24dzE2Zm80b1lYYTQ0bDdIOA%24CDm8DJxmYTsyn1IB9eHdIPArpmhLwCUXwpnu4zW7DoY',
    'XSRF-TOKEN': 'eyJpdiI6IkVlN3lQUTBQUkZjQmh3NUZ6N2taZVE9PSIsInZhbHVlIjoiS1N3ZzRVL016QW1NL0h5dyt0eUc1SmRabmIzOC9WekltMWtBY0RNNlpxdVV6VDVleFJ5MWJid29IWFlnT0p6cmwrYjArLzIvSVBHWisxeEpUQU5TRXpqb25kZ1JmS001eTcybitwcWIyMUJ0ZHFlSktPM3g0WFVJcWcrQy9xcFQiLCJtYWMiOiI3MjliODI0OTAyNGE2ZGM1YmMzYTI0NTZkNzQ3ODUwMGE5YzVhMWY0MWJmYWIyZjJkNDRjYjQwYThhNjQ4YzliIiwidGFnIjoiIn0%3D',
    'odl_session': 'CCrZ8wkKPtb6hC2S6Ha5F1SVn3e8pTCPBDVqUcw7',
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
    'X-Inertia-Version': '16361033bc8dabc69ba761dce03df65e',
    'X-XSRF-TOKEN': 'eyJpdiI6IkVlN3lQUTBQUkZjQmh3NUZ6N2taZVE9PSIsInZhbHVlIjoiS1N3ZzRVL016QW1NL0h5dyt0eUc1SmRabmIzOC9WekltMWtBY0RNNlpxdVV6VDVleFJ5MWJid29IWFlnT0p6cmwrYjArLzIvSVBHWisxeEpUQU5TRXpqb25kZ1JmS001eTcybitwcWIyMUJ0ZHFlSktPM3g0WFVJcWcrQy9xcFQiLCJtYWMiOiI3MjliODI0OTAyNGE2ZGM1YmMzYTI0NTZkNzQ3ODUwMGE5YzVhMWY0MWJmYWIyZjJkNDRjYjQwYThhNjQ4YzliIiwidGFnIjoiIn0=',
    'Origin': 'https://applydl.dotm.gov.np',
    'Connection': 'keep-alive',
    'Referer': 'https://applydl.dotm.gov.np/license/apply/verification',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'remember_applicants_59ba36addc2b2f9401580f014c7f58ea4e30989d=862186%7Cm5OJHdNZeknnaFFivrejU5WGeOmewZvR3jo1S9PMWRIdfJ40LX3Gwuv4MXxs%7C%24argon2id%24v%3D19%24m%3D65536%2Ct%3D4%2Cp%3D1%24dzE2Zm80b1lYYTQ0bDdIOA%24CDm8DJxmYTsyn1IB9eHdIPArpmhLwCUXwpnu4zW7DoY; XSRF-TOKEN=eyJpdiI6IkVlN3lQUTBQUkZjQmh3NUZ6N2taZVE9PSIsInZhbHVlIjoiS1N3ZzRVL016QW1NL0h5dyt0eUc1SmRabmIzOC9WekltMWtBY0RNNlpxdVV6VDVleFJ5MWJid29IWFlnT0p6cmwrYjArLzIvSVBHWisxeEpUQU5TRXpqb25kZ1JmS001eTcybitwcWIyMUJ0ZHFlSktPM3g0WFVJcWcrQy9xcFQiLCJtYWMiOiI3MjliODI0OTAyNGE2ZGM1YmMzYTI0NTZkNzQ3ODUwMGE5YzVhMWY0MWJmYWIyZjJkNDRjYjQwYThhNjQ4YzliIiwidGFnIjoiIn0%3D; odl_session=CCrZ8wkKPtb6hC2S6Ha5F1SVn3e8pTCPBDVqUcw7',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

json_data = {
    'category_id': 1,
    'province_id': 4,
    'office_id': 19,
    'visit_date_bs': '2079-05-26',
    'visit_date_ad': '2022-09-11',
    'is_urgent': False,
    'urgency_reason_id': '',
    'documents': {},
    'disclaimer': True,
    'otp': '000000',
    'verification': 'eyJpdiI6IjBUeWZZUzMxOXdLV21UQUJwVUpBYlE9PSIsInZhbHVlIjoiVjhqbXpreFFRei9nMXNCcnBjYlFvT3ByYTg2cTBoN3ladHJFdWdBQjhjND0iLCJtYWMiOiI2NWIxZDMzNTE0NWY4NjQyNmQwNDE1ZDU0MzlhZDA3ZjE5NWUzNzg3M2UxNDllN2U2ZGE2MTM4ZDQ4YTc3YzM4IiwidGFnIjoiIn0=',
}

response = requests.post('https://applydl.dotm.gov.np/license/apply', cookies=cookies, headers=headers, json=json_data)
print(response)
