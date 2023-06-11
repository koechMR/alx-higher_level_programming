#!/usr/bin/python3
def no_c(my_string):
    value = ''
    for char in my_string:
        if char.lower() != 'c':
            value += char
    return value
