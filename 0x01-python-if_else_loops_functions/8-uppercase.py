#!/usr/bin/python3
def uppercase(str):
    for character in str:
        unicode = ord(character)
        if 123 > unicode > 96:
            unicode -= 32
        print("{}".format(chr(unicode)), end="")
    print()
