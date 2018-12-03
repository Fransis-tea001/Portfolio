#BinaryConverter By Atip Earth

import os
import sys

print("---Binary converter program Start---")
print("Decimal to Binary : 1\nBinary to Decimal : 2\nExit : 3")

def BnD(Binum):
    #Trasform Bibary num into array
    B = Binum
    lB = str(B)
    listBi = []
    for digit in lB:
        listBi.append(int(digit))
    #print(listBi)

    #Calculate in array
    i = (len(listBi))
    ic = int(i)-1
    ls = []
    while ic >= 0:
        ls.append(2**ic)
        ic = ic-1
    #print(ls)

    count = 0
    indez = int(i)-1
    Result = []
    while count <= indez:
        Result.append(listBi[count]*ls[count])
        count = count+1
    #print(Result)

    #Answer calculation
    total = 0
    for v in Result:
        total = total + v
    print("Result is : ",end="")
    print(total)

def DnB(Dnum):
    Result = []
    D = Dnum
    while True:
        Rmd = D % 2
        Result.append(int(Rmd))
        D = int(D/2)
        if D == 0:
            break
    print("Result is : ",end='')
    for R in reversed(Result):
        print(R,end='')
    print("")


programSelect = str(input("Type program you want to start or exit : "))

if programSelect == '1' :
    while True:
        print("Pls Enter Decimal number to convert ",end='')
        num = input("or press 'e' to exit : ")
        if num == 'e':
            os.system("clear")
            sys.exit(0)
        else:
            DnB(int(num))
            print("Press 'c' to continue convert",end='')
            con1 = input("or press '3' to exit : ")
            if con1 == '3':
                os.system("clear")
                sys.exit(0)
            elif con1 == 'c':
                os.system("clear")

elif programSelect == '2' :
    while True:
        print("Pls Enter Binary number to convert",end='')
        bi = input(" or press 'e' to exit : ")
        if bi == 'e':
            os.system("clear")
            sys.exit(0)
        else:
            BnD(int(bi))
            print("Press 'c' to continue convert",end='')
            con1 = input("or press '3' to exit : ")
            if con1 == '3':
                os.system("clear")
                sys.exit(0)
            elif con1 == 'c':
                os.system("clear")
            

elif programSelect == '3':
    print("---Exit program---")
    sys.exit(0)

else :
    print("Error")



