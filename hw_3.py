# Name: Kenneth Ruiter
# hw3.py

import math
import random

# ********** Exercise 1 ********** 

# Define is_divisible function here
def is_divisible(n,m):
    if(n == 0):
        return(True)
    elif(m == 0):
        return(False)
    return(n % m == 0)

# Test cases for is_divisible
print(is_divisible(10, 5))  # This should return True
print(is_divisible(18, 7))  # This should return False
print(is_divisible(42, 0))  # This should return False

# ********** Exercise 2 ********** 

# Define not_equal function here
def not_equal(n,m):
    if(n == m):
        return(False)
    return(True)

# Test cases for not_equal
print(not_equal(2,2))
print(not_equal(2+3,2+2))
print(not_equal('ab','a' + 'b'))

# ********** Exercise 3 ********** 

## 1 - multadd function
def multadd(a,b,c):
    return(a*b+c)

## 2 - Equations
print(multadd(1,2,3))
print(multadd(2,1,3))


# Test Cases
angle_test = multadd(math.cos(math.pi/4),1/2,math.sin(math.pi/4))
print("sin(pi/4) + cos(pi/4)/2 is:")
print(angle_test)

ceiling_test = multadd(2, math.log(12,7), math.ceil(276/19))
print("ceiling(276/19) + 2 log_7(12) is:")
print(ceiling_test)


# ********** Exercise 4 **********

## 1 - rand_divis_3 function
def rand_divis_3():
    randnum = random.randint(0,100)
    print(randnum)
    return(is_divisible(randnum,3))

# Test Cases
print(rand_divis_3())
print(rand_divis_3())
print(rand_divis_3())

