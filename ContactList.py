import os
import sys

print("---Start ContactList Program---")

contactlist = {}

def addContact(name,phoneN):
    contactlist.update({name:phoneN})

def deleteContact(name):
    contactlist.pop(name)

while True:
    print("1.Add contact\n2.Delete contact\n3.Show all contact\n4.Exit Program")
    programSelect = input("Enter number of program you want to start : ")

    if programSelect == '1':
        os.system('clear')
        while True:
            name = str(input("Enter contact name : "))
            phoneN = str(input("Enter Phone number : "))
            addContact(name,phoneN)

            con = input("Add more contact? (Y/N) : ")
            if con == 'Y':
                os.system('clear')
            elif con == 'N':
                break
    
    elif programSelect == '2':
        while True:
            nameDel = input("Enter contact name you want to delete : ") 
            if not nameDel in contactlist:
                print(nameDel+"not avalible in your contact")
            elif nameDel in contactlist:
                deleteContact(nameDel)
            else:
                print("Error")
            
            con = input("Delete another contact? (Y/N) : ")
            if con == 'Y':
                os.system('clear')
            elif con == 'N':
                break

    elif programSelect == '3':
        os.system('clear')
        for Lname in contactlist:
            print(Lname ,contactlist[Lname])
        print("Press Enter to back to menu")
        


    elif programSelect == '4':
        os.system('clear')
        sys.exit(0)

    else:
        print("Error")
        os.system('clear')
        