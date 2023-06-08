#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]

    a = len(arguments)
    if a == 0:
        print("0 arguments.")
    elif a == 1:
        print("1 arguments.")
    else:
        print("{} arguments:".format(a))
    for i, argument in enumerate(arguments, start=1):
        print("{}: {}".format(i, argument))
