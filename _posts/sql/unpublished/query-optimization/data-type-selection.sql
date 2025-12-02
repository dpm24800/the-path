CREATE TABLE employees (
    emp_id VARCHAR(255),
    name VARCHAR(255),
    age VARCHAR(255),
    salary VARCHAR(255),
    join_date VARCHAR(255)
);

INSERT INTO employees (emp_id, name, age, salary, join_date)
VALUES
('1', 'Ramesh Thapa', '35', '55000', '2023-01-15'),
('2', 'Sita Karki', '28', '45000', '2022-06-20'),
('3', 'Bikash Gurung', '40', '120000', '2021-03-10');



CREATE TABLE employees_optimized (
    emp_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age TINYINT UNSIGNED,
    salary INT UNSIGNED,
    join_date DATE
);

INSERT INTO employees_optimized (name, age, salary, join_date)
VALUES
('Ramesh Thapa', 35, 55000, '2023-01-15'),
('Sita Karki', 28, 45000, '2022-06-20'),
('Bikash Gurung', 40, 120000, '2021-03-10');


SELECT name, age, salary
FROM employees_optimized
WHERE age > 30 AND salary > 50000;