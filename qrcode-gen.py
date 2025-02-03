#!/usr/bin/env python3

import sys, path

try: import validators
except: print("Couldn't import package: validators. Please install and try again")

# NOTE: try import qrcode-library
# NOTE: try import pillows-library


def check_args(url):
    if validators.url(url): return True
    else: print("Your URL doesn't seem to be valid, please inpect it.")

# NOTE: implement this
#def create_qrcode(url,filename):


# Check for input and execute
# NOTE: see if there is a standard
if not sys.stdin.isatty(): # Check if tty and has data
    print(1)
    #create_qrcode(sys.stdin.read().rstrip())

# NOTE: move to argparse, since it is standard
elif len(sys.argv) == 2: # Only one argument
    if check_args(sys.argv[1]):
        print(2)
        #create_qrcode()

elif len(sys.argv) == 3: # Only two arguments
    if check_args(sys.argv[1]):
        print(3)
        #create_qrcode()
    # fix error printing from check_args running twice
    #elif check_args(sys.argv[2]):print(4)
    #    #create_qrcode()

else:
    print("Too many arguments")
