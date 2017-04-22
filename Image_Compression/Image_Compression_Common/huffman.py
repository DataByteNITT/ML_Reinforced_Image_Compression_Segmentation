#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 22:56:06 2017

@author: joy
"""

from itertools import groupby
from heapq import *
import base64


class Node(object):
    left = None
    right = None
    item = None
    wt = 0

    def __init__(self, item, wt):
        self.item = item
        self.wt = wt

    # Sets the children

    def setChild(self, lChild, rChild):
        self.left = lChild
        self.right = rChild

    def __lt__(self, a):
        return (self.wt < a.wt)

    def __eq__(self, a):
        return (self.wt == a.wt)

    def __repr__(self):
        return "%s - %s - %s - %s \n" \
            % (self.item, self.left, self.right, self.wt)

codes = {}


def enCode(str, node):
    if node.item:
        if not str:
            codes[node.item] = "0"
        else:
            codes[node.item] = str
    else:
        enCode(str+"0", node.left)
        enCode(str+"1", node.right)


def huffman_en(input):
    itemQ = [Node(a, len(list(b))) for a, b in groupby(sorted(input))]
    heapify(itemQ)
#    print(itemQ)
    while len(itemQ) > 1:
        l = heappop(itemQ)
        r = heappop(itemQ)
        n = Node(None, r.wt+l.wt)
        n.setChild(l, r)
        heappush(itemQ, n)

#    print(itemQ)
    enCode("", itemQ[0])
    result = "".join([codes[a] for a in input])
    print(codes)
    return result, itemQ, len(result) / (len(input) * 8)

def huffman_de(input, itemQ):
    curr = itemQ[0]
    str = ""
    for bit in input:
        if curr.item:
            str = str + chr(curr.item)
            curr = itemQ[0]
       
        if bit == "0":
            curr = curr.left
        else:
            curr = curr.right

    if curr.item:
            str = str + chr(curr.item)

    return str
      
def huffman(input):
    en, itemQ, ratio = huffman_en(input)  
    de = huffman_de(en, itemQ)
    print("Encoded: %s\nRatio: %f" % (en, ratio))
    return en, de

with open("download.jpg", "rb") as img:
    s = base64.b64encode(img.read())
#   print(len(str(s))
    p, q = huffman(s)
#   print(len(p.encode('utf-8')))
with open("new_img.jpg", "wb") as img_new:
        img_new.write(base64.b64decode(q))
