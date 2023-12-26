CREATE DATABASE  IF NOT EXISTS `mydata` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mydata`;
-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: mydata
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `gamesystem`
--

DROP TABLE IF EXISTS `gamesystem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gamesystem` (
  `member` varchar(40) NOT NULL,
  `refnumber` varchar(45) NOT NULL,
  `username` varchar(45) NOT NULL,
  `firstname` varchar(45) DEFAULT NULL,
  `lastname` varchar(45) DEFAULT NULL,
  `userid` varchar(45) DEFAULT NULL,
  `region` varchar(45) DEFAULT NULL,
  `platform` varchar(45) DEFAULT NULL,
  `serialnumber` varchar(45) DEFAULT NULL,
  `title` varchar(45) DEFAULT NULL,
  `publisher` varchar(45) DEFAULT NULL,
  `releasedate` varchar(45) DEFAULT NULL,
  `version` varchar(45) DEFAULT NULL,
  `lastupdate` varchar(45) DEFAULT NULL,
  `futureupdate` varchar(45) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`refnumber`,`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gamesystem`
--

LOCK TABLES `gamesystem` WRITE;
/*!40000 ALTER TABLE `gamesystem` DISABLE KEYS */;
INSERT INTO `gamesystem` VALUES ('','','','','','','','','','','','','','','',''),('First timer','0001','Berry_SNG','Berry','SNG','5123','Indian Subcontinent','MacOS','TURBO1','Minecraft','Mojang','18 November 2011','1.17.1','June 8 2021','December 2021','26.95$'),('Normal','0002','Turbocycle_Demo','Turbocycle','Demo','6179','Europe','XBOX One','Turbo2','Grand Theft Auto 5','Rockstar Games','17-09-2013','To be filled','To be filled','To be filled','30$'),('Admin','0003','Turbocycle','Snehal','Ray','21056','Asia','XBOX One','TURBO1','Minecraft','Mojang','18 November 2011','1.17.1','June 8 2021','December 2021','26.95$'),('First timer','0004','aaa','aaa','bbb','123','Europe','XBOX One','Turbo7','Sims 4','EA Games','2-9-2014','Sims 411 Recap','6-8-2021','Not announced','360$ with all expansions'),('MVP++','1000','abc','Snehal ','Ray','1901','Europe','Windows','TURBO1','Minecraft','Mojang','18 November 2011','1.17.1','June 8 2021','December 2021','26.95$');
/*!40000 ALTER TABLE `gamesystem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-29  1:51:00
