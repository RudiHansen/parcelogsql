#!/usr/bin/python
# coding=utf-8

# Beskrivelse af hvad koden gør.
# 

import mysql.connector
import glob
import gzip

# Function definition is here
def getFileList(filepath):
    filelist = glob.glob(filepath)
    filelist.sort()
    return filelist

def readFile(filename):
    dataLines = []
    inputfile = open(filename)

    for line in inputfile:
        if line.find("GET") > 0:
            fileName = getFileName(line)
            if fileName.find("uploads") > 0:
                dataLines.append(line)

    inputfile.close()
    return dataLines

def readFileGz(filename):
    dataLines = []
    inputfile=gzip.open(filename,'rb')

    for line in inputfile:
        if line.find("GET") > 0:
            fileName = getFileName(line)
            if fileName.find("uploads") > 0:
                dataLines.append(line)

    inputfile.close()
    return dataLines

def getFileName( line ):
    pos1 = line.find("GET") + 4
    pos2 = line.find("HTTP")
    retStr = line[pos1:pos2]
    return retStr

def sqlSaveArrayToRawFileData(fileName,array):
    for line in array:
        if len(line) > 1100:
            print fileName
            print line
            print len(line)
            raw_input("Press Enter to continue...")
        else:
            sqlInsert(fileName,line)
    
def sqlInsert(fileName,fileLine):
    cnx = mysql.connector.connect(user='parcelog', database='parceLogSql')
    cursor = cnx.cursor()

    add_RawFileData = ("INSERT INTO RawFileData (FileName, FileLine) VALUES (%s, %s)")
    data_RawFileData = (fileName, fileLine)
                   
    # Insert RawFileData
    cursor.execute(add_RawFileData, data_RawFileData)

    # Make sure data is committed to the database
    cnx.commit()
    cursor.close()
    cnx.close()
    return ""