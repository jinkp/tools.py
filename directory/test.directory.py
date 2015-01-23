# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 17:51:54 2015

@author: Joel Keb
"""

from directory import *

oDirectory = Directory()

#listDirectories = oDirectory.getListDirectory("c:\\");
#listFiles = oDirectory.getListFilesDirectory("c:\\");
extensions = [".mp4"]
listFiles = oDirectory.getListOnlyExtension("c:\\",extensions);
print listFiles