# -*- coding: utf-8 -*-
# file coder with RSA 1024-bit
# Copytight © 2016 Liu Jiacheng. All rights reserved. 

# calling method 1: python RSA_coder.py decode {last 32 hex digits of private key}
# precondition: a .pwd file (cipher form)
# postcondition: a .tmp file (plain form)

# calling method 2: python .coder.py encode {encoding password}
# precondition: an updated .tmp file (plain form)
# postcondition: an updated .pwd file and a ._pwd file

import numpy as np
import sys, os

decode_code_len = 32
encode_code = '19980617'
public_key = 0x7fffffff
unit = 64

def mod_exp (a, u, n):
    base = a
    res = 1
    while u != 0:
        if u % 2 != 0:
            res = (res * base) % n
        base = (base * base) % n
        u = (u - u % 2) / 2
    return res

def execute ():
    def print_intro ():
        os.system ('echo "file coder with RSA 1024-bit"')
        os.system ('echo "Copytight © 2016 Liu Jiacheng. All rights reserved. "')
        os.system ('echo "calling method 1: python RSA_coder.py decode {last 32 hex digits of private key}"')
        os.system ('echo "precondition: a .pwd file (cipher form)"')
        os.system ('echo "postcondition: a .tmp file (plain form)"')
        os.system ('echo "calling method 2: python .coder.py encode {encoding password}"')
        os.system ('echo "precondition: an updated .tmp file (plain form)"')
        os.system ('echo "postcondition: an updated .pwd file and a ._pwd file"')
    if len (sys.argv) < 3:
        os.system ('echo "Syntax error"')
        print_intro ()
        exit (0)
    if sys.argv[1] == 'decode':
        if len (sys.argv[2]) == decode_code_len:
            n = int (open ('./.n', 'r').read (), 16)
            e = int (open ('./.e', 'r').read (), 16)
            e = e * pow (16, decode_code_len) + int (sys.argv[2], 16)
            decode ('./.pwd', './.tmp', n, e)
            os.system ('vi .tmp')
        else:
            os.system ('echo "Decoding password error"')
            print_intro ()
            exit (0)
    elif sys.argv[1] == 'encode':
        if sys.argv[2] == encode_code:
            os.system ('cp .pwd ._pwd')
            n = int (open ('./.n', 'r').read (), 16)
            e = public_key
            encode ('./.tmp', './.pwd', n, e)
            os.system ('rm .tmp')
        else:
            os.system ('echo "Encoding password error"')
            print_intro ()
            exit (0)
    else:
        os.system ('echo "Syntax error"')
        print_intro ()
        exit (0)

def encode (input_dir, output_dir, N, e):
    input_file = open (input_dir, 'r')
    input_str = input_file.read ()
    while (len (input_str)) % unit != 0:
        input_str += ' '
    input_file.close ()
    
    output_file = open (output_dir, 'w')
    for i in range (0, (len (input_str)) / unit, 1):
        pre = 0
        for j in range (0, unit, 1):
            pre = pre * 256 + ord (input_str[i * unit + j])
        post = mod_exp (pre, e, N)
        stre = hex (post)
        stre = stre.replace ('L', '\n')
        output_file.write (stre)
    output_file.close ()

def decode (input_dir, output_dir, N, e):
    input_file = open (input_dir, 'r')
    input_strs = input_file.readlines ()
    input_nums = []
    for stre in input_strs:
        input_nums.append (int (stre, 16))
    input_file.close ()
    
    output_file = open (output_dir, 'w')
    for pre in input_nums:
        post = mod_exp (pre, e, N)
        tmp = []
        for i in range (0, unit, 1):
            tmp.append (chr (post % 256))
            post /= 256
        for i in range (unit - 1, -1, -1):
            output_file.write (tmp[i])
    output_file.close ()

execute ()

'''
def codee (dir_from, unit_from, dir_to, unit_to, N, e):
    inpute = open (dir_from, 'r').read ()
    os.system ('echo "%s"' % inpute)
    outpute = ''
    while (len (inpute)) % unit_from != 0:
        inpute += ' '
    for i in range (0, (len (inpute)) / unit_from, 1):
        pre = 0
        for j in range (0, unit_from, 1):
            pre = pre * 256 + ord (inpute[i * unit_from + j])
        os.system ('echo %s' % hex (pre))
        post = mod_exp (pre, e, N)
        os.system ('echo %s' % hex (post))
        tmp = []
        for j in range (unit_to - 1, -1, -1):
            tmp.insert (j, chr (post % 256))
            post /= 256
        for j in range (0, unit_to, 1):
            outpute += tmp[j]
    open (dir_to, 'w').write (outpute)
    os.system ('echo "%s"' % outpute)
'''
