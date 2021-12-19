import math


def proverka_prost(n):
    
    d = 2
    while n% d != 0:
        d+=1
    return d == n