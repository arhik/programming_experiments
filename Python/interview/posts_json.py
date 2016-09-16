import pprint
import json
import os
import math

path = 'posts.json' #Path of the posts.json file
preprocessed_path = 'post_posts.json'

class jsonReader:
    """Custom JSON Reader
    ///Over Kill
    """
    def __init__(self,path):
        self._path = path
        self._file = None
    
    def __enter__(self):
        try:
            self._file = open(self._path)
        except IOError as ioerror:
            print("File Not found")
        else:
            return self._file
        return None

    def __exit__(self, exc_t, exc_val, exc_tb):
        del self._file


def preprocess_json():
    with jsonReader(path) as f:
        if f is not None:
            a = json.load(f, 'utf-8')
            for i in a:
                if i.has_key(u'user'): # Preprocessing in case of missing keys like 'username', 'latitude'
                    continue
                else:
                    a.pop(a.index(i))
            return(a)
        return([])

def read_posts():
    return(preprocess_json())

def getFollowersCount(post):
    return post[u'user'][u'followers']

def geodesic_dist(a):
    return (math.acos(math.sin(math.radians(a[u'latitude']))*math.sin(math.radians(42.356680)) 
        + math.cos(math.radians(a[u'latitude']))*math.cos(math.radians(42.35668))*
        math.cos(math.radians(a[u'longitude']+71.060395))))

def run():
    posts = read_posts()
    if len(posts)==0:
        return

    # Finding the user details with highest number of followers"
    posts.sort(key=lambda x: -getFollowersCount(x))
    print("The user {0} with id {1} has highest number({2}) of followers"
            .format(posts[0][u'user'][u'username'], 
                posts[0][u'user'][u'id'],
                posts[0][u'user'][u'followers'])) 
    
    # Finding the user closer to the office
    posts.sort(key=lambda x: geodesic_dist(x[u'location']))
    print("The user closer to our office is {0} with id-{1} .".format(
        posts[0][u'user'][u'username'], posts[0][u'id']))

    
if __name__=='__main__':
    run()

