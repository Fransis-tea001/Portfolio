#PrimeFactorization Program

import os
import sys
import math
import time
from time import sleep

os.system('clear')

print("Start PrimeFactorization Program")

def primefactor(Unum):
    while Unum%2 == 0:
        print(2)
        Unum = Unum/2
    
    for i in range(3,int(math.sqrt(Unum))+1,2):
        while Unum % i == 0:
            print (i)
            Unum = Unum / i

    if Unum > 2:
        print (Unum)

programSelect = input("1.Find prime factor\n2.Exit\nEnter : ")

if programSelect == '1':
    os.system('clear')
    Unum = int(input("Please Enter number to check : "))
    primefactor(Unum)

elif programSelect == '2':
    print("---Exit Program---")
    time.sleep(2)
    os.system('clear')
    sys.exit(0)



