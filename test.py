import requests
import json
import unicodedata
from pprint import pprint

def subredditInfo(client, limit=25, sr='pokemon', sorting='', return_json=False, **kwargs):
    parameters = {'limit':limit,}
    parameters.update(kwargs)
    url = r'http://www.reddit.com/r/{sr}/{top}.json'.format(sr=sr, top=sorting)
    j = json.loads(r.text)
    if return_json:
        return j
    else:
        stories = []
        for key in j:
            print key, j[key]
        for story in j['data']['children']:
            stories.append(story)
        return stories




username = 'bradygp'
password = 'treeoflife'
user_pass_dict = {'user' : username, 'passwd' : password, 'api_type':'json',}
headers = {'user-agent' : '/u/bradyp test API bot', }
client = requests.session()
r = client.post(r'http://www.reddit.com/api/login', data=user_pass_dict)
j = json.loads(r.text)

client.modhash = j['json']['data']['modhash']

me = json.loads(client.get(r'http://www.reddit.com/api/me.json').text)
for elem in me['data']:
    key = unicodedata.normalize('NFKD', elem).encode('ascii','ignore')
    print key, me['data'][key]

stories = subredditInfo(client)

for entry in stories:
    print entry
