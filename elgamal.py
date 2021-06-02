import random

#import random from library
from params import p
from params import g

def keygen():
    sk = random.randint(1,p)
    pk = pow(g, sk, p)
    return pk,sk

def encrypt(pk,m):
    #define r
    rand = random.randint(1,p)
    # formula goes here
    c1 = pow(g, rant, p)
    #formula goes here
    c2 = (m * pow(pk, rand, p)) %  p
    return [c1,c2]

def decrypt(sk,c):
    [c1, c2] = c

    #Define S
    s = pow(c1, sk, p)
    #Define M
    m = (c2 * pow(s, -1, p)) % p
    return m

pk, sk = keygen()
print(pk)
print(sk)
m = 12239119
print (decrypt(sk, encrypt(pk, m)))
