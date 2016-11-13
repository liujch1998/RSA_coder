# -*- coding: utf-8 -*-
# generator of 512-bit primes with form "11...."
# Copytight © 2016 Liu Jiacheng. All rights reserved. 

import numpy as np

def mod_exp (a, u, n):
    base = a
    res = 1
    while u != 0:
        if u % 2 != 0:
            res = (res * base) % n
        base = (base * base) % n
        u = (u - u % 2) / 2
    return res

def witness (a, n):
    u = n - 1
    t = 0
    while u % 2 == 0:
        t = t + 1
        u = u / 2
    x = mod_exp (a, u, n)
    for i in range (1, t + 1, 1):
        y = (x * x) % n
        if (y == 1) and (x != 1) and (x != n - 1):
            return True
        x = y
    if x != 1:
        return True
    return False

def miller_rabin (n, s):
    for j in range (0, s, 1):
        a = np.random.randint (1, 65535)
        if witness (a, n) == True:
            return False
    return True
    
for oo in range (0, 10000, 1):
    n = 0
    for i in range (1, 512, 1):
        p = np.random.randint (0, 2)
        if i == 1 or i == 2:
            p = 1
        n = (n + p) * 2
    n = n + 1
    if miller_rabin (n, 20):
        print n
