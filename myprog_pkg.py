#!/usr/bin/python

from my_pkg.BinToOther import *
from my_pkg.UnandInter import *

while(True):


    selection =int(input("Select menu : 1)Conversion 2)union/intersection 3)exit ?"))
    if(selection == 1):
        num = int(input("input binary number :"),2)
        Oct(num)
        Dec(num)  
        Hex(num)
        continue
    if(selection == 2):
        func()
        continue

    else:
        print("exit the program...")
        break
                



