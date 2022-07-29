/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE IF NOT EXISTS `biblioteca` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `biblioteca`;

CREATE TABLE IF NOT EXISTS `autor` (
  `Aut_Id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `Aut_Nombre` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Aut_Apellido` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Aut_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Entidad de autores.';

CREATE TABLE IF NOT EXISTS `genero` (
  `Gen_Id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `Gen_Nombre` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Gen_Id`) USING BTREE,
  KEY `Cat_Genero` (`Gen_Nombre`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Entidad Categoria para libros.';

CREATE TABLE IF NOT EXISTS `libro` (
  `Lib_Id` int unsigned NOT NULL AUTO_INCREMENT,
  `Lib_Nombre` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `Lib_Editorial` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `Lib_NroPaginas` int unsigned NOT NULL DEFAULT '0',
  `Lib_FPublicacion` date NOT NULL,
  `Lib_IdAutor` tinyint unsigned NOT NULL,
  PRIMARY KEY (`Lib_Id`),
  UNIQUE KEY `Lib_IdAutor` (`Lib_IdAutor`),
  KEY `Lib_Nombre` (`Lib_Nombre`),
  CONSTRAINT `FK_libro_autor` FOREIGN KEY (`Lib_IdAutor`) REFERENCES `autor` (`Aut_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Entidad de libros.';

CREATE TABLE IF NOT EXISTS `librocategoria` (
  `Id_Libro` int unsigned NOT NULL,
  `Id_Categoria` tinyint unsigned NOT NULL,
  UNIQUE KEY `Id_Libro` (`Id_Libro`),
  UNIQUE KEY `Id_Categoria` (`Id_Categoria`),
  CONSTRAINT `FK_librocategoria_categoria` FOREIGN KEY (`Id_Categoria`) REFERENCES `genero` (`Gen_Id`),
  CONSTRAINT `FK_librocategoria_libro` FOREIGN KEY (`Id_Libro`) REFERENCES `libro` (`Lib_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Relacion entre entidades libro y categoria.';

CREATE TABLE IF NOT EXISTS `librofavorito` (
  `Id_Usuario` int unsigned NOT NULL,
  `Id_Libro` int unsigned NOT NULL,
  UNIQUE KEY `Id_Libro` (`Id_Libro`),
  UNIQUE KEY `Dni_Usuario` (`Id_Usuario`) USING BTREE,
  CONSTRAINT `FK_librofavorito_libro` FOREIGN KEY (`Id_Libro`) REFERENCES `libro` (`Lib_Id`),
  CONSTRAINT `FK_librofavorito_usuario` FOREIGN KEY (`Id_Usuario`) REFERENCES `usuario` (`Usu_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Relacion de Libro favorito entre entidad usuario y entidad libro.';

CREATE TABLE IF NOT EXISTS `usuario` (
  `Usu_Id` int unsigned NOT NULL AUTO_INCREMENT,
  `Usu_Dni` int unsigned NOT NULL,
  `Usu_Nombre` varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
  `Usu_Apellido` varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
  `Usu_Email` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `Usu_Password` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Usu_Telefono` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`Usu_Id`),
  UNIQUE KEY `Usu_Dni` (`Usu_Dni`),
  UNIQUE KEY `Usu_Email` (`Usu_Email`),
  KEY `Usu_Password` (`Usu_Password`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Entidad de usuarios.';

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
