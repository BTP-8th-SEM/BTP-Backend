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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `test_db` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `maxMarks` int DEFAULT NULL,
  `passMarks` int DEFAULT NULL,
  `testType` varchar(45) DEFAULT NULL,
  `startTime` varchar(45) DEFAULT NULL,
  `endTime` varchar(45) DEFAULT NULL,
  `sharableId` varchar(45) DEFAULT NULL,
  `teacherEmail` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `questions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `optionsId` int DEFAULT NULL,
  `testId` int DEFAULT NULL,
  `maxMarks` int DEFAULT NULL,
  `body` varchar(255) DEFAULT NULL,
  `topic` varchar(45) DEFAULT NULL,
  `answerType` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `mcq_options` (
  `id` int NOT NULL AUTO_INCREMENT,
  `option1` varchar(255) DEFAULT NULL,
  `option2` varchar(255) DEFAULT NULL,
  `option3` varchar(255) DEFAULT NULL,
  `option4` varchar(255) DEFAULT NULL,
  `correctOption` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `responses` (
  `id` int NOT NULL AUTO_INCREMENT,
  `questionId` int DEFAULT NULL,
  `userId` int DEFAULT NULL,
  `testId` int DEFAULT NULL,
  `body` varchar(255) DEFAULT NULL,
  `obtainedMarks` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `student_test_map` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userEmail` varchar(45) DEFAULT NULL,
  `testId` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `intest`.`olap_test` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `testId` INT NULL,
  `totalAppeared` INT NULL,
  `maxMarks` INT NULL,
  `highestMarks` INT NULL,
  `lowestMarks` INT NULL,
  `avgMarks` INT NULL,
  `noOfPassed` INT NULL,
  `noOfFailed` INT NULL,
  `lastUpdated` VARCHAR(255) NULL,
  PRIMARY KEY (`id`));
  
CREATE TABLE `intest`.`olap_question` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `questionId` INT NULL,
  `maxMarks` INT NULL,
  `highestMarks` INT NULL,
  `lowestMarks` INT NULL,
  `avgMarks` INT NULL,
  `topic` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));