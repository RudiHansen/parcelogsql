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
						  SessionId INT,
						  FileType VARCHAR(50),
						  FileLine VARCHAR(2000));

DROP TABLE SessionIdTable;
CREATE TABLE SessionIdTable (SessionType VARCHAR(30),
							 NextSessionId INT);						  