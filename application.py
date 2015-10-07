"""capitals and cities"""
# -*- coding: utf-8 -*-
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from collections import OrderedDict
import sys
import os
import getpass
import smtplib
ONEDICTIONARY = {} #all(capials and contries)
LISTONE = [] #countries
LISTTWO = [] #capitalsta

def rent():
    """"This function checks whether or not to enter more \
    information about countries and capitals"""
    print u"╔═══════════════════════════════════╗"
    print u"║   Do you want to re-enter? y/n:   ║"
    print u"╚═══════════════════════════════════╝"
    reent = raw_input("")
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
    """This function save the information"""
    cleaner()
    tor = True
    while tor == True:
        print u"╔═════════════════════╗"
        print u"║   Insert country:   ║"
        print u"╚═════════════════════╝"
        countri = raw_input("")
        if str(countri).isalpha() == True or " " in countri or "ñ" in countri or "á" \
            in countri or "é" in countri or "í" in countri or "ó" in countri or "ú" in countri:
            countri = countri.title()

            LISTONE.append(countri)
            tor = False
        else:
            print u"╔═════════════════════════════════════╗"
            print u"║   Unrecognized option. Try again:   ║"
            print u"╚═════════════════════════════════════╝"
            tor = True
    whil = True
    while whil == True:
        print u"╔═════════════════════╗"
        print u"║   Insert capital:   ║"
        print u"╚═════════════════════╝"
        capi = raw_input("")
        if str(capi).isalpha() == True or " " in capi or "ñ" in capi or "á" in capi or "é" \
            in capi or "í" in capi or "ó" in capi or "ú" in capi:
            capi = capi.title()
            LISTTWO.append(capi)
            whil = False
        else:
            print u"╔═════════════════════════════════════╗"
            print u"║   Unrecognized option. Try again:   ║"
            print u"╚═════════════════════════════════════╝"
            whil = True
            cleaner()
    ONEDICTIONARY[countri] = capi
    rent()

def countries():
    """This function diisplay the list of countries"""
    cleaner()
    print u"╔═════════════════════╗"
    print u"║     Country list    ║"
    print u"╚═════════════════════╝"
    for i in LISTONE:
        print " ", i.ljust(15, " ")
    print u"╚═════════════════════╝"

    raw_input("press enter to continue")
    cleaner()
    menu()

def capitals():
    """This function diisplay the list of countries"""
    cleaner()
    print u"╔═════════════════════╗"
    print u"║    Capitals list    ║"
    print u"╚═════════════════════╝"
    for i in LISTTWO:
        print " ", i.ljust(15, " ")
    print u"╚═════════════════════╝"
    raw_input("press enter to continue")
    cleaner()
    menu()

def cleaner():
    """this function clean the screen"""
    os.system("cls")
    os.system("clear")

def alone():
    """This function diisplay the list of countries and capitals"""
    cleaner()
    print u"╔════════════════════════════════════╗"
    print u"║Country~~~~~~~~~~~~~~~~~~~~~Capitals║"
    for i in ONEDICTIONARY:
        print u"║", i.ljust(15, " "), "║", ONEDICTIONARY[i].rjust(15, " "), " ║"
    print u"╚════════════════════════════════════╝"
    raw_input("press enter to continue")
    cleaner()
    menu()

def allordered():
    """This function diisplay the list of countries and capitals ordered"""
    ordered = OrderedDict(sorted(ONEDICTIONARY.items(), key=lambda x: x[1:]))
    print u"╔════════════════════════════════════╗"
    print u"║Country~~~~~~~~~~~~~~~~~~~~~Capitals║"
    for key, value in ordered.items():
        print u"║", key.ljust(15, " "), " ║", value.rjust(15, " "), " ║"
    print u"╚════════════════════════════════════╝"
    raw_input("Press Enter to Continue")
    cleaner()
    menu()

def mail():
    """This function send the mail"""
    cleaner()
    print "Send email by gmail"

    fromaddr = raw_input("Count from gmail: ")
    password = getpass.getpass("Password: ")
    toaddrs = raw_input("to: ")
    #asunto = raw_input("subject, from message: ")
    body = "Country\t  ~~~~~~~\tCapitals\n"
    for msg in ONEDICTIONARY:
        body = body + str(msg).center(15, " ") +str(ONEDICTIONARY[msg]).center(40, " ") + "\n"
    msg = MIMEMultipart()
    msg['From'] = fromaddr #This saves the mail of the sender
    msg['To'] = toaddrs  #This saves the mail of the receiver
    msg['Subject'] = "Countries and Capitals"  #This saves the subject
    msg.attach(MIMEText(body, 'plain')) #This saves the message

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddrs, text)
        server.quit()
        print "Your message has been sent"
        raw_input("press enter to continue...")
        menu()
    except smtplib.SMTPAuthenticationError:
        print "Error. Your username or password is incorrect"
        raw_input("press enter to continue...")
        mail()
def initializing():
    """function of initializing"""
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

def finishing():
    """this function"""
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
    sys.exit()
def menu():
    """diisplay menu"""
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
    opcion = raw_input("ingrese una opcion: ")
    opcion = opcion.lower()
    if opcion == "1" or opcion == "country":
        country()
    elif opcion == "2" or opcion == "countries":
        countries()
    elif opcion == "3" or opcion == "capitals":
        capitals()
    elif opcion == "4" or opcion == "all":
        alone()
    elif opcion == "5" or opcion == "allordered":
        allordered()
    elif opcion == "6" or opcion == "mail":
        mail()
    elif opcion == "7" or opcion == "exit":
        finishing()
        quit()
    else:
        print u"╔═════════════════════════════════════╗"
        print u"║   Unrecognized option. Try again:   ║"
        print u"║       press enter to continue       ║"
        print u"╚═════════════════════════════════════╝"
        raw_input("")
        cleaner()
        menu()

menu()

