#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    count = 1
    alpha = 'abcdefghijklmnopqrstuvwxyz'.upper()
    for ch in s:
        if ch in alpha:
            count += 1
    return count

if __name__ == '__main__':
    s = input()

    result = camelcase(s)

    print(result)