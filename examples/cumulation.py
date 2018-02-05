#!/usr/bin/python
# -*- coding:utf8 -*

print ("Cumul\n")

rate = 1.04

flat = []

def compute(flat):
    sum = 0.0
    current = 40.0
    
    for i in range(0, 40):
        sum = sum + current
        if (i not in flat):
            current = current * rate
    print(i, ": sum=", sum, ", current=", current)
    return sum
    
full = compute([])
flat_10 = compute([10])
flat_35 = compute([35])

print ("diff 10 = ", full - flat_10)
print ("diff 35 = ", full - flat_35)
print ("bye")

# Nothing in flat, sum = 9502.55
# 10 is flat       sum = 9188.93    diff = 314
# 35 is flat       sum = 9435.52    diff =  67
