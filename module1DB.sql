CREATE DATABASE  IF NOT EXISTS `module1` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `module1`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: module1
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `CatID` int NOT NULL,
  `CatName` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`CatID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment` (
  `CommentID` int NOT NULL,
  `PostID` int NOT NULL,
  `CommentContent` text,
  `UserCode` int NOT NULL,
  `LikeCmtCNT` int DEFAULT NULL,
  `C_CreateDate` datetime DEFAULT NULL,
  `C_UpdateDate` datetime DEFAULT NULL,
  PRIMARY KEY (`CommentID`),
  KEY `PostID` (`PostID`),
  KEY `UserCode` (`UserCode`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`PostID`) REFERENCES `post` (`PostID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`UserCode`) REFERENCES `user` (`UserCode`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delete_comment`
--

DROP TABLE IF EXISTS `delete_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delete_comment` (
  `DeleteCommentID` int NOT NULL,
  `CommentID` int NOT NULL,
  `Delete_cFlag` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`DeleteCommentID`),
  KEY `CommentID` (`CommentID`),
  CONSTRAINT `delete_comment_ibfk_1` FOREIGN KEY (`CommentID`) REFERENCES `comment` (`CommentID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delete_comment`
--

LOCK TABLES `delete_comment` WRITE;
/*!40000 ALTER TABLE `delete_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `delete_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delete_post`
--

DROP TABLE IF EXISTS `delete_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delete_post` (
  `DeletePostID` int NOT NULL,
  `PostID` int NOT NULL,
  `Delete_pFlag` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`DeletePostID`),
  KEY `PostID` (`PostID`),
  CONSTRAINT `delete_post_ibfk_1` FOREIGN KEY (`PostID`) REFERENCES `post` (`PostID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delete_post`
--

LOCK TABLES `delete_post` WRITE;
/*!40000 ALTER TABLE `delete_post` DISABLE KEYS */;
/*!40000 ALTER TABLE `delete_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post` (
  `PostID` int NOT NULL,
  `UserCode` int NOT NULL,
  `PostTitle` varchar(255) DEFAULT NULL,
  `PostContent` text,
  `CatID` int NOT NULL,
  `LikeCNT` int DEFAULT NULL,
  `ViewCNT` int DEFAULT NULL,
  `P_CreateDate` datetime DEFAULT NULL,
  `P_UpdateDate` datetime DEFAULT NULL,
  PRIMARY KEY (`PostID`),
  KEY `UserCode` (`UserCode`),
  KEY `CatID` (`CatID`),
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`UserCode`) REFERENCES `user` (`UserCode`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `post_ibfk_2` FOREIGN KEY (`CatID`) REFERENCES `category` (`CatID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `UserCode` int NOT NULL,
  `UserID` varchar(20) DEFAULT NULL,
  `UserPW` varchar(20) DEFAULT NULL,
  `UserName` varchar(20) DEFAULT NULL,
  `SignUpDate` datetime DEFAULT NULL,
  `is_admin` tinyint DEFAULT NULL,
  `deleted_uFlag` tinyint DEFAULT NULL,
  PRIMARY KEY (`UserCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'module1'
--

--
-- Dumping routines for database 'module1'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-12 11:03:18
