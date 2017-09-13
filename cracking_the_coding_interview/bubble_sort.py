#!/bin/python

import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Write Your Code Here

n = 0
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            n += 1
    if n == 0:
        break
print "Array is sorted in {} swaps.".format(n)
print "First Element: {}".format(a[0])
print "Last Element: {}".format(a[len(a)-1])
        