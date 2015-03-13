CREATE DATABASE  IF NOT EXISTS `easecentral`;
USE `easecentral`;

--
-- Table structure for table `contact`
--

DROP TABLE IF EXISTS `contact`;
CREATE TABLE `contact` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `first_name` varchar(512) DEFAULT NULL,
    `last_name` varchar(512) DEFAULT NULL,
    `email` varchar(512) DEFAULT NULL,
    PRIMARY KEY (`id`)
);

--
-- Table structure for table `state`
--

DROP TABLE IF EXISTS `state`;
CREATE TABLE `state` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(512) DEFAULT NULL,
    `abbreviation` varchar(2) DEFAULT NULL,
    PRIMARY KEY (`id`)
);

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
CREATE TABLE `address` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `contact_id` int(11) DEFAULT NULL,
    `street1` varchar(512) DEFAULT NULL,
    `street2` varchar(512) DEFAULT NULL,
    `city` varchar(512) DEFAULT NULL,
    `state_id` int(2) DEFAULT NULL,
    `zip` int(5) DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `contact_id__idx` (`contact_id`),
    KEY `state_id__idx` (`state_id`),
    CONSTRAINT `address_ibfk_1` FOREIGN KEY (`contact_id`) REFERENCES `contact` (`id`) ON DELETE CASCADE,
    CONSTRAINT `address_ibfk_2` FOREIGN KEY (`state_id`) REFERENCES `state` (`id`) ON DELETE CASCADE
);

--
-- Table structure for table `phone_number`
--

DROP TABLE IF EXISTS `phone_number`;
CREATE TABLE `phone_number` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `contact_id` int(11) DEFAULT NULL,
    `number` varchar(10) DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `contact_id__idx` (`contact_id`),
    CONSTRAINT `phone_number_ibfk_1` FOREIGN KEY (`contact_id`) REFERENCES `contact` (`id`) ON DELETE CASCADE
);

--
-- Insert seed U.S. States
--

LOCK TABLES `state` WRITE;
INSERT INTO `state` VALUES
    (1,'Alabama','AL'),
    (2,'Alaska','AK'),
    (3,'American Samoa','AS'),
    (4,'Arizona','AZ'),
    (5,'Arkansas','AR'),
    (6,'California','CA'),
    (7,'Colorado','CO'),
    (8,'Connecticut','CT'),
    (9,'Delaware','DE'),
    (10,'District Of Columbia','DC'),
    (11,'Federated States Of Micronesia','FM'),
    (12,'Florida','FL'),
    (13,'Georgia','GA'),
    (14,'Guam','GU'),
    (15,'Hawaii','HI'),
    (16,'Idaho','ID'),
    (17,'Illinois','IL'),
    (18,'Indiana','IN'),
    (19,'Iowa','IA'),
    (20,'Kansas','KS'),
    (21,'Kentucky','KY'),
    (22,'Louisiana','LA'),
    (23,'Maine','ME'),
    (24,'Marshall Islands','MH'),
    (25,'Maryland','MD'),
    (26,'Massachusetts','MA'),
    (27,'Michigan','MI'),
    (28,'Minnesota','MN'),
    (29,'Mississippi','MS'),
    (30,'Missouri','MO'),
    (31,'Montana','MT'),
    (32,'Nebraska','NE'),
    (33,'Nevada','NV'),
    (34,'New Hampshire','NH'),
    (35,'New Jersey','NJ'),
    (36,'New Mexico','NM'),
    (37,'New York','NY'),
    (38,'North Carolina','NC'),
    (39,'North Dakota','ND'),
    (40,'Northern Mariana Islands','MP'),
    (41,'Ohio','OH'),
    (42,'Oklahoma','OK'),
    (43,'Oregon','OR'),
    (44,'Palau','PW'),
    (45,'Pennsylvania','PA'),
    (46,'Puerto Rico','PR'),
    (47,'Rhode Island','RI'),
    (48,'South Carolina','SC'),
    (49,'South Dakota','SD'),
    (50,'Tennessee','TN'),
    (51,'Texas','TX'),
    (52,'Utah','UT'),
    (53,'Vermont','VT'),
    (54,'Virgin Islands','VI'),
    (55,'Virginia','VA'),
    (56,'Washington','WA'),
    (57,'West Virginia','WV'),
    (58,'Wisconsin','WI'),
    (59,'Wyoming','WY');
UNLOCK TABLES;