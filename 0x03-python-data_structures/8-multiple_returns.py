#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length > 0:
        first = sentence[0]
    else:
        firts = None
    return length, first
