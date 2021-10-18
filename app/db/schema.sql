CREATE TABLE `merchants` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `identity_id` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `merchant_name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `description` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `contact_person` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `contact_number` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `contact_email` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `address` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` decimal(20,7) DEFAULT NULL,
  `updated_at` decimal(20,7) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `identity_id` (`identity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `clients` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `client_id` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `audience` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `pub_key` text COLLATE utf8mb4_general_ci NOT NULL,
  `active` tinyint(1) NOT NULL,
  `created_at` decimal(20,7) DEFAULT NULL,
  `updated_at` decimal(20,7) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `client_id` (`client_id`),
  UNIQUE KEY `audience` (`audience`),
  CONSTRAINT `clients_chk_1` CHECK ((`active` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
