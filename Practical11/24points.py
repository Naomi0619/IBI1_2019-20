# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:13:50 2020

@author: Naomi
"""

def game(nums, op, eps):
    n = len(nums)
    # recurrsion times
    m = 0  
    if n == 1:
        return (abs(nums[0] - 24) < eps, m)
    
    for i in range(n):
        for j in range(i):
            p, q = nums[i], nums[j]
            tries = [p + q, p - q, q - p, p * q]
            if abs(p) > eps:
                tries.append(q / p)
            if abs(q) > eps:
                tries.append(p / q)
            ret = []
            for t in tries:
                ret, dm = game([nums[k] for k in range(n) if k != i and k != j] + [t], op, eps)
                m += dm + 1
                if ret:
                    return (True, m)
    return (False, m)
            
    

while True:
    input_str = input('Please input numbers to compute 24:(use \',\' to divide them)\n')
    try:
        nums = [int(x) for x in input_str.split(',')]
    except:
        print('Wrong format\n')
        continue
    if not all(n >= 1 and n <= 23 for n in nums):
        print('The input number must be integers from 1 to 23\n')
        continue
    break

ret, recurrsion_times = game(nums, None, 1e-3)
if ret:
    print('Yes')
    print('Recursion times:', recurrsion_times)
else:
    print('No')