CREATE TABLE `intest`.`questions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `body` VARCHAR(45) NULL,
  `maxMarks` INT NULL,
  `answerType` VARCHAR(45) NULL,
  `answerId` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `answerId_idx` (`answerId` ASC) VISIBLE,
  CONSTRAINT `id`
    FOREIGN KEY (`answerId`)
    REFERENCES `intest`.`maq_answers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


CREATE TABLE `intest`.`maq_answers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `option1` INT NULL,
  `option2` INT NULL,
  `option3` INT NULL,
  `option4` INT NULL,
  `CorrectOption` INT NULL,
  PRIMARY KEY (`id`));