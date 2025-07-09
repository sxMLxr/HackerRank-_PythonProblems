#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 08:51:03 2025
Check out my YouTUBE: @Data_Details
Code will be uploaded to Github: sxMLx
              https://github.com/sxMLxr
"""
import os

def solve(s):
    split_text = s.split()
    for i in range(len(split_text)):

        if (split_text[i].isalpha()):
            split_text[i] = split_text[i].capitalize()        

    return split_text

if __name__ == '__main__':
    #fptr = open(os.environ['/changes.txt'], 'w')
    s = input()
    result = solve(s)
    #fptr.write(result + '\n')
    #fptr.close()
    print(result)
    