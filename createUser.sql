/*************************************
*Author..: Rudi Hansen <rsh@obtain.dk>
*Purpose.: Create Database for ParceLogSql
*Used by.: Admins
*Version.: 1.00
**************************************/
-- CREATE USER 'parcelog' IDENTIFIED BY '';
-- GRANT ALL PRIVILEGES ON parceLogSql.* TO 'parcelog';
CREATE USER 'rsh'@'RSH-PC' IDENTIFIED BY '';
GRANT ALL ON *.* TO 'rsh'@'RSH-PC';
FLUSH PRIVILEGES;
