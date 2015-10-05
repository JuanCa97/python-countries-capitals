import time
import sys
import os
onedictionary={}
listone=[] #countries
listtwo=[] #capitals


def rent():
    reent=raw_input("Do you want to re-enter? y/n: ")
    reent = reent.lower()
    if reent == "y":
        country()
    elif reent == "n":
        menu()
    else:
        print"Unrecognized option. Try again"
        raw_input("press enter to continue")
        rent()


def country():
    cleaner()
    tor = True
    while tor == True:
        countri=raw_input("Insert country: ")
        if str(countri).isalpha() == True or " " in countri:
            listone.append(countri)
            tor=False
        else:
            print"Unrecognized option. Try again"
            tor=True
    vr=True
    while vr==True:
        capi=raw_input("Insert capital:")
        if str(capi).isalpha() == True or " " in capi:
            listtwo.append(capi)
            vr=False
        else:
            print"Unrecognized option. Try again"
            vr=True
            cleaner()
    onedictionary [countri] = capi
    cleaner()
    rent()


def countries():
    cleaner()
    print"################"
    print"# Country list #"
    print"################"
    for i in listone:
        print i.title()
    raw_input("press enter to continue")
    cleaner()
    menu()
def capitals():
    cleaner()
    print"#################"
    print"# Capitals list #"
    print"#################"
    for i in listtwo:
        print i.title()
    raw_input("press enter to continue")
    cleaner()
    menu()
def cleaner():
    os.system("cls")
    os.system("clear")
def al():
    cleaner()
    for i in onedictionary:
        print"Country               Capitals"
        print i.title(),"--","               ", onedictionary[i].title()
    raw_input("press enter to continue")
    cleaner()
    menu()

#def allordered():

def exit():
    sys.exit()

def menu():
    cleaner()
    print"############################################################"
    print"#                        1.country                         #"
    print"#                       2.countries                        #"
    print"#                       3.capitals                         #"
    print"#                          4.all                           #"
    print"#                      5.allOrdered                        #"
    print"#                         6.EXIT                           #"
    print"############################################################"
    opcion= raw_input("ingrese una opcion: ")
    opcion = opcion.lower()
    if opcion == "1" or opcion == "country":
        country()
    elif opcion == "2" or opcion == "countries":
        countries()
    elif opcion == "3" or opcion == "capitals":
        capitals()
    elif opcion == "4" or opcion == "all":
        al()
    elif opcion == "5" or opcion == "allordered":
        allordered()
    elif opcion== "6" or opcion == "exit":
        print "The program is closing..."
        time.sleep(2)
        cleaner()
        print" please wait..."
        time.sleep(0.5)
        cleaner()
        print"=> 5%"
        time.sleep(0.5)
        cleaner()
        print"==> 20%"
        time.sleep(0.5)
        cleaner()
        print"====> 40%"
        time.sleep(0.5)
        cleaner()
        print"======> 60%"
        time.sleep(0.5)
        cleaner()
        print"========> 80%"
        time.sleep(0.5)
        cleaner()
        print"=========> 100%"
        time.sleep(0.5)
        cleaner()
        print"program is being restored"
        time.sleep(2)
        cleaner()
        print"BYE!"
        exit()
    else:
        print "Unrecognized option. Try again"
        raw_input("press enter to continue")
        cleaner()
        menu() 
menu()