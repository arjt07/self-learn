# Packages -> Third-Party Libraries
# Python's Package Manager -> pip
# pip is a program that allows to install packages on our devices by just running a program

import cowsay
import sys

if len(sys.argv) == 2:
    
    # can pass one String only
    cowsay.cow("hello, " + sys.argv[1]) 
    cowsay.trex("hello, " + sys.argv[1]) 
    
 








