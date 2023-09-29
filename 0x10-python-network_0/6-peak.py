#!/usr/bin/python3
"""
   function that finds a peak in a list of unsorted integers
"""


def find_peak(num):
    '''Finds the peak in a list'''
    length = len(num)
    if length == 0:
        return None
    if length == 1:
        return (num[0])
    if length == 2:
        return num[0] if num[0] >= num[1] else num[1]

    for lx in range(0, length):
        value = num[lx]
        if (lx > 0 and lx < length - 1 and
                num[lx + 1] <= value and num[lx - 1] <= value):
                return value
        elif lx == 0 and num[lx + 1] <= value:
            return value
        elif lx == length - 1 and num[lx - 1] <= value:
            return value
    return value
