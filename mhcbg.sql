# ************************************************************
# Sequel Pro SQL dump
# Version 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 127.0.0.1 (MySQL 5.6.24-log)
# Database: mhcbg
# Generation Time: 2019-06-25 07:34:48 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table accountPriceDetail
# ------------------------------------------------------------

DROP TABLE IF EXISTS `accountPriceDetail`;

CREATE TABLE `accountPriceDetail` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增ID号',
  `priceDetail` varchar(300) NOT NULL DEFAULT '' COMMENT '价格详情',
  `linkDir` varchar(300) NOT NULL DEFAULT '' COMMENT '连接地址',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table crawlerIp
# ------------------------------------------------------------

DROP TABLE IF EXISTS `crawlerIp`;

CREATE TABLE `crawlerIp` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '爬虫IP代理池自增ID号',
  `ipAddr` varchar(40) NOT NULL DEFAULT '' COMMENT 'IP地址',
  PRIMARY KEY (`id`),
  UNIQUE KEY `ipAddr` (`ipAddr`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `crawlerIp` WRITE;
/*!40000 ALTER TABLE `crawlerIp` DISABLE KEYS */;

INSERT INTO `crawlerIp` (`id`, `ipAddr`)
VALUES
	(17082,'http://182.150.35.145:8080'),
	(16820,'http://218.60.8.83:3129');

/*!40000 ALTER TABLE `crawlerIp` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
