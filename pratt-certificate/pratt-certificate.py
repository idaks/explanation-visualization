#!/usr/bin/env python3

def factors(n):
    """Return sorted set of prime factors of n"""
    d = 2
    factors = set() 
    while n > 1:
      if n % d == 0:
        factors.add(d)
        n = n/d
      else:
        d = d + 1
    return sorted(factors) # sort to avoid out-of-order presentation

def factorization(n):
    """Return prime factorization of n as sorted list"""
    d = 2
    factors = []
    while n > 1:
      if n % d == 0:
        factors.append(d)
        n = n/d
      else:
        d = d + 1
    return factors  # sorted automatically

# LUCAS-LEHMER Primality Test and PRATT certificate
# Derived from https://en.wikipedia.org/wiki/Lucas_primality_test#Algorithm
# and https://de.wikipedia.org/wiki/Lucas-Test_(Mathematik)#Verbesserter_Lucas-Test

def lucas(n):
    if n == 2:
        print("\nLEAF (PRIME : WITNESS) = (2:1)")
        return 
    print("\n--- TESTING {0} ".format(n) + 70*"-")
    for a in range(2,n):
        if pow(a, n-1, n) != 1:
            print("{0} is COMPOSITE because {1}^{2} != 1 (mod {0})".format(n,a,n-1))
            break
        else:
            obligations = factorization(n-1)
            for q in obligations:
                e = (n-1)//q
                if pow(a, e, n) == 1:
                    print("// {0} is NO witness since {0}^({1}/{2}) = {0}^{3} == 1 (mod {4})".format(a,n-1,q,e,n))
                    break
                else:
                    print(".. EDGE: {0}^({1}/{2}) = {0}^{3} != 1 (mod {4})".format(a,n-1,q,e,n))
            else:
                print(".. VERTEX: {1}^{2} == 1 (mod {0})".format(n,a,n-1))
                print(".. PRODUCT: {0} = {1} + 1".format(n, "*".join(str(q) for q in obligations)))
                print("=> (PRIME : WITNESS) = ({0} : {1})".format(n,a))
                # Call obligations recursively here? Or better return to the caller .. !?
                # for q in sorted(set(obligations), reverse=True):
                #     print(80 * "-")
                #     lucas(q)
                break # use this break to quit after first witness 
    return

if __name__ == '__main__':

    for n in range(2, 100+1): lucas(n)
    
    #lucas(7919)
    #lucas(229)
    lucas(474397531)
    lucas(251)
    lucas(5)
    lucas(3)
    lucas(2)
        
