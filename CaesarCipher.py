# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 09:38:56 2016

@author: student

Caesar Cipher

1. Name your function with 2 parameters, a str and a int
2. 
"""



def Caesar_Cipher(Message, shift):
    Cipher = ""
    for char in Message:
        if ord(char) > 64 and ord(char) < 91:
            if ord(char) + shift < 91:
                char = chr(ord(char) + shift)
            else:
               char = chr(ord(char) - (26 - shift))
        elif ord(char) > 96 and ord(char) < 123 :
            if (ord(char) + shift) < 123:
                char = chr(ord(char) + shift)
            else:
               char = chr(ord(char) - (26 - shift))
                
        else:
            char = " "
        Cipher += char
    print(Cipher)

Caesar_Cipher("Pokemon Go", 14)



def Caesar_Decrypt(Code):
    for i in range(26): 
        Decrypt = ""
        for char in Code:
            asc = ord(char)
            if asc > 64 and asc < 91:
                asc-=i
                if asc < 65:
                    asc+=26
                Decrypt +=chr(asc)
            elif ord(char) > 96 and ord(char) < 123 :
                asc -= i
                if asc < 97:
                     asc+=26
                Decrypt += chr(asc)
            else:
                Decrypt += char
        print(i, Decrypt)
    return(i)

Caesar_Decrypt("Dcysacb Uc")