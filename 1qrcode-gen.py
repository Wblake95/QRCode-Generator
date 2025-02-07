#!/usr/bin/env python3

import sys
import argparse
from pathlib import Path

try:
    import validators
    import qrcode
    import pillow
except ImportError: 
    print("Possibly missing validators module")
    print("Possibly missing qrcode module")
    print("Possibly missing pillow module")
    sys.exit(1)

# Argparse template for stdin and stdout
parser = argparse.ArgumentParser()
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                    default=sys.stdin)
parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                    default=sys.stdout)
parser.parse_args(['input.txt', 'output.txt'])

def check_args(url):
    if validators.url(url): return True
    else: print("Your URL doesn't seem to be valid, please inpect it.")

# NOTE: implement this
#def create_qrcode(url,filename):