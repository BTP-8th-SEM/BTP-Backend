
-- # Users
INSERT INTO `users` (`email`, `firstName`, `lastName`, `password`, `role`, `profilePicUrl`) VALUES
('amitabh@gmail.com', 'Amitabh', 'Bachchan', 'password', 'teacher', 'https://upload.wikimedia.org/wikipedia/commons/0/0b/Amitabh_Bachchan_in_2019.jpg'),
('shahrukh@gmail.com', 'Shahrukh', 'Khan', 'password', 'student', 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Shah_Rukh_Khan_graces_the_launch_of_the_New_MTV_Roadies_at_MaXposure_Office_in_Mumbai.jpg/1200px-Shah_Rukh_Khan_graces_the_launch_of_the_New_MTV_Roadies_at_MaXposure_Office_in_Mumbai.jpg'),
('salman@gmail.com', 'Salman', 'Khan', 'password', 'student', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Salman_Khan_on_the_sets_of_Bharat.jpg/220px-Salman_Khan_on_the_sets_of_Bharat.jpg'),
('aamir@gmail.com', 'Aamir', 'Khan', 'password', 'student', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Aamir_Khan_At_An_Event_%28cropped%29.jpg/1200px-Aamir_Khan_At_An_Event_%28cropped%29.jpg'),
('hrithik@gmail.com', 'Hrithik', 'Roshan', 'password', 'student', 'https://upload.wikimedia.org/wikipedia/commons/5/5f/Hrithik_roshan.jpg');

-- #Tests
INSERT INTO `test_db` (`name`, `maxMarks`, `passMarks`, `testType`, `startTime`, `endTime`, `sharableId`, `teacherEmail`) VALUES
('DSA', 20, 7, 'MCQ', '25-04-2023 12:30 PM', '25-04-2023 2:30 PM', 'ABC123', 'amitabh@gmail.com'),
('GK Test', 15, 10, 'MCQ', '27-04-2023 12:30 PM', '27-04-2023 2:30 PM', 'ABC123', 'amitabh@gmail.com');
-- # Questions
-- Question 1
INSERT INTO questions (optionsId, testId, maxMarks, body, topic, answerType) VALUES
(1, 1, 5, 'What is the capital of India?', 'Cities', 'mcq');
-- Question 2
INSERT INTO questions (optionsId, testId, maxMarks, body, topic, answerType) VALUES
(2, 1, 5, 'Who is the current Prime Minister of India?', 'Government', 'mcq');
-- Question 3
INSERT INTO questions (optionsId, testId, maxMarks, body, topic, answerType) VALUES
(3, 1, 5, 'What is the national animal of India?', 'Animals', 'mcq');

-- # Options
-- Options for Question 1
INSERT INTO mcq_options (option1, option2, option3, option4, correctOption) VALUES
('Mumbai', 'Kolkata', 'New Delhi', 'Chennai', 3);
-- Options for Question 2
INSERT INTO mcq_options (option1, option2, option3, option4, correctOption) VALUES
('Narendra Modi', 'Amit Shah', 'Manmohan Singh', 'Rahul Gandhi', 1);
-- Options for Question 3
INSERT INTO mcq_options (option1, option2, option3, option4, correctOption) VALUES
('Lion', 'Tiger', 'Elephant', 'Panda', 2);

-- # Responses
-- Responses for Student 1 for Test 1
INSERT INTO responses (questionId, userId, testId, body, obtainedMarks) VALUES
(1, 2, 1, 'New Delhi', 5),
(2, 2, 1, 'Narendra Modi', 5),
(3, 2, 1, 'Tiger', 5);
-- Responses for Student 2 for Test 1
INSERT INTO responses (questionId, userId, testId, body, obtainedMarks) VALUES
(1, 3, 1, 'Mumbai', 0),
(2, 3, 1, 'Rahul Gandhi', 0),
(3, 3, 1, 'Lion', 0);
-- Responses for Student 3 for Test 1
INSERT INTO responses (questionId, userId, testId, body, obtainedMarks) VALUES
(1, 4, 1, 'Mumbai', 0),
(2, 4, 1, 'Narendra Modi', 5),
(3, 4, 1, 'Lion', 0);
-- Responses for Student 4  for Test 1
INSERT INTO responses (questionId, userId, testId, body, obtainedMarks) VALUES
(1, 5, 1, 'New Delhi', 5),
(2, 5, 1, 'Rahul Gandhi', 0),
(3, 5, 1, 'Tiger', 5);



