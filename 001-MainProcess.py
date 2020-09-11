# -*- coding: utf-8 -*-
"""
VS Code - Project
Projeto: Copiar 

Este é um arquivo de script temporário.
"""

#Import Libraries
import os
import time
import pandas as pd
from pandas.tseries.offsets import BDay
from ftplib import FTP

#Server Path
serverPath="File_Server_Path" # incluir o caminho do servidor de arquivos

#Setup WD
WorkDirectory = "WorkingDirectory" # incluir o diretório onde o projeto será salvo
os.chdir(serverPath+WorkDirectory)
os.getcwd()

#Import Functions
from Functions import *

#Global Variables
procDate = pd.datetime.today() - BDay(1) 
procDate = procDate.strftime('%Y%m%d')

# ================================================================================================
# Files from directory IT
# ================================================================================================

fromPath=serverPath+"Arquivos_TI/"
toPath=serverPath+"Caminho_onde_será salvo os arquivos baixados"
listFiles=["lista de arquivos ou formato de arquivos a serem baixados"]

print("--- Copying files ---")
startTime = time.time()
CopyFiles(fromPath,toPath,listFiles)
RenameFiles(toPath,listFiles)
ZipFiles(toPath, procDate)
endTime = time.time()
timer(startTime,endTime)
with open(serverPath+WorkDirectory+'log.txt', 'a') as logFile:    
    logFile.write("\nData Processamento: " + pd.datetime.today().strftime('%d/%m/%Y %H:%M:%S') + \
                  " --> Nome Arquivo " + timer(startTime,endTime))

# ================================================================================================
# GCA Files FTP Server files 
# ================================================================================================
toPath=serverPath+"Onde salvar os arquivos"
fileName = open(toPath+procDate+"_Files.TXT",'wb')

print("--- Copying files ---")
startTime = time.time()
# FTP Config
ftp = FTP('serverIP')
ftp.login(user='Usuário',passwd='Senha')

# Download File
ftp.retrbinary("RETR 'Nome arquivo servidor FTP'", fileName.write ,1024)
ftp.quit()
fileName.close()
ZipFiles(toPath, procDate)

endTime = time.time()
timer(startTime,endTime)
with open(serverPath+WorkDirectory+'log.txt', 'a') as logFile:    
    logFile.write("\nData Processamento: " + pd.datetime.today().strftime('%d/%m/%Y %H:%M:%S') + \
                  " --> FTP File " + timer(startTime,endTime))
