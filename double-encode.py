#!/usr/bin/python
#Double Encoding Script by bus7dz

import binascii
from termcolor import colored

def doubleencode():

    global string   

    string=binascii.b2a_hex(string)
    print colored("HEX ENCODED>>>>>>","red"),colored(string,"yellow")   
    percent="%25"
    result=percent.join(string[i:i+2] for i in range(0,len(string),2))
    result=percent+result

    print colored("DOUBLE-ENCODED>>>>>","red"),colored(result,"green")
    print "REMINDER : %252E%252E%252F<>../ "

while 1:

    string=raw_input("Enter your string to double-encode here>>>>>>>")

    doubleencode()
