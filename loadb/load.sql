# HeidiSQL Dump 
#
# --------------------------------------------------------
# Host:                         127.0.0.1
# Database:                     load
# Server version:               5.0.27-community-nt
# Server OS:                    Win32
# Target compatibility:         ANSI SQL
# HeidiSQL version:             4.0
# Date/time:                    2024-03-04 15:36:26
# --------------------------------------------------------

/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ANSI,NO_BACKSLASH_ESCAPES';*/
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;*/


#
# Database structure for database 'load'
#

CREATE DATABASE /*!32312 IF NOT EXISTS*/ "load" /*!40100 DEFAULT CHARACTER SET latin1 */;

USE "load";


#
# Table structure for table 'cmt'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "cmt" (
  "cmtid" int(10) unsigned NOT NULL auto_increment,
  "name" varchar(50) default NULL,
  "comments" varchar(50) default NULL,
  PRIMARY KEY  ("cmtid")
);



#
# Dumping data for table 'cmt'
#

LOCK TABLES "cmt" WRITE;
/*!40000 ALTER TABLE "cmt" DISABLE KEYS;*/
REPLACE INTO "cmt" ("cmtid", "name", "comments") VALUES
	('2','DAISY','GOOD');
/*!40000 ALTER TABLE "cmt" ENABLE KEYS;*/
UNLOCK TABLES;


#
# Table structure for table 'data'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "data" (
  "userid" int(50) NOT NULL auto_increment,
  "name" varchar(50) default NULL,
  "mobile" varchar(50) default NULL,
  "email" varchar(50) default NULL,
  "data" varchar(50) default NULL,
  "date" varchar(50) default NULL,
  PRIMARY KEY  ("userid")
);



#
# Dumping data for table 'data'
#

LOCK TABLES "data" WRITE;
/*!40000 ALTER TABLE "data" DISABLE KEYS;*/
REPLACE INTO "data" ("userid", "name", "mobile", "email", "data", "date") VALUES
	(1,'Prem','08072620523','prem@gmail.com','rtfg','2024-02-28');
/*!40000 ALTER TABLE "data" ENABLE KEYS;*/
UNLOCK TABLES;


#
# Table structure for table 'req'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "req" (
  "enterid" varchar(50) default NULL,
  "content" varchar(50) default NULL,
  "request" varchar(500) default NULL
);



#
# Dumping data for table 'req'
#

LOCK TABLES "req" WRITE;
/*!40000 ALTER TABLE "req" DISABLE KEYS;*/
REPLACE INTO "req" ("enterid", "content", "request") VALUES
	('g','g','ghrt');
REPLACE INTO "req" ("enterid", "content", "request") VALUES
	('5','PROJECT','FGVSF');
/*!40000 ALTER TABLE "req" ENABLE KEYS;*/
UNLOCK TABLES;


#
# Table structure for table 'schedule'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "schedule" (
  "userid" text,
  "name" varchar(50) default NULL,
  "sch" varchar(50) default NULL
);



#
# Dumping data for table 'schedule'
#

LOCK TABLES "schedule" WRITE;
/*!40000 ALTER TABLE "schedule" DISABLE KEYS;*/
REPLACE INTO "schedule" ("userid", "name", "sch") VALUES
	('g','g','2024-02-26T05:14');
REPLACE INTO "schedule" ("userid", "name", "sch") VALUES
	('5','DAISY','2024-03-13T14:00');
REPLACE INTO "schedule" ("userid", "name", "sch") VALUES
	('1','gokul','2024-02-28T04:21');
/*!40000 ALTER TABLE "schedule" ENABLE KEYS;*/
UNLOCK TABLES;


#
# Table structure for table 'user'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "user" (
  "userid" int(10) unsigned NOT NULL auto_increment,
  "name" varchar(50) default NULL,
  "mobile" varchar(50) default NULL,
  "email" varchar(50) default NULL,
  "password" varchar(50) default NULL,
  "gender" varchar(50) default NULL,
  "date" varchar(50) default NULL,
  PRIMARY KEY  ("userid")
);



#
# Dumping data for table 'user'
#

LOCK TABLES "user" WRITE;
/*!40000 ALTER TABLE "user" DISABLE KEYS;*/
REPLACE INTO "user" ("userid", "name", "mobile", "email", "password", "gender", "date") VALUES
	('4','g','08072620523','g','g','male','2024-02-16');
REPLACE INTO "user" ("userid", "name", "mobile", "email", "password", "gender", "date") VALUES
	('5','DAISY','9773455355','DAISY@gmail.com','DAISY123','female','2024-02-28');
REPLACE INTO "user" ("userid", "name", "mobile", "email", "password", "gender", "date") VALUES
	('6','g','g','g','g','male','2024-02-28');
REPLACE INTO "user" ("userid", "name", "mobile", "email", "password", "gender", "date") VALUES
	('7','Prem','08072620523','prem@gmail.com','g','male','2024-02-28');
REPLACE INTO "user" ("userid", "name", "mobile", "email", "password", "gender", "date") VALUES
	('8','g','g','g','g','male','2024-03-02');
REPLACE INTO "user" ("userid", "name", "mobile", "email", "password", "gender", "date") VALUES
	('9','g','g','g','g','male','2024-03-29');
/*!40000 ALTER TABLE "user" ENABLE KEYS;*/
UNLOCK TABLES;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE;*/
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;*/
