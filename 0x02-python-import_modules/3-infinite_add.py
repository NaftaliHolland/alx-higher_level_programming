#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    my_sum = 0
    for number in range(1, len(argv)):
        my_sum += int(argv[number])
    print("{}".format(my_sum))
