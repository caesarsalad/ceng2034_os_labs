#!/usr/bin/python3
import os, threading

def ping(hostname):
    os.system("ping -c 3 " + hostname)

def check_prime(num):
    print("checking prime... ", num)
    if num >1:
        for i in range(2,num):
            if(num%i) == 0:
                print(num, "is not a prime number.")
                break
        else:
            print(num, "is prime number!")
    else:
        print(num, "is not a prime number.")
    
#check_prime(100001777)
#check_prime(100003243)


thread1 = threading.Thread(target=check_prime, args=(100001777,))
thread2 = threading.Thread(target=check_prime, args=(100003243,))

thread1.start()
thread2.start()

'''
ping('google.ca')
ping('github.com')
'''
'''
thread1 = threading.Thread(target=ping, args=("google.ca",))
thread2 = threading.Thread(target=ping, args=("github.com",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("the END")
'''
