#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'morganAndString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def morganAndString(a, b):
    # Write your code here
    a += 'z'
    b += 'z'
    res = ''
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i:] < b[j:]:
            res += a[i]
            i += 1
        else:
            res += b[j]
            j += 1
    return res[0:-1]


print(morganAndString("ABACABA","ABACABA", ))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         a = input()

#         b = input()

#         result = morganAndString(a, b)

#         fptr.write(result + '\n')

#     fptr.close()
