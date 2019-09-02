# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



1600000/961*2
3528000/2000

80*9.8*3000


def fibonacci(n):
    if n < 0:
        raise ValueError("invalid index!")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
        
fibonacci(12)


#Binary Search
# Returns True if A contains item and False otherwise
def binary_search(A, item):
    if len(A) == 0:
        return False
    else:
        middle = len(A) // 2
        if A[middle] == item:
            return True
       # your code goes here
    if item<A[middle]:
        #A[:middle] is a copy of the elements of A to the left of middle
            return binary_search(A[:middle], item)
    else:
        #A[middle+1:] is a copy of the elements of A to the right of middle
            return binary_search(A[middle + 1:], item)
numbers = [1, 2, 3, 5, 8, 22, 34, 42, 87, 103]
print(binary_search(numbers, 4))
print(binary_search(numbers, 42))


#mergesort
def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    #Add any remaining elements in the left or right lists. 
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result

def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

#end mergesort
4**3
64**(1/2)

343/.00858
2*20**(1/2)
6*5**(1/2)

def move(n,A,B):

#Let C be the third tower (that isn't A or B)

    if (n == 1):
        move the top disk on A to B

    if (n == 2):
        move(1,A,C) # move smallest from A to C
        move(1,A,B) # move top disk from A to B
        move(1,C,B) # move smallest from C to B

    if (n>2):
        move(n-1,A,C)
        move(n-2,C,B)
        move(1,C,A) # move disk from C to A
        move(n-2,B,A)
    
    
move(3,A,B)    

2**10-1