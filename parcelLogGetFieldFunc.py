#!/usr/bin/python
# coding=utf-8

# Beskrivelse af hvad koden gør.
# 
import parcelLogSqlFunc
from ipwhois import IPWhois
from pprint import pprint
from datetime import datetime

# Function definition is here
def getDate( line ):
    pos1 = line.find("[") + 1
    pos2 = line.find(":",pos1)
    retStr = line[pos1:pos2]
    retStr = retStr.replace('Jan','01')
    retStr = retStr.replace('Feb','02')
    retStr = retStr.replace('Mar','03')
    retStr = retStr.replace('Apr','04')
    retStr = retStr.replace('May','05')
    retStr = retStr.replace('Jun','06')
    retStr = retStr.replace('Jul','07')
    retStr = retStr.replace('Aug','08')
    retStr = retStr.replace('Sep','09')
    retStr = retStr.replace('Okt','10')
    retStr = retStr.replace('Oct','10')
    retStr = retStr.replace('Nov','11')
    retStr = retStr.replace('Dec','12')

    day    = retStr[0:2]
    month  = retStr[3:5]
    year   = retStr[6:10]
    retStr = year + "/" + month + "/" + day
    return retStr

def getTime( line ):
    pos1 = line.find("[") + 1;
    pos1 = line.find(":",pos1) + 1
    pos2 = pos1 + 8
    retStr = line[pos1:pos2]
    return retStr

def getTimeZone( line ):
    pos1 = line.find("+")
    pos2 = pos1 + 5
    retStr = line[pos1:pos2]
    return retStr

def getFileName(line):
    methods = ["GET", "POST"]  # List of HTTP methods to check
    pos1 = -1
    
    for method in methods:
        pos1 = line.find(method)
        if pos1 != -1:  # If method is found, adjust position and break
            pos1 += len(method) + 1
            break
    
    pos2 = line.find("HTTP")
    
    if pos1 > 0 and pos2 > pos1:
        return line[pos1:pos2].strip()
    else:
        return ""

def getIp( line ):
    pos1 = 0
    pos2 = line.find("-") - 1
    retStr = line[pos1:pos2]
    return retStr
    
def getWhoIs(ipAdress):
    if(ipAdress == "::1" or ipAdress == "127.0.0.1" or "192.168.0." in ipAdress or "192.168.1." in ipAdress):
        return ("","","Blank")

    countryCode = ""
    description = ""
    lookUpType  = ""
    cacheData = parcelLogSqlFunc.sqlGetIpWhoIsCache(ipAdress)
    if cacheData:
        lookUpType  = "Cache"
        countryCode = cacheData[0]
        description = cacheData[1]
    else:
        lookUpType  = "WhoIs"
        obj = IPWhois(ipAdress)
        try:
            timerStart = datetime.now()
            results = obj.lookup_rdap()
            timerEnd = datetime.now()
            with open("output.txt", "a") as text_file:
                text_file.write("{0} Lookup ip {1}\n".format((timerEnd-timerStart),ipAdress))
            countryCode = results['asn_country_code']
            description = results['asn_description']
            if description is None:
                description = ""
        except Exception as e:
            countryCode = ""
            description = "Lookup error"
            print ("ERR - ip %s failed"%ipAdress)

        description = description[:70]
        parcelLogSqlFunc.sqlSaveWhoIdCache(ipAdress,countryCode,description)

    return (countryCode,description,lookUpType)
