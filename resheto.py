import math


def proverka_prost(n):
    if n==1:
        return False
    d = 2
    while n% d != 0:
        d+=1
    return d == n