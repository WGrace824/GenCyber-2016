# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 11:15:01 2016

@author: student
"""

import qrcode
img = qrcode.make('Teacup pig with a top hat')
img.show()
img.save('Piggy.png')

import qrtools
qr = qrtools.QR()
qr.decode("Piggy.png")
print(qr.data)