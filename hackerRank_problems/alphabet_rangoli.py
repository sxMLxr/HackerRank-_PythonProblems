#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 08:51:03 2025
Check out my YouTUBE: @Data_Details
Code will be uploaded to Github: sxMLx
              https://github.com/sxMLxr
"""

def print_rangoli(size):
    # your code goes here
    if not 0 < size < 27:
        return 

    #size = 5
    alphabet =[]
    
    for i in range(size):
        alphabet.append(chr(ord("a")+i))
    
    alphabet = alphabet[::-1]
    
    lines = []
    for i in range(size):
        pattern = "-".join(alphabet[:i + 1])
        lines.append((pattern + pattern[-2::-1]).center(4 * size - 3, "-"))
    
    print("\n".join(lines + lines[-2::-1]))       
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)