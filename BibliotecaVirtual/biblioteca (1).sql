-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 01-08-2022 a las 05:36:15
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `biblioteca`
--
CREATE DATABASE IF NOT EXISTS `biblioteca` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `biblioteca`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autor`
--

CREATE TABLE `autor` (
  `Aut_Id` tinyint(3) UNSIGNED NOT NULL,
  `Aut_Nombre` varchar(15) NOT NULL,
  `Aut_Apellido` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Entidad de autores.';


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genero`
--

CREATE TABLE `genero` (
  `Gen_Id` tinyint(3) UNSIGNED NOT NULL,
  `Gen_Nombre` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Entidad Categoria para libros.';


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libro`
--

CREATE TABLE `libro` (
  `Lib_Id` int(10) UNSIGNED NOT NULL,
  `Lib_Nombre` varchar(100) NOT NULL,
  `Lib_Editorial` varchar(30) NOT NULL,
  `Lib_NroPaginas` int(10) UNSIGNED NOT NULL DEFAULT 0,
  `Lib_FPublicacion` date NOT NULL,
  `Lib_IdAutor` tinyint(3) UNSIGNED NOT NULL,
  `Lib_IdGenero` tinyint(3) UNSIGNED NOT NULL,
  `Lib_Descripcion` varchar(300) NOT NULL COMMENT 'Descripcion del libro',
  `Lib_Url` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Entidad de libros.';

--
-- Volcado de datos para la tabla `libro`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `librofavorito`
--

CREATE TABLE `librofavorito` (
  `Id_Usuario` int(10) UNSIGNED NOT NULL,
  `Id_Libro` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Relacion de Libro favorito entre entidad usuario y entidad libro.';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `Usu_Id` int(10) UNSIGNED NOT NULL,
  `Usu_Dni` int(10) UNSIGNED NOT NULL,
  `Usu_Nombre` varchar(15) NOT NULL,
  `Usu_Apellido` varchar(15) NOT NULL,
  `Usu_Email` varchar(30) NOT NULL,
  `Usu_Password` varchar(300) NOT NULL,
  `Usu_Telefono` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Entidad de usuarios.';

--
-- Volcado de datos para la tabla `usuario`
--


--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `autor`
--
ALTER TABLE `autor`
  ADD PRIMARY KEY (`Aut_Id`);

--
-- Indices de la tabla `genero`
--
ALTER TABLE `genero`
  ADD PRIMARY KEY (`Gen_Id`) USING BTREE,
  ADD KEY `Cat_Genero` (`Gen_Nombre`) USING BTREE;

--
-- Indices de la tabla `libro`
--
ALTER TABLE `libro`
  ADD PRIMARY KEY (`Lib_Id`),
  ADD UNIQUE KEY `Lib_IdAutor` (`Lib_IdAutor`),
  ADD KEY `Lib_Nombre` (`Lib_Nombre`),
  ADD KEY `FK_libro_genero` (`Lib_IdGenero`);

--
-- Indices de la tabla `librofavorito`
--
ALTER TABLE `librofavorito`
  ADD UNIQUE KEY `Id_Libro` (`Id_Libro`),
  ADD UNIQUE KEY `Dni_Usuario` (`Id_Usuario`) USING BTREE;

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`Usu_Id`),
  ADD UNIQUE KEY `Usu_Dni` (`Usu_Dni`),
  ADD UNIQUE KEY `Usu_Email` (`Usu_Email`),
  ADD KEY `Usu_Password` (`Usu_Password`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `autor`
--
ALTER TABLE `autor`
  MODIFY `Aut_Id` tinyint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `genero`
--
ALTER TABLE `genero`
  MODIFY `Gen_Id` tinyint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `libro`
--
ALTER TABLE `libro`
  MODIFY `Lib_Id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `Usu_Id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `libro`
--
ALTER TABLE `libro`
  ADD CONSTRAINT `FK_libro_autor` FOREIGN KEY (`Lib_IdAutor`) REFERENCES `autor` (`Aut_Id`),
  ADD CONSTRAINT `FK_libro_genero` FOREIGN KEY (`Lib_IdGenero`) REFERENCES `genero` (`Gen_Id`);

--
-- Filtros para la tabla `librofavorito`
--
ALTER TABLE `librofavorito`
  ADD CONSTRAINT `FK_librofavorito_libro` FOREIGN KEY (`Id_Libro`) REFERENCES `libro` (`Lib_Id`),
  ADD CONSTRAINT `FK_librofavorito_usuario` FOREIGN KEY (`Id_Usuario`) REFERENCES `usuario` (`Usu_Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
