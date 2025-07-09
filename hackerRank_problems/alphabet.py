#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 08:56:10 2025
Check out my YouTUBE: @Data_Details
Code will be uploaded to Github: sxMLx
              https://github.com/sxMLxr
"""

size = 5
alphabet = []
lines = []
pattern = "-"

for i in range(size):
    alphabet.append(chr(ord("a")+i))
'''
for i in range(size):
    pattern = "-".join(alphabet[(size-1)-i])
    for i in pattern:
        patternb = "-".join(i).center(size*4-3,"-") 
'''    
    
lines = []
for i in range(size):
    pattern = "-".join(alphabet[:i + 1])
    lines.append((pattern + pattern[-2::-1]).center(4 * size - 3, "-"))

print("\n".join(lines + lines[-2::-1]))
