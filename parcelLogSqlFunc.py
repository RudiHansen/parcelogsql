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
        dataLines.append(line)

    inputfile.close()
    return dataLines

def readFileGz(filename):
    dataLines = []
    inputfile=gzip.open(filename,'rb')

    for line in inputfile:
        dataLines.append(line)

    inputfile.close()
    return dataLines

def getFileName( line ):
    pos1 = line.find("GET") + 4
    pos2 = line.find("HTTP")
    retStr = line[pos1:pos2]
    return retStr

def sqlSaveArrayToRawFileData(nextSessionId,fileType,array):
    for line in array:
        if len(line) > 2000:
            print fileName
            print line
            print len(line)
            raw_input("Press Enter to continue...")
        else:
            sqlInsertRawFileData(nextSessionId,fileType,line)
    
def sqlInsertRawFileData(nextSessionId,fileType,fileLine):
    cnx = mysql.connector.connect(user='parcelog', database='parceLogSql')
    cursor = cnx.cursor()

    add_RawFileData = ("INSERT INTO RawFileData (LineRead, SessionId, FileType, FileLine) VALUES (%s, %s, %s, %s)")
    data_RawFileData = (0, nextSessionId, fileType, fileLine)
                   
    # Insert RawFileData
    cursor.execute(add_RawFileData, data_RawFileData)

    # Make sure data is committed to the database
    cnx.commit()
    cursor.close()
    cnx.close()
    return ""
	
def sqlDeleteRawFileData():
    cnx = mysql.connector.connect(user='parcelog', database='parceLogSql')
    cursor = cnx.cursor()

    add_RawFileData = ("DELETE FROM RawFileData")
                   
    # Insert RawFileData
    cursor.execute(add_RawFileData)

    # Make sure data is committed to the database
    cnx.commit()
    cursor.close()
    cnx.close()
    return ""

def sqlGetNextSessionId(sessionType):
    nextSessionId = 1;
    cnx = mysql.connector.connect(user='parcelog', database='parceLogSql')
    cursor = cnx.cursor()

    query = ("SELECT NextSessionId from SessionIdTable WHERE SessionType = '%s'"%sessionType)

    cursor.execute(query)

    data = cursor.fetchone()
    if data:
        nextSessionId = data[0]
        update_SessionIdTable = ("UPDATE SessionIdTable SET NextSessionId = %s WHERE SessionType = '%s'" % (nextSessionId+1,sessionType))
        cursor.execute(update_SessionIdTable)
    else:
        add_SessionIdTable = ("INSERT INTO SessionIdTable (SessionType, NextSessionId) VALUES (%s, %s)")
        data_SessionIdTable = (sessionType, nextSessionId+1)
        cursor.execute(add_SessionIdTable, data_SessionIdTable)
    
    cnx.commit()
    cursor.close()
    cnx.close()    
    return nextSessionId
