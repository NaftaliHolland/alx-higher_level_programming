#!/usr/bin/python3
alphabet = "abcdefghijklmnopqrstuvwxyz"
for character in alphabet:
    if character not in ("q", "e"):
        print("{}".format(character), end = "")
