#!/usr/bin/python
# coding=utf-8

# Læser de logfiler der skal overvåges ind i SQL RawFileData tabellen.
import parcelLogSqlFunc
fileType            = 'apache2'
filesearchpath      = '/var/log/apache2/access*'

# Main code

# Get all fileNames to read
fileNames = parcelLogSqlFunc.getFileList(filesearchpath)
#fileNames += parcelLogSqlFunc.getFileList('/home/rsh/python/parcelogsql/old1/access*')
#fileNames += parcelLogSqlFunc.getFileList('/home/rsh/python/parcelogsql/old2/access*')

# Delete the RawDataTable
# parcelLogSqlFunc.sqlDeleteRawFileData()

# Read all data from logfiles.
for fileName in fileNames:
    print fileName
    dataLines = []
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
