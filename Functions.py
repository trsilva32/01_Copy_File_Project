# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:22:28 2019

@author: tiagcon
"""

# Libraries
from datetime import datetime,timedelta
import os
import os.path
import glob
import shutil
import zipfile

# Functions
## Function to check time running process
def timer(startTime,endTime):
    hours, rem =divmod(endTime-startTime,3600)
    minutes, seconds = divmod(rem,60)
    #print("--- Tempo de Processamento : " + "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds) + " ---" )
    procTime="--- Tempo de Processamento : " + "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds) + " ---"
    return procTime
        
## Funcition to copy file from to a place
def CopyFiles(fromPath,toPath,listFiles):
    for fileName in listFiles:
        fullFileName = os.path.join(fromPath, fileName)
        if os.path.isfile(fullFileName):
            shutil.copy2(fullFileName, toPath)
    
## Function to Rename files with date
def RenameFiles(toPath,listFiles):
    for fileName in os.listdir(toPath):                   
        if fileName in listFiles:
            src=toPath+fileName
            t = os.path.getmtime(toPath+fileName)
            v = datetime.fromtimestamp(t)-timedelta(days=1)
            x = v.strftime('%Y%m%d')
            novoNome = toPath + x + "_" + fileName
            os.rename(src,novoNome)

    
## Function to list of files
def ZipFiles(toPath, procDate):
    listFiles = [os.path.basename(x) for x in glob.glob(toPath + procDate + "_*")]  
    with zipfile.ZipFile(toPath + procDate + '.zip', 'w', compression=zipfile.ZIP_DEFLATED) as myZip:
        for fileName in os.listdir(toPath):
            if fileName in listFiles:
                myZip.write(os.path.join(toPath,fileName),fileName)
                os.remove(toPath + fileName)