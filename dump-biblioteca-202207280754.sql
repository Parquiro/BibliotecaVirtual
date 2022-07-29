-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: localhost    Database: biblioteca
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.24-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `autor`
--

DROP TABLE IF EXISTS `autor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `autor` (
  `Aut_Id` tinyint(3) unsigned NOT NULL AUTO_INCREMENT,
  `Aut_Nombre` varchar(15) NOT NULL,
  `Aut_Apellido` varchar(15) NOT NULL,
  PRIMARY KEY (`Aut_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Entidad de autores.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autor`
--

LOCK TABLES `autor` WRITE;
/*!40000 ALTER TABLE `autor` DISABLE KEYS */;
/*!40000 ALTER TABLE `autor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genero`
--

DROP TABLE IF EXISTS `genero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `genero` (
  `Gen_Id` tinyint(3) unsigned NOT NULL AUTO_INCREMENT,
  `Gen_Nombre` varchar(30) NOT NULL,
  PRIMARY KEY (`Gen_Id`) USING BTREE,
  KEY `Cat_Genero` (`Gen_Nombre`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Entidad Categoria para libros.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genero`
--

LOCK TABLES `genero` WRITE;
/*!40000 ALTER TABLE `genero` DISABLE KEYS */;
/*!40000 ALTER TABLE `genero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libro`
--

DROP TABLE IF EXISTS `libro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libro` (
  `Lib_Id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Lib_Nombre` varchar(30) NOT NULL,
  `Lib_Editorial` varchar(30) NOT NULL,
  `Lib_NroPaginas` int(10) unsigned NOT NULL DEFAULT 0,
  `Lib_FPublicacion` date NOT NULL,
  `Lib_IdAutor` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY (`Lib_Id`),
  UNIQUE KEY `Lib_IdAutor` (`Lib_IdAutor`),
  KEY `Lib_Nombre` (`Lib_Nombre`),
  CONSTRAINT `FK_libro_autor` FOREIGN KEY (`Lib_IdAutor`) REFERENCES `autor` (`Aut_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Entidad de libros.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libro`
--

LOCK TABLES `libro` WRITE;
/*!40000 ALTER TABLE `libro` DISABLE KEYS */;
/*!40000 ALTER TABLE `libro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `librocategoria`
--

DROP TABLE IF EXISTS `librocategoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `librocategoria` (
  `Id_Libro` int(10) unsigned NOT NULL,
  `Id_Categoria` tinyint(3) unsigned NOT NULL,
  UNIQUE KEY `Id_Libro` (`Id_Libro`),
  UNIQUE KEY `Id_Categoria` (`Id_Categoria`),
  CONSTRAINT `FK_librocategoria_categoria` FOREIGN KEY (`Id_Categoria`) REFERENCES `genero` (`Gen_Id`),
  CONSTRAINT `FK_librocategoria_libro` FOREIGN KEY (`Id_Libro`) REFERENCES `libro` (`Lib_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Relacion entre entidades libro y categoria.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `librocategoria`
--

LOCK TABLES `librocategoria` WRITE;
/*!40000 ALTER TABLE `librocategoria` DISABLE KEYS */;
/*!40000 ALTER TABLE `librocategoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `librofavorito`
--

DROP TABLE IF EXISTS `librofavorito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `librofavorito` (
  `Id_Usuario` int(10) unsigned NOT NULL,
  `Id_Libro` int(10) unsigned NOT NULL,
  UNIQUE KEY `Id_Libro` (`Id_Libro`),
  UNIQUE KEY `Dni_Usuario` (`Id_Usuario`) USING BTREE,
  CONSTRAINT `FK_librofavorito_libro` FOREIGN KEY (`Id_Libro`) REFERENCES `libro` (`Lib_Id`),
  CONSTRAINT `FK_librofavorito_usuario` FOREIGN KEY (`Id_Usuario`) REFERENCES `usuario` (`Usu_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Relacion de Libro favorito entre entidad usuario y entidad libro.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `librofavorito`
--

LOCK TABLES `librofavorito` WRITE;
/*!40000 ALTER TABLE `librofavorito` DISABLE KEYS */;
/*!40000 ALTER TABLE `librofavorito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario` (
  `Usu_Id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Usu_Dni` int(10) unsigned NOT NULL,
  `Usu_Nombre` varchar(15) NOT NULL,
  `Usu_Apellido` varchar(15) NOT NULL,
  `Usu_Email` varchar(30) NOT NULL,
  `Usu_Password` varchar(300) NOT NULL,
  `Usu_Telefono` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`Usu_Id`),
  UNIQUE KEY `Usu_Dni` (`Usu_Dni`),
  UNIQUE KEY `Usu_Email` (`Usu_Email`),
  KEY `Usu_Password` (`Usu_Password`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='Entidad de usuarios.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,30749551,'Emmanuel','Cañate','emmanuelcanate@gmail.com','pbkdf2:sha256:260000$wOGOFXcavce043D2$2c5e9b5a17a338656a346e8ec2591fd017a36bc929c6fe28a3851fa81bf98e42','04146380056');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'biblioteca'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-28  7:54:10
