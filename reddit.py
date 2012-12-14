# http://blog.tankorsmash.com/?p=378
import sys

#########################################################

try:
    import json
    import ujson
    import requests
    import os.path
    import fileinput
    from pprint import pprint as pp2
except ImportError as err:
    sys.stderr.write('Error importing dependency ({}), terminating program'.format(err))
    sys.exit(-1)

#########################################################

def read_tweets():
    for line in fileinput.input():
        yield ujson.loads(line)

#########################################################

class Redpy:
    def __init__(self):
        headers = {'user-agent': '/u/bradygp\'s Crawler', }
        self.client = requests.session()
        self.data = []

        if os.path.isfile('DATA.json'):
            self.data = list(read_tweets())
        else:
            f = open('DATA.json','w')
            f.close()

    def login(self, username, password):
        """
        Input: reddit username, reddit password
        Output: session object
        """

        UP = {'user': username, 'passwd': password, 'api_type': 'json',}

        r = self.client.post('http://www.reddit.com/api/login', data=UP)
        j = json.loads(r.text)

        self.client.modhash = j['json']['data']['modhash']
        self.client.user = username
        return self.client

    def subredditInfo(self, limit, sr, sorting='', return_json=False, **kwargs):
        """
        INPUT: max number of posts up to 100, subreddit, sorting method(new,top,old,best,etc.), boolean specifying if returning json, additional arguments
        OUTPUT: json file of all desired reddit posts
        """
        parameters = {'limit': limit,}
        parameters.update(kwargs)

        url = r'http://www.reddit.com/r/{sr}/{top}.json'.format(sr=sr, top=sorting)
        r = self.client.get(url,params=parameters)
        j = json.loads(r.text)
        if return_json:
            return j
        else:
            for story in j['data']['children']:
                self.data.append(story)

#########################################################

obj = Redpy()
obj.login(sys.argv[2], sys.argv[3])
obj.subredditInfo(10, 'pokemon', 'hot')

#########################################################

#pp2(j)
