-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: wittyDBName
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `blc`
--

DROP TABLE IF EXISTS `blc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blc` (
  `bid` int DEFAULT NULL,
  `lid` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blc`
--

LOCK TABLES `blc` WRITE;
/*!40000 ALTER TABLE `blc` DISABLE KEYS */;
/*!40000 ALTER TABLE `blc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blt`
--

DROP TABLE IF EXISTS `blt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blt` (
  `bid` int DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blt`
--

LOCK TABLES `blt` WRITE;
/*!40000 ALTER TABLE `blt` DISABLE KEYS */;
/*!40000 ALTER TABLE `blt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brlt`
--

DROP TABLE IF EXISTS `brlt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brlt` (
  `cid` int NOT NULL AUTO_INCREMENT,
  `bid` int NOT NULL,
  `rid` int NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brlt`
--

LOCK TABLES `brlt` WRITE;
/*!40000 ALTER TABLE `brlt` DISABLE KEYS */;
/*!40000 ALTER TABLE `brlt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `catID` int NOT NULL AUTO_INCREMENT,
  `category` varchar(255) NOT NULL,
  PRIMARY KEY (`catID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'abortion'),(2,'crime and cops'),(3,'labor and workers'),(4,'other'),(5,'trans');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lst`
--

DROP TABLE IF EXISTS `lst`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lst` (
  `lid` int DEFAULT NULL,
  `sum` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lst`
--

LOCK TABLES `lst` WRITE;
/*!40000 ALTER TABLE `lst` DISABLE KEYS */;
INSERT INTO `lst` VALUES (0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(33,0),(34,0),(35,0),(36,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0),(44,0),(45,0),(46,0),(47,0),(48,0),(49,0),(50,0);
/*!40000 ALTER TABLE `lst` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reason_category_connect`
--

DROP TABLE IF EXISTS `reason_category_connect`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reason_category_connect` (
  `rccid` int NOT NULL AUTO_INCREMENT,
  `rid` int NOT NULL,
  `catId` int NOT NULL,
  PRIMARY KEY (`rccid`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reason_category_connect`
--

LOCK TABLES `reason_category_connect` WRITE;
/*!40000 ALTER TABLE `reason_category_connect` DISABLE KEYS */;
INSERT INTO `reason_category_connect` VALUES (1,47,5),(2,46,5),(3,45,5),(4,44,5),(5,43,5),(6,42,5),(7,41,5),(8,40,5),(9,39,5),(10,38,5),(11,37,5),(12,36,5),(13,35,5),(14,34,5),(15,33,5),(16,32,5),(17,31,5),(18,30,5),(19,29,5),(20,28,5),(21,27,5),(22,26,5),(23,25,5),(24,24,5),(25,23,5),(26,22,5),(27,21,5),(28,20,5),(29,19,5),(30,18,5),(31,17,4),(32,16,4),(33,15,4),(34,14,3),(35,13,4),(36,12,3),(37,11,2),(38,10,2),(39,9,2),(40,8,2),(41,7,2),(42,6,1),(43,5,1),(44,4,1),(45,3,1),(46,2,1),(47,1,1);
/*!40000 ALTER TABLE `reason_category_connect` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reasons`
--

DROP TABLE IF EXISTS `reasons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reasons` (
  `rid` int NOT NULL AUTO_INCREMENT,
  `reason` varchar(255) NOT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reasons`
--

LOCK TABLES `reasons` WRITE;
/*!40000 ALTER TABLE `reasons` DISABLE KEYS */;
INSERT INTO `reasons` VALUES (1,'born alive'),(2,'born-alive'),(3,'terminate'),(4,'abortion'),(5,'mifepristone'),(6,'conception'),(7,'organized retail crime'),(8,'law enforcement'),(9,'police'),(10,'officer'),(11,'protect and serve'),(12,'union'),(13,'unions'),(14,'social security'),(15,'education'),(16,'race'),(17,'error'),(18,'gender ideology'),(19,'gender'),(20,'parental rights'),(21,'parent rights'),(22,'parent\'s rights'),(23,'transgender'),(24,'predator'),(25,'groomer'),(26,'grooming'),(27,'biological'),(28,'drag'),(29,'adult oriented'),(30,'sexualize'),(31,'sexualizing'),(32,'cross-sex'),(33,'nonbinary'),(34,'non binary'),(35,'non-binary'),(36,'reassignment'),(37,'pronouns'),(38,'puberty blockers'),(39,'puberty-blockers'),(40,'gender transition'),(41,'indecency'),(42,'birth'),(43,'name'),(44,'women\'s bill of rights'),(45,'bathroom'),(46,'preferred'),(47,'family');
/*!40000 ALTER TABLE `reasons` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-05 10:37:56
