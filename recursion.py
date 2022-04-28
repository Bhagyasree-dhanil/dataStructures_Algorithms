"""


"""

# find the sum of n numbers
import numpy as np

# method 1
n = 5
arr_list = np.arange(1, n+1)
print(sum(arr_list))

# method 2 - iterative approach
sum_val = 0
for i in range(1, n+1):
    sum_val += i
print(sum_val)

# method 3 - recursion approach
"""
Two criteria

1. repetitive task your are doing
2. Base condition which terminate your recursion

once we reach the break point then it will unstack the windings.
and finally returns the first mentioned  return

5 + f[4] -->  4 + f[3] -->  3 + f[2] --> 2 + f[1] --> 1
result = 5+4+3+2+1 = 10
"""


def sum_n(val):
    if val == 1:
        return 1
    return val + sum_n(val - 1)


print(sum_n(5))

# create fibinocci series - iterative approach
# 0,1,1,2,3,4,5


def fib(fib_range):

    fib_array = []
    fib_array.extend([0, 1])
    a = 0
    b = 1
    for k in range(2, fib_range):
        c = a+b
        fib_array.append(c)
        a, b = b, c
    print(fib_array)


fib(5)

# fibinocci using recursive approach
# fib series=0,1,2,3,5,8 -->
# index =    0,1,2,3,4,5
# base criteria set first 2 element


def fib_rec(no):
    if no == 0 or no == 1:
        return no
    return fib_rec(no-1) + fib_rec(no-2)


fib_range = 5
fib_list = []
for i in range(fib_range):
    fib_list.append(fib_rec(i))
print(fib_list)

# write a python program to recursion list sum.
# test_data = [1,2,[3,4],[5,6]] ==> output = 21


def find_sum(test_data):
    test_sum = 0
    for td in test_data:
        if type(td) is int:
            test_sum += td
        else:
            test_sum += find_sum(td)
    return test_sum


test_data = [1, 2, [3, 4], [5, 6]]
print(find_sum(test_data))

# find factorial of non-negative no
# 4! = 4*3*2*1
# n! = n*(n-1)!


def fact(num):
    if num == 1:
        return 1
    return num * fact(num-1)


print(fact(4))

# find sum of non-negative numbers

# iterative approach


def sum_no(int_val):
    str_val = str(int_val)
    sum_val = 0
    for sd in str_val:
        sum_val += int(sd)
    return sum_val


print(sum_no(321))


# recursive approach

def find_int_sum(value):
    if value == 0:
        return 0
    vl = value % 10
    return vl + find_int_sum(int(value/10))


print("recursive sum", find_int_sum(321))


# calculate sum of positive integers of n + (n-2) + (n-4) +....(n-x) =< 0
# 6 --> 6+4+2+0 ==> 12
# 5 --> 5+3+1 ==> 9

def sum_series(nos):
    if nos < 0:
        return 0
    else:
        return nos + sum_series(nos-2)


print(sum_series(10))

# calculate harmonic sum of n-2
# harmonic sum = sum of reciprocals of positive integers
# 1+ 1/2 + 1/3 + 1/4


def harm_sum(no):
    if no == 1:
        return 1
    return 1/no + harm_sum(no-1)


print(harm_sum(5))

# find the greatest common divisor of two integers(gcd) or hcf
"""
2 | 8,6 
  | 4,3
  
  LCM = 2*4*3 = 24 ==> 
  HCF = 2          ==> 
  
  no 1 * no 2 = lcm * hcf
  lcm = no1 * no2 / hcf
  
  hcf - highest common factor or greatest common divisor
  
  divisors of 8,6 
  8 - 1,2,4,8
  6 - 1,2,3,6
  common -2 ==> greatest divisor of both
  
  lcm - least common multiple
  
  8 - 8,16,24,32,40
  6 - 6,12,18,24,30
  least common -24
  

"""


def find_cf(a, b):
    if a > b:
        small = b
    else:
        small = a

    hcf = 1
    for k in range(2, small+1):
        if a % k == 0 and b % k == 0:
            hcf = k

    lcm = (a*b)/hcf
    return hcf,lcm


print(find_cf(8,6))

