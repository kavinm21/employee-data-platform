USE auth;
CREATE TABLE `keystore` 
(
  `user_id` int NOT NULL AUTO_INCREMENT,
  `passkey` varchar(64) COLLATE utf8mb4_general_ci NOT NULL,
  `username` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) 
ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;