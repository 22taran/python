#!/usr/bin/env python3

import webbrowser

import sys

if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
webbrowser.open('http://www.google.com/maps/place/' +address)
