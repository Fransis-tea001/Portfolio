#PasswordGenerator Program

import os
import sys
import string
import random
import time
from time import sleep

os.system('clear')

print("---Start Password Generator Program---")

ingredt1 = "abcdefghijklmnopqrstuvwzyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789#!&"

while True:
    
    programSelect = input("1.Generate password\n2.Exit\nEnter : ")

    if programSelect == '1':
        os.system('clear')
        passlenght = int(input("1.Please Enter the lenght of your pass word\nEnter : "))
        print(''.join(random.sample(ingredt1, passlenght)))

    elif programSelect == '2':
        print("---Exit Program---")
        time.sleep(2)
        os.system('clear')
        sys.exit(0)