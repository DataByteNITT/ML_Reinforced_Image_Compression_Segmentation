#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 21:31:01 2017

@author: joy
"""
import base64


def lwz_encode(input):
    codes = dict([(chr(x), x) for x in range(256)])
    code_count = 256
    curr_str = ''
    en_data = []
    input = str(input)
    for c in input:
        curr_str = curr_str + str(c)
        if curr_str not in codes.keys():
            codes.update({curr_str: code_count})
            en_data.append(codes[curr_str[:-1]])
            code_count += 1
            curr_str = c

    en_data.append(codes[curr_str])
    return en_data


def lwz_decode(input):
    strings = dict([(x, chr(x)) for x in range(256)])
    next_code = 256
    de_str = ""
    prev_str = ""
    for x in input:
        if x not in strings.keys():
            new_str = prev_str + (prev_str[0])
            strings.update({x: new_str})
        de_str += strings[x]
        if len(prev_str) != 0:
            strings[next_code] = prev_str + (strings[x][0])
            next_code += 1
        prev_str = strings[x]
    return de_str

with open("download.jpg", "rb") as img:
    s = base64.b64encode(img.read())
#   print(len(str(s))
    p = lwz_encode(str(s))
    q = lwz_decode(p)
#   print(len(p.encode('utf-8')))
    print("Compression Ratio : " + str(len(p) / len(s)))
with open("new_img.jpg", "wb") as img_new:
        img_new.write(base64.b64decode(q[2:]))
