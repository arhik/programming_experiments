#!/usr/bin/env python2

# Copyright (C) 2016  <arhik@groundsignal.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pprint
import json
import os
import math

path = 'posts.json' #Path of the posts.json file
preprocessed_path = 'post_posts.json'

class jsonReader:
    """
    Custom JSON Reader Context Manager
    Gracefully exits and prompts the error on the console.
    
    @param path: path to the json file
    @returns _file: file object
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


def preprocess_json(mandatory_keys=None):
    """
    Preprocess json file

    @param mandatory_keys: keys which should present in the json.
    @returns list object of parsed json file
    """
    with jsonReader(path) as f:
        if f is not None:
            a = json.load(f, 'utf-8')
            for i in a:
                for k in mandatory_keys:
                    if i.has_key(k): # Preprocessing in case of missing keys like 'username', 'latitude'
                        continue
                    else:
                        a.pop(a.index(i))
            return(a)
        return([])

def read_posts(keys=None):
    """
    Read the posts
    
    @returns list object of posts
    """
    return(preprocess_json(mandatory_keys=keys))

def getFollowersCount(post):
    """
    Utility function to get the followers count of a user

    @returns int object
    """
    return post[u'user'][u'followers']

def geodesic_dist(a):
    """
    Computes the radial distance of the user from office using location information

    @param a : dictionary of latitude and longitude
    @returns float : distance of user from office
    """
    return (math.acos(math.sin(math.radians(a[u'latitude']))*math.sin(math.radians(42.356680)) 
        + math.cos(math.radians(a[u'latitude']))*math.cos(math.radians(42.35668))*
        math.cos(math.radians(a[u'longitude']+71.060395))))

def run():
    """
    Function to find the user closest to the office

    @returns dict - user information
    """
    posts = read_posts(keys=[u'user',u'location'])
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
    return posts[0][u'user']
    
if __name__=='__main__':
    run()

