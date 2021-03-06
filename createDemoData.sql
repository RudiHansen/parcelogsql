/*************************************
*Author..: Rudi Hansen <rsh@obtain.dk>
*Purpose.: Create tables for ParceLogSql
*Used by.: Admins
*Version.: 1.00
**************************************/
USE parceLogSql;
INSERT INTO LogTable
    (LogDate,LogTime,TimeZone,Country,WhoIS,IpAddress,FileName)
VALUES
	('2017/08/18','05:39:27','+0200','KR','SK Broadband Co Ltd','116.126.102.227','/uploads/AxDynManager/AxDynManagerV1.03.zip'),
	('2017/08/19','16:53:46','+0200','US','Yahoo! Inc.','68.180.229.225','/uploads/DevCreate/DevCreateV1.06.zip'),
	('2017/08/22','01:24:57','+0200','NL','Advanced Hosters B.V.','46.229.168.69','/uploads/RUHAExportUtilElements/5.0/Class_RUHAExportUtilElements.xpo'),
	('2017/08/22','01:25:27','+0200','NL','Advanced Hosters B.V.','46.229.168.76','/uploads/RUHAExportUtilElements/Class_RUHAExportUtilElements_V01_06.xpo'),
	('2017/08/22','01:25:34','+0200','NL','Advanced Hosters B.V.','46.229.168.66','/uploads/RUHAExportUtilElements/6.0/Class_RUHAExportUtilElements.xpo'),
	('2017/08/23','06:21:52','+0200','US','Yahoo! Inc.','68.180.229.225','/uploads/AxDynManager/AxDynManagerV1.02.zip'),
	('2017/08/24','21:39:52','+0200','US','Yahoo! Inc.','68.180.229.225','/uploads/RUHAExportUtilElements/5.0/Class_RUHAExportUtilElements.xpo'),
	('2017/08/30','10:38:25','+0200','US','Yahoo! Inc.','68.180.229.225','/uploads/DevCreate/DevCreateV1.05.zip'),
	('2017/09/05','15:13:26','+0200','NL','Advanced Hosters B.V.','46.229.168.72','/uploads/RUHAExportUtilElements/5.0/Class_RUHAExportUtilElements.xpo'),
	('2017/09/05','15:13:44','+0200','NL','Advanced Hosters B.V.','46.229.168.75','/uploads/RUHAExportUtilElements/Class_RUHAExportUtilElements_V01_06.xpo'),
	('2017/09/05','15:14:08','+0200','NL','Advanced Hosters B.V.','46.229.168.66','/uploads/RUHAExportUtilElements/6.0/Class_RUHAExportUtilElements.xpo'),
	('2017/09/15','10:19:15','+0200','DK','','193.219.27.230','/uploads/AxDynManager/AxDynManagerV1.03.zip');
