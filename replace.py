# -*- coding: utf-8 -*-

import re
import fileinput
from sys import *

import os


def replace(filename, pattern, replacement, regex=False):
    """Repalce the selected contents of the file with either
    regular expressions, or a traditional find and replace"""

    if regex:
        replace_regex(filename, pattern, replacement)
    else:
        replace_normal(filename, pattern, replacement)


def replace_regex(filename, pattern, replacement):
    """use regular expressoions to replace selected contents of the file"""
    #Consider repalcing this with fileinput methods below, they seem suprerior
    #maybe test using 'w+' as the open mode???
    #get a file descriptor
    fd = open(filename, 'r')

    #get string data from file
    data = fd.read()
    #close file descriptor
    fd.close()

    # use the regualar expressions package to replace the desired pattern
    data = (re.sub(pattern, replacement, data))
    print(data)

    #write the new file contents back to the original file
    #fd = open(file, 'w')

    #write the data back to the file
    #fd.wr(data)
    #fd.close()


def replace_normal(filename, pattern, replacement):
    """use replace selected contents of the file using
    traditional search and replace"""
    for line in fileinput.input(filename, inplace=True):
        print((line.replace(pattern, replacement).rstrip()))
    fileinput.input().close()

#def replaceInFiles(path, condition, pattern, replacement, useRegEx):
#    for
#


#def isTestfile(filename):
#    return filename == "test.txt"


def get_files(path, targetname):
    file_list = []
    for root, dirs, files in os.walk(path):
        if targetname in files:
            file_list.append((os.path.join(root, targetname)))
    return file_list


def replace_all(path, filename, pattern, replacement):
    files = get_files(path, filename)
    for f in files:
        replace_regex(f, pattern, replacement)
