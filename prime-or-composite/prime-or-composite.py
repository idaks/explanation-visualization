#!/usr/bin/env python3

import sys

print("### Running", *sys.argv, "###\n")                  # a bit of logging

N = int(sys.argv[1])                                      # number N to test

d = 2
is_prime = True
while d*d <= N:                                           # the largest divisor d to try is ceiling(sqrt(N))
    q, r = divmod(N,d)
    print("[ {0} = {1} * {2} + {3} ]".format(N, d, q, r)) # Number = divisor * quotient + remainder
    for i in range(d):                                    # d is the number of columns to create
        print("{0:3}".format(i+1), q * "o")               # .. each having q many elements 'o' 
    if r == 0:                                            # No remainder?
        is_prime = False
        print("PROVED composite: {0} = {1} * {2}".format(N, d, q)) # .. we got a composite!
    else:
        print("   ", r * "*")                                     # .. for now: display remainder.
    print()
    d = d + 1

if is_prime:
    print("PROVED", N, "is PRIME!")
else:
    print("Sorry", N, "is composite ..")
