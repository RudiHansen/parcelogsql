/*************************************
*Author..: Rudi Hansen <rsh@obtain.dk>
*Purpose.: Create Database for ParceLogSql
*Used by.: Admins
*Version.: 1.00
**************************************/
-- CREATE USER 'parcelog' IDENTIFIED BY '';
-- GRANT ALL PRIVILEGES ON parceLogSql.* TO 'parcelog';

CREATE USER 'rsh'@'obtain' IDENTIFIED BY '';
GRANT ALL ON *.* TO 'rsh'@'RSH-PC';

-- CREATE USER 'rsh'@'x1-6-04-a1-51-d4-08-da.cpe.webspeed.dk' IDENTIFIED BY 'grasslin';
-- GRANT ALL ON *.* TO 'rsh'@'x1-6-04-a1-51-d4-08-da.cpe.webspeed.dk';
FLUSH PRIVILEGES;
