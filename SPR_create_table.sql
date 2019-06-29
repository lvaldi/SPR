
CREATE TABLE user (
ID INT NOT NULL AUTO_INCREMENT,
Name VARCHAR(50) NOT NULL,
Role VARCHAR(20) NOT NULL,
PRIMARY KEY (ID));

CREATE TABLE todolist (
ID INT NOT NULL AUTO_INCREMENT,
Title VARCHAR(80) NOT NULL,
Due_Date DATE NOT NULL,
Status ENUM('Incomplete', 'In Progress', 'Complete'),
Priority ENUM('1', '2', '3', '4', '5'), 
Milestone TEXT, 
PRIMARY KEY (ID));


