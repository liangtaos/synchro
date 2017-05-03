#!/usr/bin/python
#coding:utf-8
from optparse import OptionParser
import sys, os
#parser = OptionParser()
parser = OptionParser("Usage: %prog [file1] [file2]...")
parser.add_option("-c", 
                  "--chars",		
 		  dest="characters",
	          action="store_true",
         	  default=False,
		  help="only count characters",)
parser.add_option("-w",
		"--words",
		dest="words",
		action="store_true",
		default=False,
		help="only count words",)
parser.add_option("-l",
		"--lines",
		dest="lines",
		action="store_true",
		default=False,
		help="only count lines",)
#options, args = parser.parse_args()

if __name__ == '__main__':
    options, args = parser.parse_args()
    print options
    print args
