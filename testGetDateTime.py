#!/usr/bin/python
# coding=utf-8

# Løber igennem poster i RawFileData og opretter udfra dem de korrekte poster i andre log tabeller.
import parcelLogSqlFunc
import parcelLogGetFieldFunc
import warnings
from datetime import datetime

#logLine     = '::1 - - [18/Sep/2017:15:15:46 +0200] "OPTIONS * HTTP/1.0" 200 126 "-" "Apache/2.4.18 (Ubuntu) (internal dummy connection)"'
#logLine     = '212.237.134.149 - - [24/Sep/2017:13:31:59 +0200] "GET /apple-touch-icon.png HTTP/1.1" 404 518 "-" "MobileSafari/602.1 CFNetwork/811.5.4 Darwin/16.7.0"'
logLine     = '222.239.76.119 - - [22/Sep/2017:07:47:04 +0200] "GET /manager/html HTTP/1.1" 404 452 "-" "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)'
# Main code
date                        = parcelLogGetFieldFunc.getDate(logLine)
time                        = parcelLogGetFieldFunc.getTime(logLine)
fileName                    = parcelLogGetFieldFunc.getFileName(logLine)

print ("Start processLog {0}".format(datetime.now()))
print date
print time
print fileName
