#!/usr/bin/env python3

import sys

print("### Running", *sys.argv, "###")       # a bit of logging

N = int(sys.argv[1])                         # number N > 2 to test
assert N > 2

d = 2                                        # trial divisor d = 2,3, ...
c = 0                                        # count 'composite' proofs 
composite = False
while d*d <= N:                              # try up to d <= sqrt(N)
    print()
    print(".. arranging {0} in {1} columns:".format(N,d))
    q,r = divmod(N,d)                        # Number = Quotient * Divisor + Remainder
    for i in range(1, q+1):                  # create q*d rectangle with q rows
        print("{0:3}".format(i), d * "o ")   # .. and d columns
    if r == 0:                               # No remainder?
        composite = True                     # .. we got a composite for sure!
        c = c + 1
        print("==> {0} = {1} cols * {2} rows; PROVED {0} is COMPOSITE".format(N,d,q), 29 * "-") 
    else:
        print("   ", r * "* ")                # .. for now: only display remainder
        print("==> {0} = {1} cols x {2} rows + {3} remaining".format(N,d,q,r)) 
    d = d + 1

print()
print("## We are DONE! ##########################################################")

# Now d*d > N, so do one more rectangle to show we're done: 
print("   ... since {0} * {0} > {1}".format(d,N))

q, r = divmod(N,d)                

print("   ... and we have a WIDE rectangle with {0} cols > {1} rows:".format(d,q))

for i in range(1, q+1):                       
    print("{0:3}".format(i), d * "o ")  
print("   ", r * "* ")               
print("  [ {0} = {1} cols x {2} rows + {3} remaining ]".format(N,d,q,r)) 
print()
print(74 * "#")
    
print("Using",d-2,"trial divisors,", end=" ")
if composite:
    print("proved {0} times over that {1} is COMPOSITE!".format(c,N))
else:
    print("PROVED ONCE ==> {0} is PRIME!".format(N)) 

print("Q.E.D.")
    
    
# Another way to show that we're done!?
# 17 = 4 x 4 + 1
    
# 5*5 = 25 = 17 + 8
# 8 = 1 x 5 + 3
    
#   1 o o o o o
#   2 o o o o o
#   3 o o o o o
#   4 o o . . .
#   5 . . . . .  


