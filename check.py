from ratelimit import limits
import requests
import json

'''Your GoDaddy API Key. It's free with a Godaddy account. You get 60 requests/minute.'''
f = open('keys.json')
KEYS = json.load(f)
API_KEY = KEYS['key']
SECRET = KEYS['secret']

'''Setting our period for ratelimiting calls to the Godaddy API'''
ONE_MINUTE = 60
CALLS = 60

testlist = ['google.com', 'fitz.city', 'financewriter12.io', 'microsoft.com', 'ny.city', 'sdaofsdsdf.io']

'''We use the @limits decorator from the --ratelimit-- package to rate limit our calls to the API.
The --calls-- argument is the max number of calls per --period--'''
@limits(calls=CALLS, period=ONE_MINUTE)
def checker(domains):
    avail = []
    for x in domains:
        headers = {'Authorization': f'sso-key {API_KEY}:{SECRET}'}
        url = f'https://api.godaddy.com/v1/domains/available?domain={x}&checkType=FAST&forTransfer=false'
        resp = requests.get(url, headers=headers)
        data = resp.json()
        if data['available']:
            avail.append(x)
        print(data)
    return avail

print(checker(testlist))