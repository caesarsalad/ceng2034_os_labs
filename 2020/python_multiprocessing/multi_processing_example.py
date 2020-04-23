#!/usr/bin/python3
import os
from multiprocessing import Pool


def check_prime(num):
    print("checking prime... ", num, "PID: ", os.getpid())
    if num >1:
        for i in range(2,num):
            if(num%i) == 0:
                print(num, "is not a prime number.")
                break
        else:
            print(num, "is prime number!")
    else:
        print(num, "is not a prime number.")
        
   
with Pool(4) as p:
    print(p.map(check_prime, [100001777, 100003243, 100001777, 100001777, 100001777]))
    
    
#check_prime(100001777)
#check_prime(100003243)
