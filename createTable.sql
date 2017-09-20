/*************************************
*Author..: Rudi Hansen <rsh@obtain.dk>
*Purpose.: Create tables for ParceLogSql
*Used by.: Admins
*Version.: 1.00
**************************************/
USE parceLogSql;
DROP TABLE LogTable;
CREATE TABLE LogTable (LogDate 		DATE, 
					   LogTime 		TIME, 
					   TimeZone 	VARCHAR(5), 
					   Country 		VARCHAR(30), 
					   WhoIS 		VARCHAR(30), 
					   IpAddress 	VARCHAR(30),
					   FileName		VARCHAR(255));


DROP TABLE RawFileData;
CREATE TABLE RawFileData (LineRead BOOL,
						  FileName VARCHAR(50),
						  FileLine VARCHAR(1100));