#!/usr/bin/python
# coding=utf-8

# Beskrivelse af hvad koden gør.
# 

import mysql.connector
import glob
import gzip
from datetime import datetime, timedelta

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
    timerStart = datetime.now()
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
    timerEnd = datetime.now()
    with open("Output.txt", "a") as text_file:
        text_file.write("{0} GetNextSessionId {1}\n".format((timerEnd-timerStart),nextSessionId))
    return nextSessionId

def sqlRawFileData_getSessionId(fileType):
    timerStart = datetime.now()
    sessionId = 0
    cnx = mysql.connector.connect(user='parcelog', database='parceLogSql')
    cursor = cnx.cursor()
    
    query = ("SELECT SessionId from RawFileData WHERE FileType = '%s' AND LineRead = 0 ORDER BY SessionId LIMIT 1"%fileType)

    cursor.execute(query)

    data = cursor.fetchone()
    if data:
        sessionId = data[0]
        
    cursor.close()
    cnx.close()    
    timerEnd = datetime.now()
    with open("Output.txt", "a") as text_file:
        text_file.write("{0} sqlRawFileData_getSessionId {1}\n".format((timerEnd-timerStart),fileType))
    return sessionId

def sqlRawFileData_getNewLines(fileType,sessionId):
    timerStart = datetime.now()
    cnx = mysql.connector.connect(user='parcelog', database='parceLogSql')
    cursor = cnx.cursor()
    
    query = ("SELECT FileLine from RawFileData WHERE FileType = '%s' AND SessionId = %s AND LineRead = 0"%(fileType,sessionId))
    cursor.execute(query)
    data = cursor.fetchall()
    
    query = ("UPDATE RawFileData SET LineRead = 1 WHERE FileType = '%s' AND SessionId = %s AND LineRead = 0"%(fileType,sessionId))
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()    
    timerEnd = datetime.now()
    with open("Output.txt", "a") as text_file:
        text_file.write("{0} sqlRawFileData_getNewLines {1}\n".format((timerEnd-timerStart),sessionId))
    return data

def sqlGetIpWhoIsCache(ipAddress):
    timerStart = datetime.now()
    cnx = mysql.connector.connect(user='parcelog', database='parceLogSql')
    cursor = cnx.cursor()
    cacheDate = datetime.today() - timedelta(days=7) 

    query = ("SELECT Country, WhoIS from IpWhoIsCache WHERE IpAddress = '%s' AND CacheDate >= '%s'"%(ipAddress,cacheDate.strftime('%Y-%m-%d %H:%M:%S')))
    cursor.execute(query)

    data = cursor.fetchone()
    
    cursor.close()
    cnx.close()    
    timerEnd = datetime.now()
    with open("Output.txt", "a") as text_file:
        text_file.write("{0} sqlGetIpWhoIsCache {1}\n".format((timerEnd-timerStart),ipAddress))
    return data
    
def sqlSaveWhoIdCache(ipAddress,country,whoIs):
    timerStart = datetime.now()
    cnx = mysql.connector.connect(user='parcelog', database='parceLogSql')
    cursor = cnx.cursor()
    cacheDate = datetime.today()

    if(len(whoIs) > 70):
        print ("SQL PROBLEM length of WhoId exceeds 70 chars it is %s chars long"%len(whoIs))
        print whoIs
        return ""

    query = ("INSERT INTO IpWhoIsCache (CacheDate, Country, WhoIS, IpAddress) "
             "VALUES ('%s','%s','%s','%s')"%(cacheDate.strftime('%Y-%m-%d %H:%M:%S'),country,whoIs,ipAddress))
    cursor.execute(query)

    cnx.commit()
    cursor.close()
    cnx.close()    
    timerEnd = datetime.now()
    with open("Output.txt", "a") as text_file:
        text_file.write("{0} sqlSaveWhoIdCache {1}\n".format((timerEnd-timerStart),ipAddress))

def sqlSaveLogTable(date,time,timeZone,fileName,ipAddress,country,whoIs):
    timerStart = datetime.now()
    cnx = mysql.connector.connect(user='parcelog', database='parceLogSql')
    cursor = cnx.cursor()
    cacheDate = datetime.today()
    fileName = fileName.replace("'", "")
    query = ("INSERT IGNORE INTO LogTable (LogDate, TimeZone, Country, WhoIS, IpAddress, FileName) "
             "VALUES ('%s %s','%s','%s','%s','%s','%s')"%(date,time,timeZone,country,whoIs,ipAddress,fileName))

    try:
        cursor.execute(query)
    except Exception as e:
        print query
        raise        
        quit()


    cnx.commit()
    cursor.close()
    cnx.close()    
    timerEnd = datetime.now()
    with open("Output.txt", "a") as text_file:
        text_file.write("{0} sqlSaveLogTable {1}\n".format((timerEnd-timerStart),ipAddress))
