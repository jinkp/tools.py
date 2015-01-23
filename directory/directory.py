# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 17:42:28 2015

@author: Joel Keb
"""

import os

class Directory:
    
    def __init__(self):
        self.directories=[]
        self.files=[]
    
    def getListDirectory(self,directory):
        if not directory:
            return  "Parameter Directory Empty"    
            
        if(os.path.isdir(directory)):
            for file in os.listdir(directory):
                if(os.path.isdir(os.path.join(directory,file))):            
                    self.directories.append(os.path.join(directory,file));
                                    
        else:
            return "Directory Not Found"        
            
        return self.directories;
                
                
    def getListFilesDirectory(self,directory):
        if not directory:
            return  "Parameter Directory Empty"    
            
        if(os.path.isdir(directory)):
            for file in os.listdir(directory):
                if(os.path.isfile(os.path.join(directory,file))):            
                    self.files.append(os.path.join(directory,file));
                                    
        else:
            return "Files Not Found"        
            
        return self.files;        
        
    def getListOnlyExtension(self,directory,extensions):        
        if (not directory) or (not extensions):
            return "Check The Parameters"
        if(os.path.isdir(directory)):
            for file in os.listdir(directory):
                if(os.path.isdir(os.path.join(directory,file))):
                    continue
                            
                name,extension = os.path.splitext(file)                       
                if (extension in extensions):
                    self.files.append(os.path.join(directory,file))
                
        else:
            return "Directory Not Found"
        
        return self.files;
        
    def getListDirectoryByDate(self):
        print ""
    
    def getListFilesByDate(self):
        print ""
    
    def getListAllDirectory(self):
        print ""
    
    def getListAllFileDirectory(self):
        print ""

    def getListAllOnlyExtension(self):
        print ""

    
        