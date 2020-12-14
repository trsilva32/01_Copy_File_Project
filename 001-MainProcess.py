#Import Libraries
import os
import time
import pandas as pd
from pandas.tseries.offsets import BDay
from ftplib import FTP

#Server Path
serverPath="File_Server_Path/" # path to collect files from

#Setup WD
WorkDirectory = "WorkingDirectory/" # path of this file is saved
os.chdir(serverPath+WorkDirectory)
os.getcwd()

#Import Functions
from Functions import * # Import Functions from the functions.py 

#Global Variables
procDate = pd.datetime.today() - BDay(1) # Get last Business day Date
procDate = procDate.strftime('%Y%m%d')

# ================================================================================================
# Files from Network Folder ---> Copy it to your processing folder 
# ================================================================================================

fromPath=serverPath+"From_Folder/"
toPath=serverPath+"To_Folder"
listFiles=["List of files to be copied from the From_Folder"]

print("--- Copying files ---> ", fromPath,' to ', toPath ) 
startTime = time.time() # variable to controles time spent copying files
CopyFiles(fromPath,toPath,listFiles)
RenameFiles(toPath,listFiles)
ZipFiles(toPath, procDate) # Save file on Processing Date Folder
endTime = time.time() # variable to controles time spent copying files
timer(startTime,endTime) # Spent time
with open(serverPath+WorkDirectory+'log.txt', 'a') as logFile: # Log file   
    logFile.write("\nProcessing Date: " + pd.datetime.today().strftime('%d/%m/%Y %H:%M:%S') + \
                  " --> File Name " + timer(startTime,endTime))

# ================================================================================================
# Files FTP Server 
# ================================================================================================
toPath=serverPath+"To_Folder"
fileName = open(toPath+procDate+"_Files.TXT",'wb') # File New Name

print("--- Downloading FTP File ---")
startTime = time.time() # variable to controles time spent copying files
# FTP Config
ftp = FTP('serverIP')
ftp.login(user='Usuário',passwd='Senha')

# Download File
ftp.retrbinary("RETR 'File_Name_FTP_Server'", fileName.write ,1024)
ftp.quit()
fileName.close()
ZipFiles(toPath, procDate) # Save file on Processing Date Folder

endTime = time.time() # variable to controles time spent copying files
timer(startTime,endTime) # Spent time
with open(serverPath+WorkDirectory+'log.txt', 'a') as logFile: # Log File
    logFile.write("\nData Processamento: " + pd.datetime.today().strftime('%d/%m/%Y %H:%M:%S') + \
                  " --> FTP File " + timer(startTime,endTime))
