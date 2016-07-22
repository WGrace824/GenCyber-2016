# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 12:48:12 2016

@author: student
"""
'''

import base64
encoded = base64.b64encoder(b'lkeflk')
'''
import binascii
#define starting string
h = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
hex = h.decode("hex")
base = binascii.b2a_base64(hex)
print(base)