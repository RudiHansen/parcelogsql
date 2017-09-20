/*************************************
*Author..: Rudi Hansen <rsh@obtain.dk>
*Purpose.: Shrink database and logfile
*Used by.: Admins
*Version.: 1.00
**************************************/
USE parceLogSql;
SELECT * FROM LogTable;
SELECT * FROM RawFileData;
SELECT * FROM SessionIdTable;
