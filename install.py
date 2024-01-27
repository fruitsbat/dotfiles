#!/usr/bin/python

import os

try:
    print("making symlink for fish")
    os.symlink("./fish", "../")
except:
    print("symlink for fish already exists")
