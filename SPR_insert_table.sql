INSERT INTO spr_user (name, role) VALUES
    ('Dan Zhou', 'mentor'),
    ('Laney Johnson', 'parent'),
    ('Amaya Grant', 'parent'),
    ('Aniyah Quigley', 'parent'),
    ('Aileen Rohan', 'parent'),
    ('Darion Cronin', 'student'),
    ('Melissa Mitchell', 'student'),
    ('Maxine Crona', 'student'),
    ('Justice Adams', 'student');

INSERT INTO task (title, due_date, priority) VALUES
    ('UC Application', '2019-11-30', 'High'),
    ('Common App', '2020-1-10', 'Low');

INSERT INTO task_milestone (task_id, milestone, status) VALUES
    ('1', 'Finalize majors and colleges', 'Incomplete'),
    ('1', 'Create Portal Log In', 'Incomplete'),
    ('1', 'Filling out personal information and activities', 'Incomplete'),
    ('1', 'Personal statement 1', 'Complete'),
    ('1', 'Personal statement 2', 'Incomplete'),
    ('1', 'Personal statement 3', 'Complete'),
    ('1', 'Personal statement 4', 'Incomplete'),
    ('1', 'Additional Comments', 'Incomplete'),
    ('2', 'Finalize majors and colleges', 'Incomplete'),
    ('2', 'Create Portal Log In', 'Incomplete'),
    ('2', 'Assign and request letters of recommendations and approval', 'Incomplete'),
    ('2', 'Filling out personal information and activities', 'Incomplete'),
    ('2', 'Complete 650 common app essay', 'Incomplete'),
    ('2', 'Complete college supplements', 'Incomplete'),
    ('2', 'Additional Comments', 'Incomplete');

SELECT task_id, id
FROM task_milestone
ORDER BY task_id ASC, id ASC;