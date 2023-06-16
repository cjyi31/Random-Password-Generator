# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 08:03:16 2023

@author: Grace.Choo
"""
"""
To generate random passwords. Expected outputs are:
    1. X characters in length. Assign how long you want your password to be in 'HowLongPW' Setting
    2. At least 1 Big Case Character
    3. At least 1 Lower case Character
    4. At least 1 Digit
    5. At least 1 Special Character

"""

"""
0. Settings
"""
HowLongPW = 15


"""
1. Packages
"""
import random as rd

BigAlpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SmallAlpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SpecialChar = ['~', '!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '+', '=']

CharacterList = ['BigAlpha','SmallAlpha','Digits','SpecialChar']


grouplist=[]
while len(dict.fromkeys(grouplist)) != 4:
    pw = []
    for i in range(HowLongPW):
        group = rd.choice(CharacterList)
        if group == 'BigAlpha':
            p = rd.choice(BigAlpha)
        elif group == 'SmallAlpha':
            p = rd.choice(SmallAlpha)
        elif group == 'Digits':
            p = rd.choice(Digits)
        else:
            p = rd.choice(SpecialChar)
        pw.append(p)
        grouplist.append(group)
    print("")
    print("")
    print("Your Password is: " + ''.join(pw))
    print("")
    print("")

















