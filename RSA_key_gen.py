# -*- coding: utf-8 -*-
# RSA private key generator with public key 0x7fffffff
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

def extended_euclid (a, b):
    if b == 0:
        return (a, 1, 0)
    (D, X, Y) = extended_euclid (b, a % b)
    (d, x, y) = (D, Y, X - Y * int (a / b))
    return (d, x, y)
    
def inv (phiN, e1):
    (d, x, y) = extended_euclid (e1, phiN)
    return x

p = 2 # replace with a 512-bit prime
q = 3 # replace with a 512-bit prime
N = p * q
phiN = (p - 1) * (q - 1)
e1 = 0x7fffffff
e2 = inv (phiN, e1)
print hex (N)
print hex (phiN)
print hex (e1)
print hex (e2)
