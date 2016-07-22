# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 09:37:51 2016

@author: student
"""

import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
print(md5("facebook_is_lame.jpg"))
print(md5("wishing_to_shave.jpg"))

print(md5("ocean_breeze.jpg"))
print(md5("whitest_shirt_ever.jpg"))

print(md5("myspace_profile_pic.jpg"))
print(md5("throwback.jpg"))

print(md5("my_speech.jpg"))
print(md5("looking_fresh.jpg"))