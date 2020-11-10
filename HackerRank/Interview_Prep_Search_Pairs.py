#!/bin/python3

import math
import os
import random
import re
import sys

def binarySearch(arr, left, right,number_1,target):
    if(right<left):
        return(-1)
    mid = int((left + right)/2)
    diff = abs(arr[mid]-number_1)
    if(diff == target):
        return(mid)
    elif(diff<target):
        return(binarySearch(arr,mid+1,right,number_1,target))
    else:
        return(binarySearch(arr,left,mid-1,number_1,target))
# Complete the pairs function below.
def pairs(k, arr):
    arr.sort()
    n = len(arr)
    cnt = 0
    for i in range(n):
        number_1 = arr[i]
        index = binarySearch(arr, i+1, n-1, number_1,k)
        if(index != -1):
            cnt += 1
    return(cnt)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
