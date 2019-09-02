# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 06:25:36 2019

@author: tony
"""


#factorial solution
def factorial(n):
    # Solve the base case
    if n == 0 or n == 1:
        return 1
    
    else:
            
        return n*factorial(n-1)
    
print(factorial(2))

#Slow Fib Solution
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    
    else:
        return fibonacci(n-2) + fibonacci(n-1)#?

print(fibonacci(10))


#Number of fib operations
def num_operations_fibonacci(n):
    if n in [1, 2]:
        return 0

    else:
        return 1+ num_operations_fibonacci(n-1) + num_operations_fibonacci(n-2)#?

print(num_operations_fibonacci(10))

# slow fib runtime
num = (4.8*10**208)/(10**15*60*60*24*365)

print(num)

# Faster Fib (n-1 operations)

def smart_fibonacci(n):
    a, b = 0, 1
    for i in range(1,n):
        a, b = b, a+b
    return b

print(smart_fibonacci(1000))