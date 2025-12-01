---
layout: post
title: SQL Test – 2
description: 
thumbnail: ../../../../../assets/images/sql/sql-test.png
author: Dipak Pulami Magar
date :  2025-11-30 12:12:45 +0545
categories: sql test
status: draft
---


**1. Retrieve the first purchase date and the total number of purchases for each customer.**
```sql
-- Creating transactions table
CREATE TABLE IF NOT EXISTS transactions(
	customer_id VARCHAR(5),
  purchase_date DATE,
  transaction_id VARCHAR(8)
);
```

```sql
-- Inserting data into: transactions table
INSERT INTO transactions(customer_id, purchase_date, transaction_id) VALUES
('C1', '2024-01-10', 'T001'),
('C1', '2024-01-15', 'T002'),
('C2', '2024-02-01', 'T003'),
('C1', '2024-02-20', 'T004'),
('C2', '2024-03-05', 'T005');
```

```sql
-- 1. Retrieve the first purchase date and the total number of purchases for each customer.
SELECT 
    customer_id, 
    MIN(purchase_date) AS first_purchase_date, 
    COUNT(customer_id) AS total_purchases
FROM transactions
GROUP BY customer_id;
```

Output:
```
+-------------+---------------------+-----------------+
| customer_id | first_purchase_date | total_purchases |
+-------------+---------------------+-----------------+
| C1          | 2024-01-10          |               3 |
| C2          | 2024-02-01          |               2 |
+-------------+---------------------+-----------------+
```

**Altering transactions table for second question.**
```sql
ALTER TABLE transactions` 
ADD COLUMN `amount` INT NULL AFTER `transaction_id`;

UPDATE transactions SET amount = 100 WHERE transaction_id = 'T001';
UPDATE transactions SET amount = 150 WHERE transaction_id = 'T002';
UPDATE transactions SET amount = 100 WHERE transaction_id = 'T003';
UPDATE transactions SET amount = 100 WHERE transaction_id = 'T004';
UPDATE transactions SET amount = 150 WHERE transaction_id = 'T005';
```

**2.  Find the transaction amount that occurs most frequently**
```sql
-- 2.  Find the transaction amount that occurs most frequently
SELECT amount
FROM transactions
GROUP BY amount
ORDER BY COUNT(amount) DESC
LIMIT 1;
```

<!-- ```sql
-- Rough 
SELECT amount, COUNT(*) AS freq
FROM transactions
GROUP BY amount
ORDER BY freq DESC;
``` -->

Output:
```
+--------+
| amount |
+--------+
|    100 |
+--------+
```

**Question 3. Identify the top 3 departments based on their average salary.**
```sql
-- Creating table employee
CREATE TABLE IF NOT EXISTS employee(
	emp_id INT,
	department VARCHAR(20),
	salary INT
);

-- Inserting data into table employee
INSERT INTO employee (emp_id, department, salary) VALUES ('1', 'HR', '50000');
INSERT INTO employee (emp_id, department, salary) VALUES ('2', 'IT', '80000');
INSERT INTO employee (emp_id, department, salary) VALUES ('3', 'IT', '85000');
INSERT INTO employee (emp_id, department, salary) VALUES ('4', 'Sales', '60000');
INSERT INTO employee (emp_id, department, salary) VALUES ('5', 'Sales', '62000');
INSERT INTO employee (emp_id, department, salary) VALUES ('6', 'Finance', '75000');
```

```sql
-- Identify the top 3 departments based on their average salary.
SELECT department, AVG(salary) AS avg_salary
FROM employee
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 3;
```

Output:
```
+------------+------------+
| department | avg_salary |
+------------+------------+
| IT         | 82500.0000 |
| Finance    | 75000.0000 |
| Sales      | 61000.0000 |
+------------+------------+
```

**Question 4. Solve the following problems**


<!-- 1. Write a query to select all students.
2. Display only the names and GPA of students.
3. Find students who belong to the `Physics` department.
4. List students whose GPA is greater than `3.5`.
5. Retrieve the course names with credits greater than `3`.
6. Show all enrollments for `Fall2024`.
7. Get student names in ascending order.
8. Count the total number of students.
9. Find the average GPA of students in `ComputerSci` department.
10. Show distinct department names from the `students` table.
11. Find students who scored grade A in any course.
12. Retrieve all courses taken by `Alice`.
13. List student names along with the courses they enrolled in (using `JOIN`).
14. Show students who are enrolled in more than one course.
15. Get the highest GPA student from the `Physics` department.
16. Find courses that have not been taken by any student.
17. Display the number of students enrolled in each course.
18. Show student names along with their average grade per semester.
19. Write a query to update Bob’s GPA to `3.5`.
20. Delete enrollments where grade is `C+`. -->


```sql
-- Creating table students
CREATE TABLE IF NOT EXISTS students(
	student_id INT PRIMARY KEY,
	name VARCHAR(50),
	age INT,
	department VARCHAR(30),
	gpa FLOAT
);

-- Inserting data into students table
INSERT INTO students (student_id, name, age, department, gpa) VALUES ('1', 'Alice', '20', 'ComputerSci', '3.8');
INSERT INTO students (student_id, name, age, department, gpa) VALUES ('2', 'Bob', '22', 'Physics', '3.2');
INSERT INTO students (student_id, name, age, department, gpa) VALUES ('3', 'Charlie', '21', 'Mathematics', '2.9');
INSERT INTO students (student_id, name, age, department, gpa) VALUES ('4', 'Diana', '23', 'ComputerSci', '3.6');
INSERT INTO students (student_id, name, age, department, gpa) VALUES ('5', 'Eva', '20', 'Physics', '3.1');
```

```sql
-- Creating courses students
CREATE TABLE IF NOT EXISTS courses(
  course_id INT PRIMARY KEY,
  course_name VARCHAR(20),
  credits TINYINT
);

-- Inserting data into courses table
INSERT INTO courses (course_id, course_name, credits) VALUES ('101', 'Database', '3');
INSERT INTO courses (course_id, course_name, credits) VALUES ('102', 'Algorithms', '4');
INSERT INTO courses (course_id, course_name, credits) VALUES ('103', 'Physics-I', '3');
INSERT INTO courses (course_id, course_name, credits) VALUES ('104', 'Calculus', '4');
INSERT INTO courses (course_id, course_name, credits) VALUES ('105', 'AI Basics', '3');
```

```sql
-- Creating enrollments students
CREATE TABLE IF NOT EXISTS enrollments(
	enrollment_id INT PRIMARY KEY,
	student_id INT,
	course_id INT,
	semester VARCHAR(20),
	grade VARCHAR(5)
);

-- Inserting data into enrollments table
INSERT INTO enrollments (enrollment_id, student_id, course_id, semester, grade) VALUES
(1, 1, 101, 'Fall2024', 'A'),
(2, 1, 102, 'Fall2024', 'B'),
(3, 2, 103, 'Fall2024', 'B+'),
(4, 3, 104, 'Fall2024', 'A-'),
(5, 4, 101, 'Fall2024', 'B'),
(6, 5, 103, 'Fall2024', 'C+'),
(7, 2, 104, 'Spring25', 'A'),
(8, 3, 105, 'Spring25', 'B+');
```

**1. Select all students**
```sql
-- 1. Select all students
SELECT * 
FROM students;
```
Output:
```
+------------+---------+------+-------------+------+
| student_id | name    | age  | department  | gpa  |
+------------+---------+------+-------------+------+
|          1 | Alice   |   20 | ComputerSci |  3.8 |
|          2 | Bob     |   22 | Physics     |  3.2 |
|          3 | Charlie |   21 | Mathematics |  2.9 |
|          4 | Diana   |   23 | ComputerSci |  3.6 |
|          5 | Eva     |   20 | Physics     |  3.1 |
+------------+---------+------+-------------+------+
```
**2. Display only the names and GPA of students**
```sql
-- 2. Display only the names and GPA of students
SELECT name, gpa 
FROM students;
```
Output:
```
+---------+------+
| name    | gpa  |
+---------+------+
| Alice   |  3.8 |
| Bob     |  3.2 |
| Charlie |  2.9 |
| Diana   |  3.6 |
| Eva     |  3.1 |
+---------+------+
```

**3. Find students who belong to the Physics department**
```sql
-- 3. Find students who belong to the Physics department
SELECT * 
FROM students
WHERE department = 'Physics';
```

Output:
```sql
+------------+------+------+------------+------+
| student_id | name | age  | department | gpa  |
+------------+------+------+------------+------+
|          2 | Bob  |   22 | Physics    |  3.2 |
|          5 | Eva  |   20 | Physics    |  3.1 |
+------------+------+------+------------+------+
```
**4. List students whose GPA is greater than 3.5**
```sql
-- 4. List students whose GPA is greater than 3.5
SELECT * FROM students
WHERE gpa > 3.5;
```

Output:
```sql
+------------+-------+------+-------------+------+
| student_id | name  | age  | department  | gpa  |
+------------+-------+------+-------------+------+
|          1 | Alice |   20 | ComputerSci |  3.8 |
|          4 | Diana |   23 | ComputerSci |  3.6 |
+------------+-------+------+-------------+------+
```

**5. Retrieve the course names with credits greater than 3**
```sql
-- 5. Retrieve the course names with credits greater than 3
SELECT course_name, credits 
FROM courses
WHERE credits > 3;
```
Output:
```
+-------------+---------+
| course_name | credits |
+-------------+---------+
| Algorithms  |       4 |
| Calculus    |       4 |
+-------------+---------+
```

**6. Show all enrollments for Fall2024**
```sql
-- 6. Show all enrollments for Fall2024
SELECT * 
FROM enrollments
WHERE semester = 'Fall2024';
```

Output:
```
+---------------+------------+-----------+----------+-------+
| enrollment_id | student_id | course_id | semester | grade |
+---------------+------------+-----------+----------+-------+
|             1 |          1 |       101 | Fall2024 | A     |
|             2 |          1 |       102 | Fall2024 | B     |
|             3 |          2 |       103 | Fall2024 | B+    |
|             4 |          3 |       104 | Fall2024 | A-    |
|             5 |          4 |       101 | Fall2024 | B     |
|             6 |          5 |       103 | Fall2024 | C+    |
+---------------+------------+-----------+----------+-------+
```

**7. Get student names in ascending order**
```sql
-- 7. Get student names in ascending order
SELECT name 
FROM students
ORDER BY name ASC;
```

Output:
```
+---------+
| name    |
+---------+
| Alice   |
| Bob     |
| Charlie |
| Diana   |
| Eva     |
+---------+
```

**8. Count the total number of students**
```sql
-- 8. Count the total number of students
SELECT COUNT(*) AS total_students 
FROM students;
```

Output:
```
+----------------+
| total_students |
+----------------+
|              5 |
+----------------+
```
**9. Find the average GPA of students in ComputerSci department**
```sql
-- 9. Find the average GPA of students in ComputerSci department
SELECT AVG(gpa) AS avg_gpa
FROM students
WHERE department = 'ComputerSci';
```

Output:
```
+--------------------+
| avg_gpa            |
+--------------------+
| 3.6999999284744263 |
+--------------------+
```

**10. Show distinct department names**
```sql
-- 10. Show distinct department names
SELECT DISTINCT department
FROM students;
```

Output:
```
+-------------+
| department  |
+-------------+
| ComputerSci |
| Physics     |
| Mathematics |
+-------------+
```

**11. Find students who scored grade A in any course**
```sql
-- 11. Find students who scored grade A in any course
SELECT DISTINCT s.name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
WHERE e.grade = 'A';
```
Output:
```
+-------+
| name  |
+-------+
| Alice |
| Bob   |
+-------+
```

**12. Retrieve all courses taken by Alice**
```sql
-- 12. Retrieve all courses taken by Alice
SELECT c.course_name
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
JOIN students s ON s.student_id = e.student_id
WHERE s.name = 'Alice';
```

Output:
```
+-------------+
| course_name |
+-------------+
| Database    |
| Algorithms  |
+-------------+
```

**13. List student names along with the courses they enrolled in**
```sql
-- 13. List student names along with the courses they enrolled in
SELECT s.name, c.course_name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id;
```

Output:
```
+---------+-------------+
| name    | course_name |
+---------+-------------+
| Alice   | Database    |
| Alice   | Algorithms  |
| Bob     | Physics-I   |
| Charlie | Calculus    |
| Diana   | Database    |
| Eva     | Physics-I   |
| Bob     | Calculus    |
| Charlie | AI Basics   |
+---------+-------------+
```

**14. Show students who are enrolled in more than one course**
```sql
-- 14. Show students who are enrolled in more than one course
SELECT s.name, COUNT(*) AS course_count
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id
HAVING COUNT(*) > 1;
```
Output:
```
+---------+--------------+
| name    | course_count |
+---------+--------------+
| Alice   |            2 |
| Bob     |            2 |
| Charlie |            2 |
+---------+--------------+
```

**15. Get the highest GPA student from the Physics department**
```sql
-- 15. Get the highest GPA student from the Physics department
SELECT *
FROM students
WHERE department = 'Physics'
ORDER BY gpa DESC
LIMIT 1;
```
Output:
```
+------------+------+------+------------+------+
| student_id | name | age  | department | gpa  |
+------------+------+------+------------+------+
|          2 | Bob  |   22 | Physics    |  3.2 |
+------------+------+------+------------+------+
```


**16. Courses that have not been taken by any student**
```sql
-- 16. Courses that have not been taken by any student
SELECT c.*
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
WHERE e.course_id IS NULL;
```

Output:
```
Empty set (0.101 sec)
```

**17. Display the number of students enrolled in each course**
```sql
-- 17. Display the number of students enrolled in each course
SELECT c.course_name, COUNT(e.student_id) AS total_students
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;
```

Output:
```
+-------------+----------------+
| course_name | total_students |
+-------------+----------------+
| Database    |              2 |
| Algorithms  |              1 |
| Physics-I   |              2 |
| Calculus    |              2 |
| AI Basics   |              1 |
+-------------+----------------+
```

**18. Student names with their average grade per semester**
```sql
-- 18. Student names with their average grade per semester
SELECT s.name, e.semester, AVG(s.gpa) AS avg_grade
FROM enrollments AS e
JOIN students AS s ON s.student_id = e.student_id
GROUP BY s.name, e.semester;
```

Output:
```
+---------+------------+--------------------+
| name    | semester   | avg_grade          |
+---------+------------+--------------------+
| Alice   | Fall2024   |  3.799999952316284 |
| Bob     | Fall2024   |  3.200000047683716 |
| Charlie | Fall2024   | 2.9000000953674316 |
| Diana   | Fall2024   | 3.5999999046325684 |
| Eva     | Fall2024   | 3.0999999046325684 |
| Bob     | Spring2025 |  3.200000047683716 |
| Charlie | Spring2025 | 2.9000000953674316 |
+---------+------------+--------------------+
```

<!-- 
```sql
-- Assuming grade-to-points conversion is needed: A=4, A-=3.7, B=3, B+=3.3, C+=2.3)
-- Step 1: Use a CASE mapping
SELECT s.name, e.semester,
       AVG(
         CASE e.grade
           WHEN 'A'  THEN 4.0
           WHEN 'A-' THEN 3.7
           WHEN 'B+' THEN 3.3
           WHEN 'B'  THEN 3.0
           WHEN 'C+' THEN 2.3
         END
       ) AS avg_grade_points
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.name, e.semester;
```
Output:
```
+---------+------------+------------------+
| name    | semester   | avg_grade_points |
+---------+------------+------------------+
| Alice   | Fall2024   |          3.50000 |
| Bob     | Fall2024   |          3.30000 |
| Charlie | Fall2024   |          3.70000 |
| Diana   | Fall2024   |          3.00000 |
| Eva     | Fall2024   |          2.30000 |
| Bob     | Spring2025 |          4.00000 |
| Charlie | Spring2025 |          3.30000 |
+---------+------------+------------------+
``` -->


**19. Update Bob’s GPA to 3.5**
```sql
UPDATE students
SET gpa = 3.5
WHERE name = 'Bob';
```

**20. Delete enrollments where grade is C+**
```sql
DELETE FROM enrollments
WHERE grade = 'C+';
```