CREATE TABLE `questions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `optionsId` int DEFAULT NULL,
  `testId` int DEFAULT NULL,
  `maxMarks` int DEFAULT NULL,
  `body` varchar(45) DEFAULT NULL,
  `topic` varchar(45) DEFAULT NULL,
  `answerType` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `users` (
  `email` varchar(255) DEFAULT NULL,
  `firstName` varchar(255) DEFAULT NULL,
  `lastName` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `role` varchar(255) DEFAULT NULL,
  `profilePicUrl` varchar(255) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `mcq_options` (
  `id` int NOT NULL AUTO_INCREMENT,
  `option1` int DEFAULT NULL,
  `option2` int DEFAULT NULL,
  `option3` int DEFAULT NULL,
  `option4` int DEFAULT NULL,
  `correctOption` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `responses` (
  `id` int NOT NULL AUTO_INCREMENT,
  `questionId` int DEFAULT NULL,
  `userId` int DEFAULT NULL,
  `testId` int DEFAULT NULL,
  `body` varchar(45) DEFAULT NULL,
  `obtainedMarks` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `test_db` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `maxMarks` int NOT NULL,
  `passMarks` int NOT NULL,
  `testType` int NOT NULL,
  `startTime` varchar(45) NOT NULL,
  `endTime` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- update this

ALTER TABLE `intest`.`questions` 
CHANGE COLUMN `body` `body` VARCHAR(255) NULL DEFAULT NULL ;

ALTER TABLE `intest`.`responses` 
CHANGE COLUMN `body` `body` VARCHAR(255) NULL DEFAULT NULL ;

CREATE TABLE `mcq_options` (
  `id` int NOT NULL AUTO_INCREMENT,
  `option1` varchar(255) DEFAULT NULL,
  `option2` varchar(255) DEFAULT NULL,
  `option3` varchar(255) DEFAULT NULL,
  `option4` varchar(255) DEFAULT NULL,
  `correctOption` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
