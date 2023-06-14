#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = len(sys.argv)-1
    if a == 0:
        print("0 arguments.")
    elif a == 1:
        print("1 arguments:")
    else:
        print("{} arguments:".format(a))
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
