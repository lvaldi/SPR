CREATE TYPE task_priority AS ENUM ('Low', 'Medium', 'High');
CREATE TYPE task_status AS ENUM ('Incomplete', 'In Progress', 'Complete');

CREATE TABLE spr_user (
ID SERIAL,
Name VARCHAR(50) NOT NULL,
Role VARCHAR(20) NOT NULL,
PRIMARY KEY (ID));

CREATE TABLE task (
ID SERIAL,
Title VARCHAR(80) NOT NULL,
Due_Date DATE NOT NULL,
Priority task_priority, 
PRIMARY KEY (ID));

CREATE TABLE task_milestone (
    ID SERIAL,
    Task_ID INT NOT NULL,
    Milestone VARCHAR(200),
    Status task_status,
    PRIMARY KEY (ID, task_ID),
    FOREIGN KEY (task_ID) REFERENCES task(ID) ON DELETE CASCADE);


