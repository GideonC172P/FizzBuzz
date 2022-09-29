# -*- coding: utf-8 -*-
"""
Spyder Editor

Like I made this, and it works 
which is cool :D
Gideon Nebelsick 
"""

a=0


while a<100:
    a=a+1
    word=""
    b=a%3
    c=a%5
    if b==0:
        word="Fizz"
    else:
        n1=1
    if c==0:
        word="Buzz"
    else:
        n1=2
    if c==0 and b==0:
        word="FizzBuzz"
    else:
        n1=3
    if len(word)==0:
        print(a)
    else:
        print(word)
    n1=4
    

n1=5
print("Happy Days :D")