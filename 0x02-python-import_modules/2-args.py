#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num_elem = len(argv)
    n = 1

    if num_elem == 1:
        print("{} arguments.". format(num_elem - 1))
    elif num_elem > 1:
        s = "" if num_elem == 2 else "s"
        print("{} argument{}:".format(num_elem - 1, s))

        while n < num_elem:
            print("{}: {}".format(n, argv[n]))
            n += 1
