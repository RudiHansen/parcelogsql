#!/usr/bin/python
# coding=utf-8

# Beskrivelse af hvad koden gør.
# 

import parcelLogSqlFunc
filesearchpath     = '/var/log/apache2/access*'


# Main code

# Get all fileNames to read
fileNames = parcelLogSqlFunc.getFileList(filesearchpath)
print len(fileNames)
fileNames += parcelLogSqlFunc.getFileList('/home/rsh/python/parcelogsql/old1/access*')
print len(fileNames)
fileNames += parcelLogSqlFunc.getFileList('/home/rsh/python/parcelogsql/old2/access*')
print len(fileNames)
raw_input("Press Enter to continue...")

# Read all data from logfiles.
for fileName in fileNames:
	print fileName
	dataLines = []
	if fileName.find(".gz") > 0:
		dataLines = parcelLogSqlFunc.readFileGz(fileName)
		if len(dataLines) > 0:
			parcelLogSqlFunc.sqlSaveArrayToRawFileData(fileName,dataLines)
	else:
		dataLines = parcelLogSqlFunc.readFile(fileName)
		if len(dataLines) > 0:
			parcelLogSqlFunc.sqlSaveArrayToRawFileData(fileName,dataLines)

			