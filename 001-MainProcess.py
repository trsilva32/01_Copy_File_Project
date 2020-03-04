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
serverPath="//ZEUS/CONTROLES_INTERNOS_BI$/"

#Setup WD
WorkDirectory = "19-DataManagement/002-Projetos/012-FileManagement/"
os.chdir(serverPath+WorkDirectory)
os.getcwd()

#Import Functions
from Functions import *

#Global Variables
procDate = pd.datetime.today() - BDay(1) 
procDate = procDate.strftime('%Y%m%d')

# ================================================================================================
# Suitability Files
# ================================================================================================

fromPath=serverPath+"Arquivos TI/"
toPath=serverPath+"19-DataManagement/000-ArquivosFonte/00-Suitability/"
listFiles=["Nota_Risco.txt","PERF-INV.TXT","SUIT_REL_CLIE.TXT",
              "SUIT_REL_CLIE_DECLARACAO.TXT","SUIT_TERMOS_PLAN.TXT"]

print("--- Copying Suitability files ---")
startTime = time.time()
CopyFiles(fromPath,toPath,listFiles)
RenameFiles(toPath,listFiles)
ZipFiles(toPath, procDate)
endTime = time.time()
timer(startTime,endTime)
with open(serverPath+WorkDirectory+'log.txt', 'a') as logFile:    
    logFile.write("\nData Processamento: " + pd.datetime.today().strftime('%d/%m/%Y %H:%M:%S') + \
                  " --> Suitability " + timer(startTime,endTime))

# ================================================================================================
# GCA Files
# ================================================================================================
toPath=serverPath+"19-DataManagement/000-ArquivosFonte/01-GCA/"
fileName = open(toPath+procDate+"_GCA.TXT",'wb')

print("--- Copying GCA files ---")
startTime = time.time()
# FTP Config
ftp = FTP('172.16.8.250')
ftp.login(user='tiagcon',passwd='ts201912')

# Download File
ftp.retrbinary("RETR 'GCA.PS312.SEXPB532(0)'", fileName.write ,1024)
ftp.quit()
fileName.close()
ZipFiles(toPath, procDate)

endTime = time.time()
timer(startTime,endTime)
with open(serverPath+WorkDirectory+'log.txt', 'a') as logFile:    
    logFile.write("\nData Processamento: " + pd.datetime.today().strftime('%d/%m/%Y %H:%M:%S') + \
                  " --> GCA " + timer(startTime,endTime))