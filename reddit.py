# http://blog.tankorsmash.com/?p=378
import sys

try:
    import json
    import requests
    from pprint import pprint as pp2
except ImportError:
    print 'Error importing a dependancy, terminating program'
    sys.exit(-1)

class Redpy:
    def __init__(self):
        headers = {'user-agent': '/u/bradygp\'s Crawler', }
        self.client = requests.session()

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
 
    def subredditInfo(self, limit, sr, sorting='', return_json=True, **kwargs):
        """
        INPUT: max number of posts up to 100, subreddit, sorting method(new,top,old,best,etc.), boolean specifying if returning json, additional arguments
        OUTPUT: json file of all desired reddit posts
        """
        """retrieves X (max 100) amount of stories in a subreddit\n
        'sorting' is whether or not the sorting of the reddit should be customized or not,
        if it is: Allowed passing params/queries such as t=hour, week, month, year or all"""
 
        parameters = {'limit': limit,}
        parameters.update(kwargs)
 
        url = r'http://www.reddit.com/r/{sr}/{top}.json'.format(sr=sr, top=sorting)
        r = self.client.get(url,params=parameters)
        j = json.loads(r.text)
 
        if return_json:
            return j
        else:
            stories = []
            for story in j['data']['children']:
                stories.append(story) 
            return stories

obj = Redpy() 
obj.login('bradygp', 'treeoflife')
 
j = obj.subredditInfo(sys.argv[1], 'netsec', 'hot')
 
pp2(j)
