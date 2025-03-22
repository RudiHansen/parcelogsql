#!/usr/bin/python
# coding=utf-8

# Læser de logfiler der skal overvåges ind i SQL RawFileData tabellen.
import parcelLogSqlFunc
from datetime import datetime
fileType            = 'apache2'
filesearchpath      = '/var/log/apache2/access*'
print ("Start readLogFiles {0}".format(datetime.now()))
# Main code

# Get all fileNames to read
fileNames = parcelLogSqlFunc.getFileList(filesearchpath)
#fileNames += parcelLogSqlFunc.getFileList('/home/rsh/python/parcelogsql/old1/access*')
#fileNames += parcelLogSqlFunc.getFileList('/home/rsh/python/parcelogsql/old2/access*')

# Delete the RawDataTable
# parcelLogSqlFunc.sqlDeleteRawFileData()

# Read all data from logfiles.
for fileName in fileNames:
    dataLines = []
    print("Read file {0}".format(fileName))
    if fileName.find(".gz") > 0:
        dataLines = parcelLogSqlFunc.readFileGz(fileName)
        if len(dataLines) > 0:
            nextSessionId = parcelLogSqlFunc.sqlGetNextSessionId("RawFileData")
            parcelLogSqlFunc.sqlSaveArrayToRawFileData(nextSessionId,fileType,dataLines)
    else:
        dataLines = parcelLogSqlFunc.readFile(fileName)
        if len(dataLines) > 0:
            nextSessionId = parcelLogSqlFunc.sqlGetNextSessionId("RawFileData")
            parcelLogSqlFunc.sqlSaveArrayToRawFileData(nextSessionId,fileType,dataLines)

print ("End readLogFiles {0}".format(datetime.now()))