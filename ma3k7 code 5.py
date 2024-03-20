# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:18:17 2024

@author: corey
"""

import numpy as np
from turtle import *

n = 50

def primality_checker(num):
    cofactors = np.arange(2,num)
    prime = True
    
    if num == 1:
        prime = False
        
    for i in cofactors:
        remain = num % i
        if remain == 0:
            prime = False
            break
    return prime

def odd_checker(num):
    odd = False
    if num % 2 == 0:
        odd = True
    return odd

num = 0


for i in range(1,n):
    
    for _ in range (i):
        num+=1
        primality = primality_checker(num)
        if primality:
            dot(7,"red")
        else:
            dot(3, "black")
        forward(10)
    left(90)
    
    for _ in range (i):
        num+=1
        primality = primality_checker(num)
        if primality:
            dot(7, "red")
        else:
            dot(3, "black")
        forward(10)
    left(90)
    
color("white")
while True:
    forward(1)