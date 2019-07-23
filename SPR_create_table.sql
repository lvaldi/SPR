-- CREATE TYPE task_priority AS ENUM ('Low', 'Medium', 'High');
-- CREATE TYPE task_status AS ENUM ('Incomplete', 'In Progress', 'Complete');

CREATE TABLE spr_user (
ID SERIAL,
Name VARCHAR(50) NOT NULL,
Role VARCHAR(20) NOT NULL,
PRIMARY KEY (ID));

CREATE TABLE task (
ID SERIAL,
Title VARCHAR(500),
Due_Date DATE,
Priority task_priority, 
sub_task VARCHAR(500), 
Status task_status,
Parent_Task INT,
PRIMARY KEY (ID),
FOREIGN KEY (Parent_Task) REFERENCES task(ID) ON DELETE CASCADE);

