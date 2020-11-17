# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 18:08:56 2020

@author: Denes Sexty
"""
import matplotlib.pyplot as plt

seed=0x1a57f26c

def LFSR(seed,taps,n):
    strdigits=bin(seed)[2:].zfill(n)
    bindigits=[1]*n
    for i in range(n):
        bindigits[i]=int(strdigits[i])
    newbit=0
    while True:
#        print(bindigits)
        newbit=0
        for i in taps:
            newbit^=bindigits[i]
        yield newbit
        bindigits=([newbit]+bindigits)[:n]
            
        
def randfloatLFSR(seed,taps,n,m):
    mygen=LFSR(seed,taps,n)
    fakt=1.0/2**m
    while True:
        newnum=0
        for i in range(m):
            newnum*=2
            newnum+=next(mygen)
        yield newnum*fakt

def floatLCG(seed,m,a,c):
    x=seed
    fakt=1.0/m
    while True:
        x=(a*x+c) % m
        yield x*fakt
        
        
def floatmiddlesquare(seed,ndigs):
    x=seed
    fakt=1.0/10**ndigs
    while True:
        x=int(str(x*x).zfill(2*ndigs)[int(ndigs/2):int(2*ndigs-ndigs/2)])
        yield x*fakt

LCGgen1=floatLCG(31213,pow(2,17),1277,0)
LCGgen2=floatLCG(16807555,pow(2,31)-1,16807,0)
LCGgen3=floatLCG(3113,pow(2,31)-1,48271,0)
LCGgen4=floatLCG(1131,pow(2,48),25214903917,11)       

middlegen=floatmiddlesquare(1215678432232,10)


gen=LFSR(seed,[10,12,13,15],16)
'''
for i in range(3):
    print(next(gen))

floatgen=randfloatLFSR(seed,[10,12,13,15],16,32)

for i in range(10):
    print(next(floatgen))
    
randoms=[ next(floatgen) for i in range(100000) ]    
    
plt.hist(randoms)
plt.show()   '''