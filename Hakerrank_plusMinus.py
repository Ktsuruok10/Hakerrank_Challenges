#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 22:11:44 2023

@author: kellentsuruoka
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg =0
    zeros = 0
    for a in arr: 
        if a >0:
            pos+=1
        elif a < 0:
            neg+=1
        elif a == 0:
            zeros+=1
    pos_ratio = pos/len(arr)
    neg_ratio = neg/len(arr)
    zeros_ratio = zeros/len(arr)
    print("{:.6f}".format(pos_ratio))
    print("{:.6f}".format(neg_ratio))
    print("{:.6f}".format(zeros_ratio))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
