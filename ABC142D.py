import fractions
A,B = map(int,input().split())
GCD = fractions.gcd(A,B)
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
c = prime_factorize(GCD)
C = set(c)
print(len(C)+1)