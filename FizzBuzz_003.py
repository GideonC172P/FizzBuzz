# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 18:16:17 2022

@author: Gideon
"""

n=3

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        l1=[]
        for g in range(0, n):
            n=g+1
            word=""
            b=n%3
            c=n%5
            if c==0 and b==0:
                word="FizzBuzz"
            elif b==0:
                word="Fizz"
            elif c==0:
                word="Buzz"
            else:
                word=str(n)
            l1.append(word)       
        return l1

n=3    
c4=Solution()
r4=c4.fizzBuzz(n)       
print(r4)   

