# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 09:59:58 2016

@author: student
Grace Wang
GenCyber 2016
7/7/16
Loops
"""
#While loop
'''
import random 
myint = 465

while myint > 400:
   myint = myint - 5
   print(myint)

guess = int(input("Guess my number: "))
number = random.randint(0,100)

while number != guess :
    if (number > guess):
        print("Not quite, this number is too small")
    else:
        print("Well, this number is too big")
    guess = int(input("Guess again: "))
    
print("Woo!! Your number was correct")
'''
'''
password = input("Whats my password? (Hint: It's 4 letters and in all caps) ")
my_password = "BKHY"
while password != my_password:
    print("Haha fooled ya! You'll never get me!")
    password = input("Try again: ")
print ("Darn! You got me!")
'''
'''
#For loop
#i is a variable that exists inside my for loop
for i in range(20, 2, -5):
    print(str(i)+"2")
 '''
'''  
string = "Do you wanna be my lover"
for char in string: # char goes through each character ie letter in a string
    if char == "D":
        print(char + "o")
    elif char == "b":
        print(char + "e")
    elif char == "m":
        print(char + "y")
    elif char == "l":
        print(char + "over")
    elif char == "w"
        print (char + "anna")
    else:
        print(char)
'''
'''
def ascii_to_eight_bit(letter):
    num = ord(letter)
    bitstring=""
    for i in range(8):
        print(num)
        if num%2 == 0:
            bitstring = '0' + bitstring
            print('0')
        else:
            bitstring = '1' + bitstring
            print('1')
        num = num //2
    return bitstring
'''

'''
def valid_password(password):
    hasUpper = False
    hasLower = False
    if len(password) >= 6 :
        for char in password:
            if ord(char) < 91 and ord(char) > 64 :
                hasUpper = True
            elif ord(char) < 123 and ord(char) > 96 :
                hasLower = True
            else:
                return False
        if hasUpper== True and hasLower == True:
            return True
    else:
        return False
        
print(valid_password("iuhl"))
'''

import smtplib
to = '8482194611@tmomail.net'

gmail_user = "goannabananassavana@gmail.com"
gmail_pwd = "U7CWbg4wJkrmXB"

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user,gmail_pwd)

header = 'To:' + to + '\n' + 'From' + gmail_user + '\n' + 'Subject: Yo  \n'
print(header)
msg = header + '\n The mafia is coming after you \n\n'
smtpserver.sendmail(gmail_user, to, msg)
print('done!')
smtpserver.close()

