#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    num_elem = len(argv) - 1
    sum_arg = 0

    for i in range(num_elem):
        sum_arg += int(argv[i + 1])
    print("{}".format(sum_arg))
