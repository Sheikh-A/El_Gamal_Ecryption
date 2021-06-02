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
    c0 = c[0]
    #use array index
    c1 = c[1]
    #use array index
    funcC0 = pow(c0, sk, p)

    #Modular Inverse
    funcC1 = c1 * pow(funcC0, -1, p)
    #Define M
    m = pow(funcC1, 1, p)
    return m
