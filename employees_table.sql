USE prashanta;
DROP TABLE IF EXISTS employees;
CREATE TABLE employees (id INT, first_name VARCHAR(20), last_name VARCHAR(30));
INSERT INTO employees (id, first_name, last_name) VALUES (1, 'John', 'Doe');
INSERT INTO employees (id, first_name, last_name) VALUES (2, 'Bob', 'Smith');
INSERT INTO employees (id, first_name, last_name) VALUES (3, 'Jane', 'Doe');
SELECT * FROM employees;

/* working below */
/* LOAD DATA LOCAL INFILE 'C:/Translink/region.csv' INTO TABLE region FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS; */

/*
C:\Program Files\MySQL\MySQL Server 5.7\bin>mysqldump -u root -pPs268848@  prashanta > C:/sql/backup-file.sql
mysqldump: [Warning] Using a password on the command line interface can be insecure.

**********************************************************************************************************************************************/

/*

C:\Program Files\MySQL\MySQL Server 5.7\bin>mysqlimport --ignore-lines=1 --fields-terminated-by="," --fields-enclosed-by="\"" --lines-terminated-by="\n" --local --user root -p prashanta C:\Translink\\region.csv
Enter password: *********
prashanta.region: Records: 4062  Deleted: 0  Skipped: 0  Warnings: 579

**********************************************************************************************************************************/
/* https://michaelrigart.be/export-directly-mysql-csv/
SELECT field1, field2
FROM table1
INTO OUTFILE '/path/to/file.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
FIELDS ESCAPED BY '\'
LINES TERMINATED BY '\n';
*/

SELECT * FROM employees INTO OUTFILE 'C:/sql/cars.csv'
FIELDS TERMINATED BY ',';