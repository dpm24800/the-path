

### Table: Employees


mysql> DESCRIBE Employees;
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| employee_id | int          | NO   | PRI | NULL    |       |
| name        | varchar(50)  | YES  |     | NULL    |       |
| dept_id     | int          | YES  | MUL | NULL    |       |
| manager_id  | int          | YES  | MUL | NULL    |       |
+-------------+--------------+------+-----+---------+-------+



---

### Table Departments;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| dept_id   | int          | NO   | PRI | NULL    |       |
| dept_name | varchar(50)  | YES  |     | NULL    |       |
| location  | varchar(50)  | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

INSERT INTO departments (dept_id, dept_name) VALUES
(1, 'HR'),
(2, 'Finance'),
(3, 'IT'),
(4, 'Marketing');


### Projects

-- Projects;
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| project_id  | int          | NO   | PRI | NULL    |       |
| project_name| varchar(100) | YES  |     | NULL    |       |
| start_date  | date         | YES  |     | NULL    |       |
| end_date    | date         | YES  |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+


### EmployeeProjects;
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| emp_id       | int          | NO   | PRI | NULL    |       |
| project_id   | int          | NO   | PRI | NULL    |       |
| role         | varchar(50)  | YES  |     | NULL    |       |
| hours_worked | int          | YES  |     | NULL    |       |
+--------------+--------------+------+-----+---------+-------+

```sql
CREATE TABLE employee_projects (
    emp_id INT,
    project_id INT,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

INSERT INTO employee_projects (emp_id, project_id) VALUES
(101, 10),
(104, 10),
(102, 20),
(103, 30),
(104, 30),
(105, 40);
```

---

### Salaries;
+---------------+--------------+------+-----+---------+-------+
| Field         | Type         | Null | Key | Default | Extra |
+---------------+--------------+------+-----+---------+-------+
| emp_id        | int          | NO   | PRI | NULL    |       |
| base_salary   | int          | YES  |     | NULL    |       |
| bonus         | int          | YES  |     | NULL    |       |
| effective_from| date         | YES  |     | NULL    |       |
+---------------+--------------+------+-----+---------+-------+




