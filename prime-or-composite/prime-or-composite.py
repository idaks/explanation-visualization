#!/usr/bin/env python3

import sys

print("### Running", *sys.argv, "###\n")                  # a bit of logging

N = int(sys.argv[1])                                      # number N to test

d = 2
is_prime = True
while d*d <= N:                                           # enough to test only d <= sqrt(N)
    q, r = divmod(N,d)
    print("[ {0} = {1} * {2} + {3} ]".format(N, d, q, r)) # Number = Divisor * Quotient + Remainder
    for i in range(q):                                    # q is the number of rows to create
        print("{0:3}".format(i+1), d * "o")               # .. each being d elements (columns) wide
    if r == 0:                                            # No remainder?
        is_prime = False
        print("PROVED composite: {0} = {1} * {2}".format(N, d, q)) # .. we got a composite for sure!
    else:
        print("   ", r * "*")                                      # .. for now: display remainder
    print()
    d = d + 1

if is_prime:
    print("PROVED", N, "is PRIME!")                        # Only now can we be sure!
else:
    print("Sorry", N, "is composite ..")                   # .. ok, we knew this already (redundant)
