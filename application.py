# -*- coding: utf-8 -*-
import time
from collections import OrderedDict
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import sys
import os
import getpass
import smtplib
onedictionary={}
listone=[] #countries
listtwo=[] #capitals
def rent():
    print u"╔═══════════════════════════════════╗"
    print u"║   Do you want to re-enter? y/n:   ║"
    print u"╚═══════════════════════════════════╝"
    reent=raw_input("")
    reent = reent.lower()
    if reent == "y":
        country()
    elif reent == "n":
        menu()
    else:
        print u"╔═════════════════════════════════════╗"
        print u"║   Unrecognized option. Try again:   ║"
        print u"║       press enter to continue       ║"
        print u"╚═════════════════════════════════════╝"
        raw_input("")
        rent()
def country():
    cleaner()
    tor = True
    while tor == True:
        print u"╔═════════════════════╗"
        print u"║   Insert country:   ║"
        print u"╚═════════════════════╝"
        countri = raw_input("")
        if str(countri).isalpha() == True or " " in countri:
            countri = countri.title()

            listone.append(countri)
            tor = False
        else:
            print u"╔═════════════════════════════════════╗"
            print u"║   Unrecognized option. Try again:   ║"
            print u"╚═════════════════════════════════════╝"
            tor=True
    vr = True
    while vr == True:
        print u"╔═════════════════════╗"
        print u"║   Insert capital:   ║"
        print u"╚═════════════════════╝"
        capi = raw_input("")
        if str(capi).isalpha() == True or " " in capi:
            capi = capi.title()
            listtwo.append(capi)
            vr = False
        else:
            print u"╔═════════════════════════════════════╗"
            print u"║   Unrecognized option. Try again:   ║"
            print u"╚═════════════════════════════════════╝"
            vr = True
            cleaner()
    onedictionary [countri] = capi
    rent()
def countries():
    cleaner() 
    print u"╔═════════════════════╗"
    print u"║     Country list    ║"
    print u"╚═════════════════════╝"
    for i in listone:
        print " ",i.ljust(15, " ")
    print u"╚═════════════════════╝"

    raw_input("press enter to continue")
    cleaner()
    menu()
def capitals():
    cleaner()
    print u"╔═════════════════════╗"
    print u"║    Capitals list    ║"
    print u"╚═════════════════════╝"
    for i in listtwo:
        print " ", i.ljust(15, " ")
    print u"╚═════════════════════╝"
    raw_input("press enter to continue")
    cleaner()
    menu()
def cleaner():
    os.system("cls")
    os.system("clear")
def al():
    cleaner()
    print u"╔════════════════════════════════════╗"
    print u"║Country~~~~~~~~~~~~~~~~~~~~~Capitals║"
    for i in onedictionary:
        print u"║", i.ljust(15, " "),"║", onedictionary[i].rjust(15, " ")," ║"
    print u"╚════════════════════════════════════╝"
    raw_input("press enter to continue")
    cleaner()
    menu()
def allordered():
    ordered = OrderedDict(sorted(onedictionary.items(), key=lambda x: x[1:]))
    print u"╔════════════════════════════════════╗"
    print u"║Country~~~~~~~~~~~~~~~~~~~~~Capitals║"
    for key, value in ordered.items():
        print u"║",key.ljust(15, " "),"║",value.rjust(15, " ")," ║"
    print u"╚════════════════════════════════════╝"    
    raw_input("Press Enter to Continue")
    cleaner()
    menu()
def mail():
    cleaner()
    print "Send email by gmail"

    fromaddr = raw_input("Count from gmail: ")
    password = getpass.getpass("Password: ")
    toaddrs = raw_input("to: ")
    #asunto = raw_input("subject, from message: ")
    body = "Country\t  ~~~~~~~\tCapitals\n"
    for msg in onedictionary:
        body = body + str(msg).center(15, " ") +str(onedictionary[msg]).center(40," ") + "\n" 
    msg = MIMEMultipart()
    msg['From'] = fromaddr #This saves the mail of the sender
    msg['To'] = toaddrs  #This saves the mail of the receiver
    msg['Subject'] = "Countries and Capitals"  #This saves the subject
    msg.attach(MIMEText(body, 'plain')) #This saves the message

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(fromaddr,password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddrs, text)
        server.quit()
        print "Your message has been sent"
        raw_input("press enter to continue...")
        menu()
    except (smtplib.SMTPAuthenticationError):
        print "Error. Your username or password is incorrect"
        raw_input("press enter to continue...")
        mail()

def exit():
    sys.exit()
def menu():
    cleaner()
    print"=> 5%"
    time.sleep(0.25)
    cleaner()
    print"==> 20%"
    time.sleep(0.25)
    cleaner()
    print"====> 40%"
    time.sleep(0.25)
    cleaner()
    print"======> 60%"
    time.sleep(0.25)
    cleaner()
    print"========> 80%"
    time.sleep(0.25)
    cleaner()
    print"=========> 100%"
    time.sleep(0.25)
    cleaner()
    print "                   COUNTRIES AND CAPITALS                    "
    print u"╔══════════════════════════════════════════════════════════╗"
    print u"║                       1.country                          ║"
    print u"║                       2.countries                        ║"
    print u"║                       3.capitals                         ║"
    print u"║                       4.all                              ║"
    print u"║                       5.allOrdere                        ║"
    print u"║                       6.Mail                             ║"
    print u"║                       7.EXIT                             ║"
    print u"╚══════════════════════════════════════════════════════════╝"
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
    elif opcion == "6" or opcion == "mail":
        mail()
    elif opcion== "7" or opcion == "exit":
        print "The program is closing..."
        time.sleep(1)
        cleaner()
        print" please wait..."
        time.sleep(0.25)
        cleaner()
        print"=> 5%"
        time.sleep(0.25)
        cleaner()
        print"==> 20%"
        time.sleep(0.25)
        cleaner()
        print"====> 40%"
        time.sleep(0.25)
        cleaner()
        print"======> 60%"
        time.sleep(0.25)
        cleaner()
        print"========> 80%"
        time.sleep(0.25)
        cleaner()
        print"=========> 100%"
        time.sleep(0.25)
        cleaner()
        print"program is being restored"
        time.sleep(1)
        cleaner()
        print"BYE!"
        time.sleep(1)
        cleaner()
        exit()
    else:
        print u"╔═════════════════════════════════════╗"
        print u"║   Unrecognized option. Try again:   ║"
        print u"║       press enter to continue       ║"
        print u"╚═════════════════════════════════════╝"
        raw_input("")
        cleaner()
        menu() 
menu()