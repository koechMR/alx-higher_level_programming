#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    result = sum(int(arg) for arg in arguments)
    print(result)
