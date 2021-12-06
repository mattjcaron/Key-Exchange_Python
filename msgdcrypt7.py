print("Key Generation")
# Program to generate keys from random, prime numbers p & q
"""
Generate two large random primes, p and q, of approximately equal size such that
their product n = pq is of the required bit length, e.g. 1024 bits. [See note 1].
Compute n = pq and (phi) φ = (p-1)(q-1). [See note 6].
Choose an integer e, 1 < e < phi, such that gcd(e, phi) = 1. [See note 2].
Compute the secret exponent d, 1 < d < phi, such that ed ≡ 1 (mod phi). [See note 3].
The public key is (n, e) and the private key (d, p, q). Keep all the values d, p, q and phi secret.
[We prefer sometimes to write the private key as (n, d) because you need the value of n when using d.
Other times we might write the key pair as ((N, e), d).]
n is known as the modulus.
e is known as the public exponent or encryption exponent or just the exponent.
d is known as the secret exponent or decryption exponent
"""
# import the random and math module
import random
import math

# k is the bit length for modulus N typically k= 1024, 2048, 3072, 4096,...
k=1024
k2=k/2-1
k1=k/2

# m is message to share privately by sender, bob
m=89;print("Message =",m)

# e for public key encrypt; small, odd number, co-prime number greater than 1 an less than Phi(n)
# Select a value of e from {5, 17, 257, 65537}
e=5;print("Public key e =",e)


# Check number input from rand.int for primality by factoring, p and q to be in range
j=0
prime = False
while prime == False:
    num=random.randrange(300,501)
    # check for factors for random number
    for i in range(2,int(math.sqrt(num))):
        if (num % i) == 0:break
    else:
        j+=1;
        if j==1:p=num;print("p =",p)
        if j==2:q=num;print("q =",q)
    if j==2:break

# Modulus N for public key
n=p*q; print("n =",n)
if m >> n: raise Exception("m > n")
print("p-1 =",p-1)
print("q-1 =",q-1)
phi=(p-1)*(q-1); print("Phi(N) =",phi)

#Check 1 < e > phi
if e<=1 or e>= phi:raise Exception('e not > 1 or < phi')


# d is Private key - decryptor such that the greatest common denominator equals one.
# Took from SO
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    if g != 1:
        raise Exception("egcd not equal to one")
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

check_e_p=egcd(e,p-1)
check_e_q=egcd(e,q-1)
check_e_phi=egcd(e,phi)
print ("check egcd e & p-1 =",check_e_p)
print ("check ecgd e & q-1 =",check_e_q)
print ("check egcd e & Phi =",check_e_phi)

#generate private key d
d = modinv(e, phi)
if d <= 1 or d >= phi:raise Exception('e not > 1 or < phi')
print("Decryption key d =", d)

# encrypted message c from sender bob
c=pow(m,e) % n; print("Encrypted message c =",c)

# decryption of message using d by recipient 
M= pow(c,d,n); print("Message =",M)

# Show modular inverse = 1
print('(E*D)%Phi =', (e*d)%phi)

#endprint