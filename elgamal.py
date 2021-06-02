import random

#import random from library
from params import p
from params import g

def keygen():
    get_random = random.randint(1,p)
    #set SK
    sk = get_random
    #set pk
    pk = pow(g, sk, p)
    return pk,sk

def encrypt(pk,m):
    #define r
    rand = random.randint(1,p)
    r = rand
    # formula goes here
    c1 = pow(g, r, p)
    #formula goes here
    c2 = (pow(pk, r, p) * (m % p)) %  p
    return [c1,c2]

def decrypt(sk,c):
    c1 = c[0]
    #use array index
    c2 = c[1]
    #use array index

    #Define M
    m = ((c2 % p) * pow(c1, -sk, p), sk, p) % p
    return m

pk, sk = keygen()
print(pk)
print(sk)
m = 12239119
print (decrypt(sk, encrypt(pk, m)))
