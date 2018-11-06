#!/usr/bin/env python3

import sys

print("### Running", *sys.argv, "###\n")     # a bit of logging

N = int(sys.argv[1])                         # number N to test

d = 2
c = 0                                        # number of times we proved composite
is_prime = True
while d*d <= N:                              # enough to test only d <= sqrt(N)
    q, r = divmod(N,d)                       # Number = Quotient * Divisor + Remainder
    for i in range(q):                       # q is the number of rows to create
        print("{0:3}".format(i+1), d * "o")  # .. each being d elements (columns) wide
    if r == 0:                               # No remainder?
        is_prime = False                     # .. we got a composite for sure!
        c = c + 1
        print("[ {0} = {1} * _{2}_ ] PROVED COMPOSITE".format(N,d,q)) 
    else:
        print("   ", r * "*")                # .. for now: only display remainder
        print("[ {0} = {1} * _{2}_ + {3} ]".format(N,q,d,r)) 
    print()
    d = d + 1

if is_prime:
    print("PROVED",N,"is PRIME using",d-2,"trial divisons") # .. only now can we be sure!
else:
    print("PROVED",N,"is COMPOSITE",c,"times!")    # .. ok, we knew this already (redundant)
