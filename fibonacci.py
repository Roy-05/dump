# An extremely fast implementation of fibonacci using Recursion
# Saket Roy, February 14th 2020

import time
import random

#Return the nth fibo element
def recursive(n, a, b):
    if(n<=2):
        return 1
    else:
        return a + recursive(n-1, b, a+b)

for i in range(1,30):
    print(recursive(i,1,1))
