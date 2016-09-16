import pprint
import json
import os
import math

path = 'posts.json' #Path of the posts.json file

def read_posts():
    with open(path) as f:
        return(json.load(f, 'utf-8'))

def getFollowersCount(post):
    return post[u'user'][u'followers']

def geodesic_dist(a):
    return (math.acos(math.sin(math.radians(a[u'latitude']))*math.sin(math.radians(42.356680)) 
        + math.cos(math.radians(a[u'latitude']))*math.cos(math.radians(42.35668))*
        math.cos(math.radians(a[u'longitude']+71.060395))))

def run():
    posts = read_posts()

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

