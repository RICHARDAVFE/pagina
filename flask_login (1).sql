-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-07-2022 a las 19:16:29
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
-- Base de datos: `flask_login`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `codigos`
--

CREATE TABLE `codigos` (
  `id` int(10) NOT NULL,
  `name` varchar(55) NOT NULL,
  `archivo` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `codigos`
--

INSERT INTO `codigos` (`id`, `name`, `archivo`) VALUES
(5, 'Graficador de funciones con tkinter y matplotlib Python', '2022155829expoIA1.py');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` smallint(3) UNSIGNED NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(102) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password`) VALUES
(1, 'richard', 'ejemplo@gmail.com', 'pbkdf2:sha256:260000$fiRyeVmApEki8uvm$40d93cdea3f941010f3eedfafd228db15c41810ce625a691ff8cb2491300b010'),
(7, 'juan', 'juan@gmail.com', '123456'),
(11, 'juan', 'juan@gmail.com', 'pbkdf2:sha256:260000$Kyq65ZzowfPeCz2N$28c2f7eedfc5c39578ead586abaf935b9bc4deca4877b17363ae8abb91f0e14e'),
(12, 'pedro', 'pedro@gmail.com', 'pbkdf2:sha256:260000$rojAjvlbWB2jiOBB$cd731778f51757df283da5ba19bb74b263ec98df6e0a1aec3ac7829b2b3f0f6c'),
(13, 'maria', 'maria@gmail.com', 'pbkdf2:sha256:260000$iQDfoEVl1lCVhi1V$e786c0d371e09c8d8773c5515df8355d481b5aaea80723bd272a5d850b2c3bf4'),
(14, 'yorichard', 'yo@gmail.com', 'pbkdf2:sha256:260000$kZWAahBLYuy1cSPy$ed31c5c6bbb498539673ec1929bb73faf612908031132bbe5d456ba83518d60b');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `codigos`
--
ALTER TABLE `codigos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `codigos`
--
ALTER TABLE `codigos`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` smallint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
