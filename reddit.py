#!/usr/bin/python

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
    msg = '\nError importing: ({}); terminating program\n\n'
    sys.stderr.write(msg.format(err))
    sys.exit(-1)


#########################################################

<<<<<<< HEAD

def read_tweets():
    for line in fileinput.input():
=======
def read_json():
    for line in open('Data.json','r'):
>>>>>>> upstream/master
        yield ujson.loads(line)


#########################################################


class Redpy:
    """
    TODO :: Class Description
    """
    def __init__(self):
        # Prepare class variables
        self.data = []
        self.client = requests.session()
        self.headers = {'user-agent': '/u/bradygp\'s Crawler', }

        # Read DATA.json file if present or create on if needed
        if os.path.isfile('DATA.json'):
            self.data = list(read_json())
        else:
            f = open('DATA.json', 'w')
            f.close()

    def login(self, username, password):
        """
        Input: reddit username, reddit password
        Output: session object
        """
        UP = {'user': username, 'passwd': password, 'api_type': 'json', }
        r = self.client.post('http://www.reddit.com/api/login', data=UP)
        j = json.loads(r.text)

        self.client.modhash = j['json']['data']['modhash']
        self.client.user = username
        return self.client

    def sub_reddit_info(self, lim, sr, sort='', return_json=False, **kwargs):
        """
        INPUT:  Max number of posts up to 100, subreddit, sort
                method(new,top,old,best,etc.), boolean specifying
                if returning json, additional arguments
        OUTPUT: Json file of all desired reddit posts
        """
        parameters = {'limit': limit, }
        parameters.update(kwargs)

        url = r'http://www.reddit.com/r/{sr}/{top}.json'
        url = url.format(sr=sr, top=sort)
        r = self.client.get(url, params=parameters)
        j = json.loads(r.text)

        if return_json:
            return j
        else:
            for story in j['data']['children']:
                self.data.append(story)
                print story


#########################################################


def main():
    obj = Redpy()
    obj.login(sys.argv[1], sys.argv[2])
    obj.sub_reddit_info(lim=10, sr='pokemon', sort='hot')
    #obj.sub_reddit_info(10, 'pokemon', 'hot')
    #pp2(j)

#########################################################

#########################################################
# Python Boilerplate


if __name__ == '__main__':
    main()


#########################################################
