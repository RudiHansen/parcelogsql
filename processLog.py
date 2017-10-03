#!/usr/bin/python
# coding=utf-8

# Løber igennem poster i RawFileData og opretter udfra dem de korrekte poster i andre log tabeller.
import parcelLogSqlFunc
import parcelLogGetFieldFunc
import warnings
from datetime import datetime

fileType    = 'apache2'
newLines    = 0

# Main code
warnings.filterwarnings("ignore")
sessionId = parcelLogSqlFunc.sqlRawFileData_getSessionId(fileType)
print ("Start processLog {0}".format(datetime.now()))

while(sessionId > 0):
    timerStart = datetime.now()
    logLines = parcelLogSqlFunc.sqlRawFileData_getNewLines(fileType,sessionId)
    numLines = len(logLines)
    print ("Processing {0} lines from sessionId {1}".format(numLines,sessionId))

    for logLine in logLines:
        date                        = parcelLogGetFieldFunc.getDate(logLine[0])
        time                        = parcelLogGetFieldFunc.getTime(logLine[0])
        timeZone                    = parcelLogGetFieldFunc.getTimeZone(logLine[0])
        fileName                    = parcelLogGetFieldFunc.getFileName(logLine[0])
        ipAddress                   = parcelLogGetFieldFunc.getIp(logLine[0])
        (country,whoIs,lookUpType)  = parcelLogGetFieldFunc.getWhoIs(ipAddress)
        if(ipAddress != "188.182.160.189" and ipAddress != "127.0.0.1" and ipAddress != "192.168.0.1"):
            parcelLogSqlFunc.sqlSaveLogTable(date,time,timeZone,fileName,ipAddress,country,whoIs,logLine[0])
            newLines = newLines + 1

        if(0):
            tmpStr = logLine[0]
            tmpStr = tmpStr.replace('\n', '')
            print tmpStr
            print ("Logdata - date (%s) - time (%s) - timeZone (%s) - ip (%s)"%(date,time,timeZone,ipAddress))
            print ("Logdata - filename (%s)"%fileName)
            print ("Logdata - country (%s) - whoIs (%s) - lookUpType (%s)"%(country,whoIs,lookUpType))
            print ("")
            raw_input("Press Enter to continue...")
    timerEnd = datetime.now()
    print ("{0} Time for sessionId {1}".format((timerEnd-timerStart),sessionId))
    sessionId = parcelLogSqlFunc.sqlRawFileData_getSessionId(fileType)

if(newLines > 0):
    print ("Added {0} new lines.".format(numLines))
print ("End processLog {0}".format(datetime.now()))