-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  ven. 06 juil. 2018 à 13:57
-- Version du serveur :  5.7.19
-- Version de PHP :  7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `bdd_python`
--

-- --------------------------------------------------------

--
-- Structure de la table `modele_marque`
--

DROP TABLE IF EXISTS `modele_marque`;
CREATE TABLE IF NOT EXISTS `modele_marque` (
  `marque` varchar(30) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `produit`
--

DROP TABLE IF EXISTS `produit`;
CREATE TABLE IF NOT EXISTS `produit` (
  `pr_refour` varchar(40) NOT NULL,
  `pr_desi` varchar(100) NOT NULL,
  `pr_pack` int(11) NOT NULL,
  `pr_codebarre` bigint(14) DEFAULT NULL,
  `pr_prac` decimal(8,2) NOT NULL DEFAULT '0.00',
  `pr_prix` decimal(8,2) NOT NULL,
  `pr_modele` varchar(30) NOT NULL,
  `pr_cd_pr` bigint(16) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`pr_cd_pr`)
) ENGINE=MyISAM AUTO_INCREMENT=1000053 DEFAULT CHARSET=utf8mb4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
