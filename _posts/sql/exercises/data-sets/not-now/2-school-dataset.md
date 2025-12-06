# Sector 2: School

### Table 1: students
```
+------------+---------------+------+-----+---------+----------------+
| Field      | Type          | Null | Key | Default | Extra          |
+------------+---------------+------+-----+---------+----------------+
| student_id | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| first_name | VARCHAR(50)   | NO   |     | NULL    |                |
| last_name  | VARCHAR(50)   | NO   |     | NULL    |                |
| dob        | DATE          | NO   |     | NULL    |                |
| gender     | VARCHAR(10)   | YES  |     | NULL    |                |
| address    | VARCHAR(100)  | YES  |     | NULL    |                |
+------------+---------------+------+-----+---------+----------------+

+------------+------------+-----------+------------+--------+----------------------+
| student_id | first_name | last_name | dob        | gender | address              |
+------------+------------+-----------+------------+--------+----------------------+
| 101        | Alice      | Johnson   | 2010-01-15 | Female | 123 Maple St         |
| 102        | Bob        | Smith     | 2009-05-20 | Male   | 456 Oak St           |
| 103        | Charlie    | Lee       | 2010-07-12 | Male   | 789 Pine St          |
| 104        | Diana      | Brown     | 2008-11-30 | Female | 321 Elm St           |
| 105        | Ethan      | Davis     | 2009-03-22 | Male   | 654 Cedar St         |
| 106        | Fiona      | Miller    | 2010-08-05 | Female | 987 Spruce St        |
| 107        | George     | Wilson    | 2008-12-18 | Male   | 147 Birch St         |
| 108        | Hannah     | Moore     | 2009-06-25 | Female | 258 Poplar St        |
| 109        | Ian        | Taylor    | 2010-09-15 | Male   | 369 Walnut St        |
| 110        | Julia      | Anderson  | 2008-02-28 | Female | 741 Chestnut St      |
| 111        | Kevin      | Thomas    | 2009-10-10 | Male   | 852 Willow St        |
| 112        | Laura      | Jackson   | 2010-04-05 | Female | 963 Aspen St         |
| 113        | Michael    | White     | 2008-07-21 | Male   | 159 Dogwood St       |
| 114        | Nina       | Harris    | 2009-12-30 | Female | 753 Magnolia St      |
| 115        | Oliver     | Martin    | 2010-02-17 | Male   | 357 Redwood St       |
| 116        | Patricia   | Thompson  | 2008-03-09 | Female | 951 Sycamore St      |
| 117        | Quentin    | Garcia    | 2009-11-15 | Male   | 258 Hickory St       |
| 118        | Rachel     | Martinez  | 2010-06-20 | Female | 369 Beech St         |
| 119        | Samuel     | Robinson  | 2008-08-25 | Male   | 147 Locust St        |
| 120        | Tina       | Clark     | 2009-09-30 | Female | 456 Linden St        |
| 121        | Umar       | Rodriguez | 2010-01-10 | Male   | 789 Palm St          |
| 122        | Victoria   | Lewis     | 2008-05-05 | Female | 123 Fir St           |
| 123        | William    | Lee       | 2009-07-18 | Male   | 456 Pine St          |
| 124        | Xena       | Hall      | 2010-10-22 | Female | 789 Maple St         |
| 125        | Yara       | Allen     | 2008-12-15 | Female | 321 Oak St           |
| 126        | Zach       | Young     | 2009-03-12 | Male   | 654 Cedar St         |
| 127        | Amy        | King      | 2010-07-08 | Female | 987 Spruce St        |
| 128        | Brian      | Wright    | 2008-11-11 | Male   | 147 Birch St         |
| 129        | Chloe      | Scott     | 2009-06-14 | Female | 258 Poplar St        |
| 130        | David      | Green     | 2010-09-19 | Male   | 369 Walnut St        |
| 131        | Ella       | Adams     | 2008-02-20 | Female | 741 Chestnut St      |
| 132        | Frank      | Baker     | 2009-10-08 | Male   | 852 Willow St        |
| 133        | Grace      | Gonzalez  | 2010-04-22 | Female | 963 Aspen St         |
| 134        | Henry      | Nelson    | 2008-07-29 | Male   | 159 Dogwood St       |
| 135        | Isabella   | Carter    | 2009-12-12 | Female | 753 Magnolia St      |
| 136        | Jack       | Mitchell  | 2010-02-05 | Male   | 357 Redwood St       |
| 137        | Karen      | Perez     | 2008-03-18 | Female | 951 Sycamore St      |
| 138        | Liam       | Roberts   | 2009-11-22 | Male   | 258 Hickory St       |
| 139        | Mia        | Turner    | 2010-06-28 | Female | 369 Beech St         |
| 140        | Noah       | Phillips  | 2008-08-03 | Male   | 147 Locust St        |
| 141        | Olivia     | Campbell  | 2009-09-17 | Female | 456 Linden St        |
| 142        | Peter      | Parker    | 2010-01-26 | Male   | 789 Palm St          |
| 143        | Queenie    | Evans     | 2008-05-12 | Female | 123 Fir St           |
| 144        | Ryan       | Edwards   | 2009-07-23 | Male   | 456 Pine St          |
| 145        | Sophia     | Collins   | 2010-10-02 | Female | 789 Maple St         |
| 146        | Thomas     | Stewart   | 2008-12-28 | Male   | 321 Oak St           |
| 147        | Ursula     | Sanchez   | 2009-03-07 | Female | 654 Cedar St         |
| 148        | Victor     | Morris    | 2010-07-30 | Male   | 987 Spruce St        |
| 149        | Wendy      | Rogers    | 2008-11-20 | Female | 147 Birch St         |
| 150        | Xavier     | Reed      | 2009-06-08 | Male   | 258 Poplar St        |
+------------+------------+-----------+------------+--------+----------------------+
```

```sql
CREATE TABLE students (
    student_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    dob DATE NOT NULL,
    gender VARCHAR(10),
    address VARCHAR(100),
    PRIMARY KEY (student_id)
) ENGINE=InnoDB;

INSERT INTO students (student_id, first_name, last_name, dob, gender, address) VALUES
(101, 'Alice', 'Johnson', '2010-01-15', 'Female', '123 Maple St'),
(102, 'Bob', 'Smith', '2009-05-20', 'Male', '456 Oak St'),
(103, 'Charlie', 'Lee', '2010-07-12', 'Male', '789 Pine St'),
(104, 'Diana', 'Brown', '2008-11-30', 'Female', '321 Elm St'),
(105, 'Ethan', 'Davis', '2009-03-22', 'Male', '654 Cedar St'),
(106, 'Fiona', 'Miller', '2010-08-05', 'Female', '987 Spruce St'),
(107, 'George', 'Wilson', '2008-12-18', 'Male', '147 Birch St'),
(108, 'Hannah', 'Moore', '2009-06-25', 'Female', '258 Poplar St'),
(109, 'Ian', 'Taylor', '2010-09-15', 'Male', '369 Walnut St'),
(110, 'Julia', 'Anderson', '2008-02-28', 'Female', '741 Chestnut St'),
(111, 'Kevin', 'Thomas', '2009-10-10', 'Male', '852 Willow St'),
(112, 'Laura', 'Jackson', '2010-04-05', 'Female', '963 Aspen St'),
(113, 'Michael', 'White', '2008-07-21', 'Male', '159 Dogwood St'),
(114, 'Nina', 'Harris', '2009-12-30', 'Female', '753 Magnolia St'),
(115, 'Oliver', 'Martin', '2010-02-17', 'Male', '357 Redwood St'),
(116, 'Patricia', 'Thompson', '2008-03-09', 'Female', '951 Sycamore St'),
(117, 'Quentin', 'Garcia', '2009-11-15', 'Male', '258 Hickory St'),
(118, 'Rachel', 'Martinez', '2010-06-20', 'Female', '369 Beech St'),
(119, 'Samuel', 'Robinson', '2008-08-25', 'Male', '147 Locust St'),
(120, 'Tina', 'Clark', '2009-09-30', 'Female', '456 Linden St'),
(121, 'Umar', 'Rodriguez', '2010-01-10', 'Male', '789 Palm St'),
(122, 'Victoria', 'Lewis', '2008-05-05', 'Female', '123 Fir St'),
(123, 'William', 'Lee', '2009-07-18', 'Male', '456 Pine St'),
(124, 'Xena', 'Hall', '2010-10-22', 'Female', '789 Maple St'),
(125, 'Yara', 'Allen', '2008-12-15', 'Female', '321 Oak St'),
(126, 'Zach', 'Young', '2009-03-12', 'Male', '654 Cedar St'),
(127, 'Amy', 'King', '2010-07-08', 'Female', '987 Spruce St'),
(128, 'Brian', 'Wright', '2008-11-11', 'Male', '147 Birch St'),
(129, 'Chloe', 'Scott', '2009-06-14', 'Female', '258 Poplar St'),
(130, 'David', 'Green', '2010-09-19', 'Male', '369 Walnut St'),
(131, 'Ella', 'Adams', '2008-02-20', 'Female', '741 Chestnut St'),
(132, 'Frank', 'Baker', '2009-10-08', 'Male', '852 Willow St'),
(133, 'Grace', 'Gonzalez', '2010-04-22', 'Female', '963 Aspen St'),
(134, 'Henry', 'Nelson', '2008-07-29', 'Male', '159 Dogwood St'),
(135, 'Isabella', 'Carter', '2009-12-12', 'Female', '753 Magnolia St'),
(136, 'Jack', 'Mitchell', '2010-02-05', 'Male', '357 Redwood St'),
(137, 'Karen', 'Perez', '2008-03-18', 'Female', '951 Sycamore St'),
(138, 'Liam', 'Roberts', '2009-11-22', 'Male', '258 Hickory St'),
(139, 'Mia', 'Turner', '2010-06-28', 'Female', '369 Beech St'),
(140, 'Noah', 'Phillips', '2008-08-03', 'Male', '147 Locust St'),
(141, 'Olivia', 'Campbell', '2009-09-17', 'Female', '456 Linden St'),
(142, 'Peter', 'Parker', '2010-01-26', 'Male', '789 Palm St'),
(143, 'Queenie', 'Evans', '2008-05-12', 'Female', '123 Fir St'),
(144, 'Ryan', 'Edwards', '2009-07-23', 'Male', '456 Pine St'),
(145, 'Sophia', 'Collins', '2010-10-02', 'Female', '789 Maple St'),
(146, 'Thomas', 'Stewart', '2008-12-28', 'Male', '321 Oak St'),
(147, 'Ursula', 'Sanchez', '2009-03-07', 'Female', '654 Cedar St'),
(148, 'Victor', 'Morris', '2010-07-30', 'Male', '987 Spruce St'),
(149, 'Wendy', 'Rogers', '2008-11-20', 'Female', '147 Birch St'),
(150, 'Xavier', 'Reed', '2009-06-08', 'Male', '258 Poplar St');
```

### Table 2: teachers
```
+------------+---------------+------+-----+---------+----------------+
| Field      | Type          | Null | Key | Default | Extra          |
+------------+---------------+------+-----+---------+----------------+
| teacher_id | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| first_name | VARCHAR(50)   | NO   |     | NULL    |                |
| last_name  | VARCHAR(50)   | NO   |     | NULL    |                |
| hire_date  | DATE          | NO   |     | NULL    |                |
| subject    | VARCHAR(50)   | YES  |     | NULL    |                |
| email      | VARCHAR(100)  | YES  | UNI | NULL    |                |
+------------+---------------+------+-----+---------+----------------+

+------------+------------+-----------+------------+----------------+---------------------+
| teacher_id | first_name | last_name | hire_date  | subject        | email               |
+------------+------------+-----------+------------+----------------+---------------------+
| 201        | Adam       | Johnson   | 2015-08-01 | Math           | adam.johnson@mail.com |
| 202        | Beth       | Smith     | 2016-01-12 | English        | beth.smith@mail.com   |
| 203        | Carl       | Lee       | 2017-03-15 | Science        | carl.lee@mail.com     |
| 204        | Dana       | Brown     | 2014-09-05 | History        | dana.brown@mail.com   |
| 205        | Ethan      | Davis     | 2018-06-20 | Art            | ethan.davis@mail.com  |
| 206        | Fiona      | Miller    | 2016-11-10 | Math           | fiona.miller@mail.com |
| 207        | George     | Wilson    | 2015-05-23 | English        | george.wilson@mail.com|
| 208        | Hannah     | Moore     | 2017-07-17 | Science        | hannah.moore@mail.com |
| 209        | Ian        | Taylor    | 2018-02-28 | History        | ian.taylor@mail.com   |
| 210        | Julia      | Anderson  | 2014-10-01 | Art            | julia.anderson@mail.com|
| 211        | Kevin      | Thomas    | 2015-12-15 | Math           | kevin.thomas@mail.com |
| 212        | Laura      | Jackson   | 2016-03-05 | English        | laura.jackson@mail.com|
| 213        | Michael    | White     | 2017-08-22 | Science        | michael.white@mail.com|
| 214        | Nina       | Harris    | 2014-05-30 | History        | nina.harris@mail.com  |
| 215        | Oliver     | Martin    | 2018-01-18 | Art            | oliver.martin@mail.com|
| 216        | Patricia   | Thompson  | 2015-06-12 | Math           | patricia.thompson@mail.com|
| 217        | Quentin    | Garcia    | 2016-09-28 | English        | quentin.garcia@mail.com|
| 218        | Rachel     | Martinez  | 2017-11-11 | Science        | rachel.martinez@mail.com|
| 219        | Samuel     | Robinson  | 2014-03-05 | History        | samuel.robinson@mail.com|
| 220        | Tina       | Clark     | 2018-07-22 | Art            | tina.clark@mail.com   |
| 221        | Umar       | Rodriguez | 2015-04-10 | Math           | umar.rodriguez@mail.com|
| 222        | Victoria   | Lewis     | 2016-08-01 | English        | victoria.lewis@mail.com|
| 223        | William    | Lee       | 2017-05-19 | Science        | william.lee@mail.com  |
| 224        | Xena       | Hall      | 2014-12-03 | History        | xena.hall@mail.com    |
| 225        | Yara       | Allen     | 2018-02-14 | Art            | yara.allen@mail.com   |
| 226        | Zach       | Young     | 2015-09-17 | Math           | zach.young@mail.com   |
| 227        | Amy        | King      | 2016-06-30 | English        | amy.king@mail.com     |
| 228        | Brian      | Wright    | 2017-08-21 | Science        | brian.wright@mail.com |
| 229        | Chloe      | Scott     | 2014-11-19 | History        | chloe.scott@mail.com  |
| 230        | David      | Green     | 2018-01-05 | Art            | david.green@mail.com  |
| 231        | Ella       | Adams     | 2015-03-20 | Math           | ella.adams@mail.com   |
| 232        | Frank      | Baker     | 2016-07-12 | English        | frank.baker@mail.com  |
| 233        | Grace      | Gonzalez  | 2017-09-05 | Science        | grace.gonzalez@mail.com|
| 234        | Henry      | Nelson    | 2014-04-15 | History        | henry.nelson@mail.com |
| 235        | Isabella   | Carter    | 2018-05-25 | Art            | isabella.carter@mail.com|
| 236        | Jack       | Mitchell  | 2015-08-30 | Math           | jack.mitchell@mail.com|
| 237        | Karen      | Perez     | 2016-02-18 | English        | karen.perez@mail.com  |
| 238        | Liam       | Roberts   | 2017-03-29 | Science        | liam.roberts@mail.com |
| 239        | Mia        | Turner    | 2014-06-20 | History        | mia.turner@mail.com   |
| 240        | Noah       | Phillips  | 2018-07-08 | Art            | noah.phillips@mail.com|
| 241        | Olivia     | Campbell  | 2015-05-11 | Math           | olivia.campbell@mail.com|
| 242        | Peter      | Parker    | 2016-09-21 | English        | peter.parker@mail.com |
| 243        | Queenie    | Evans     | 2017-01-14 | Science        | queenie.evans@mail.com|
| 244        | Ryan       | Edwards   | 2014-08-30 | History        | ryan.edwards@mail.com |
| 245        | Sophia     | Collins   | 2018-03-02 | Art            | sophia.collins@mail.com|
| 246        | Thomas     | Stewart   | 2015-11-19 | Math           | thomas.stewart@mail.com|
| 247        | Ursula     | Sanchez   | 2016-04-05 | English        | ursula.sanchez@mail.com|
| 248        | Victor     | Morris    | 2017-07-28 | Science        | victor.morris@mail.com|
| 249        | Wendy      | Rogers    | 2014-02-15 | History        | wendy.rogers@mail.com |
| 250        | Xavier     | Reed      | 2018-06-12 | Art            | xavier.reed@mail.com  |
+------------+------------+-----------+------------+----------------+---------------------+
```

```sql
CREATE TABLE teachers (
    teacher_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    hire_date DATE NOT NULL,
    subject VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    PRIMARY KEY (teacher_id)
) ENGINE=InnoDB;

INSERT INTO teachers (teacher_id, first_name, last_name, hire_date, subject, email)
VALUES
(201, 'Adam', 'Johnson', '2015-08-01', 'Math', 'adam.johnson@mail.com'),
(202, 'Beth', 'Smith', '2016-01-12', 'English', 'beth.smith@mail.com'),
(203, 'Carl', 'Lee', '2017-03-15', 'Science', 'carl.lee@mail.com'),
(204, 'Dana', 'Brown', '2014-09-05', 'History', 'dana.brown@mail.com'),
(205, 'Ethan', 'Davis', '2018-06-20', 'Art', 'ethan.davis@mail.com'),
(206, 'Fiona', 'Miller', '2016-11-10', 'Math', 'fiona.miller@mail.com'),
(207, 'George', 'Wilson', '2015-05-23', 'English', 'george.wilson@mail.com'),
(208, 'Hannah', 'Moore', '2017-07-17', 'Science', 'hannah.moore@mail.com'),
(209, 'Ian', 'Taylor', '2018-02-28', 'History', 'ian.taylor@mail.com'),
(210, 'Julia', 'Anderson', '2014-10-01', 'Art', 'julia.anderson@mail.com'),
(211, 'Kevin', 'Thomas', '2015-12-15', 'Math', 'kevin.thomas@mail.com'),
(212, 'Laura', 'Jackson', '2016-03-05', 'English', 'laura.jackson@mail.com'),
(213, 'Michael', 'White', '2017-08-22', 'Science', 'michael.white@mail.com'),
(214, 'Nina', 'Harris', '2014-05-30', 'History', 'nina.harris@mail.com'),
(215, 'Oliver', 'Martin', '2018-01-18', 'Art', 'oliver.martin@mail.com'),
(216, 'Patricia', 'Thompson', '2015-06-12', 'Math', 'patricia.thompson@mail.com'),
(217, 'Quentin', 'Garcia', '2016-09-28', 'English', 'quentin.garcia@mail.com'),
(218, 'Rachel', 'Martinez', '2017-11-11', 'Science', 'rachel.martinez@mail.com'),
(219, 'Samuel', 'Robinson', '2014-03-05', 'History', 'samuel.robinson@mail.com'),
(220, 'Tina', 'Clark', '2018-07-22', 'Art', 'tina.clark@mail.com'),
(221, 'Umar', 'Rodriguez', '2015-04-10', 'Math', 'umar.rodriguez@mail.com'),
(222, 'Victoria', 'Lewis', '2016-08-01', 'English', 'victoria.lewis@mail.com'),
(223, 'William', 'Lee', '2017-05-19', 'Science', 'william.lee@mail.com'),
(224, 'Xena', 'Hall', '2014-12-03', 'History', 'xena.hall@mail.com'),
(225, 'Yara', 'Allen', '2018-02-14', 'Art', 'yara.allen@mail.com'),
(226, 'Zach', 'Young', '2015-09-17', 'Math', 'zach.young@mail.com'),
(227, 'Amy', 'King', '2016-06-30', 'English', 'amy.king@mail.com'),
(228, 'Brian', 'Wright', '2017-08-21', 'Science', 'brian.wright@mail.com'),
(229, 'Chloe', 'Scott', '2014-11-19', 'History', 'chloe.scott@mail.com'),
(230, 'David', 'Green', '2018-01-05', 'Art', 'david.green@mail.com'),
(231, 'Ella', 'Adams', '2015-03-20', 'Math', 'ella.adams@mail.com'),
(232, 'Frank', 'Baker', '2016-07-12', 'English', 'frank.baker@mail.com'),
(233, 'Grace', 'Gonzalez', '2017-09-05', 'Science', 'grace.gonzalez@mail.com'),
(234, 'Henry', 'Nelson', '2014-04-15', 'History', 'henry.nelson@mail.com'),
(235, 'Isabella', 'Carter', '2018-05-25', 'Art', 'isabella.carter@mail.com'),
(236, 'Jack', 'Mitchell', '2015-08-30', 'Math', 'jack.mitchell@mail.com'),
(237, 'Karen', 'Perez', '2016-02-18', 'English', 'karen.perez@mail.com'),
(238, 'Liam', 'Roberts', '2017-03-29', 'Science', 'liam.roberts@mail.com'),
(239, 'Mia', 'Turner', '2014-06-20', 'History', 'mia.turner@mail.com'),
(240, 'Noah', 'Phillips', '2018-07-08', 'Art', 'noah.phillips@mail.com'),
(241, 'Olivia', 'Campbell', '2015-05-11', 'Math', 'olivia.campbell@mail.com'),
(242, 'Peter', 'Parker', '2016-09-21', 'English', 'peter.parker@mail.com'),
(243, 'Queenie', 'Evans', '2017-01-14', 'Science', 'queenie.evans@mail.com'),
(244, 'Ryan', 'Edwards', '2014-08-30', 'History', 'ryan.edwards@mail.com'),
(245, 'Sophia', 'Collins', '2018-03-02', 'Art', 'sophia.collins@mail.com'),
(246, 'Thomas', 'Stewart', '2015-11-19', 'Math', 'thomas.stewart@mail.com'),
(247, 'Ursula', 'Sanchez', '2016-04-05', 'English', 'ursula.sanchez@mail.com'),
(248, 'Victor', 'Morris', '2017-07-28', 'Science', 'victor.morris@mail.com'),
(249, 'Wendy', 'Rogers', '2014-02-15', 'History', 'wendy.rogers@mail.com'),
(250, 'Xavier', 'Reed', '2018-06-12', 'Art', 'xavier.reed@mail.com');
```

### Table 3: classes
```
+------------+---------------+------+-----+---------+----------------+
| Field      | Type          | Null | Key | Default | Extra          |
+------------+---------------+------+-----+---------+----------------+
| class_id   | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| class_name | VARCHAR(50)   | NO   |     | NULL    |                |
| teacher_id | INT           | NO   | MUL | NULL    |                |
| room       | VARCHAR(20)   | YES  |     | NULL    |                |
| schedule   | VARCHAR(50)   | YES  |     | NULL    |                |
+------------+---------------+------+-----+---------+----------------+

+----------+----------------+------------+-------+----------------+
| class_id | class_name     | teacher_id | room  | schedule       |
+----------+----------------+------------+-------+----------------+
| 301      | Math 101       | 201        | R101  | Mon/Wed 9-10   |
| 302      | English 101    | 202        | R102  | Tue/Thu 10-11  |
| 303      | Science 101    | 203        | R103  | Mon/Wed 11-12  |
| 304      | History 101    | 204        | R104  | Tue/Thu 1-2    |
| 305      | Art 101        | 205        | R105  | Fri 9-11       |
| 306      | Math 102       | 206        | R106  | Mon/Wed 10-11  |
| 307      | English 102    | 207        | R107  | Tue/Thu 11-12  |
| 308      | Science 102    | 208        | R108  | Mon/Wed 1-2    |
| 309      | History 102    | 209        | R109  | Tue/Thu 2-3    |
| 310      | Art 102        | 210        | R110  | Fri 11-1       |
| 311      | Math 103       | 211        | R111  | Mon/Wed 2-3    |
| 312      | English 103    | 212        | R112  | Tue/Thu 9-10   |
| 313      | Science 103    | 213        | R113  | Mon/Wed 3-4    |
| 314      | History 103    | 214        | R114  | Tue/Thu 10-11  |
| 315      | Art 103        | 215        | R115  | Fri 1-3        |
| 316      | Math 104       | 216        | R116  | Mon/Wed 9-10   |
| 317      | English 104    | 217        | R117  | Tue/Thu 11-12  |
| 318      | Science 104    | 218        | R118  | Mon/Wed 10-11  |
| 319      | History 104    | 219        | R119  | Tue/Thu 1-2    |
| 320      | Art 104        | 220        | R120  | Fri 9-11       |
| 321      | Math 105       | 221        | R121  | Mon/Wed 2-3    |
| 322      | English 105    | 222        | R122  | Tue/Thu 2-3    |
| 323      | Science 105    | 223        | R123  | Mon/Wed 1-2    |
| 324      | History 105    | 224        | R124  | Tue/Thu 3-4    |
| 325      | Art 105        | 225        | R125  | Fri 11-1       |
| 326      | Math 106       | 226        | R126  | Mon/Wed 3-4    |
| 327      | English 106    | 227        | R127  | Tue/Thu 9-10   |
| 328      | Science 106    | 228        | R128  | Mon/Wed 11-12  |
| 329      | History 106    | 229        | R129  | Tue/Thu 1-2    |
| 330      | Art 106        | 230        | R130  | Fri 1-3        |
| 331      | Math 107       | 231        | R131  | Mon/Wed 9-10   |
| 332      | English 107    | 232        | R132  | Tue/Thu 10-11  |
| 333      | Science 107    | 233        | R133  | Mon/Wed 1-2    |
| 334      | History 107    | 234        | R134  | Tue/Thu 2-3    |
| 335      | Art 107        | 235        | R135  | Fri 9-11       |
| 336      | Math 108       | 236        | R136  | Mon/Wed 11-12  |
| 337      | English 108    | 237        | R137  | Tue/Thu 3-4    |
| 338      | Science 108    | 238        | R138  | Mon/Wed 3-4    |
| 339      | History 108    | 239        | R139  | Tue/Thu 1-2    |
| 340      | Art 108        | 240        | R140  | Fri 11-1       |
| 341      | Math 109       | 241        | R141  | Mon/Wed 2-3    |
| 342      | English 109    | 242        | R142  | Tue/Thu 9-10   |
| 343      | Science 109    | 243        | R143  | Mon/Wed 10-11  |
| 344      | History 109    | 244        | R144  | Tue/Thu 3-4    |
| 345      | Art 109        | 245        | R145  | Fri 1-3        |
| 346      | Math 110       | 246        | R146  | Mon/Wed 9-10   |
| 347      | English 110    | 247        | R147  | Tue/Thu 11-12  |
| 348      | Science 110    | 248        | R148  | Mon/Wed 1-2    |
| 349      | History 110    | 249        | R149  | Tue/Thu 2-3    |
| 350      | Art 110        | 250        | R150  | Fri 9-11       |
+----------+----------------+------------+-------+----------------+
```

```sql
CREATE TABLE classes (
    class_id INT NOT NULL AUTO_INCREMENT,
    class_name VARCHAR(50) NOT NULL,
    teacher_id INT NOT NULL,
    room VARCHAR(20),
    schedule VARCHAR(50),
    PRIMARY KEY (class_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
) ENGINE=InnoDB;

INSERT INTO classes (class_id, class_name, teacher_id, room, schedule)
VALUES
(301, 'Math 101', 201, 'R101', 'Mon/Wed 9-10'),
(302, 'English 101', 202, 'R102', 'Tue/Thu 10-11'),
(303, 'Science 101', 203, 'R103', 'Mon/Wed 11-12'),
(304, 'History 101', 204, 'R104', 'Tue/Thu 1-2'),
(305, 'Art 101', 205, 'R105', 'Fri 9-11'),
(306, 'Math 102', 206, 'R106', 'Mon/Wed 10-11'),
(307, 'English 102', 207, 'R107', 'Tue/Thu 11-12'),
(308, 'Science 102', 208, 'R108', 'Mon/Wed 1-2'),
(309, 'History 102', 209, 'R109', 'Tue/Thu 2-3'),
(310, 'Art 102', 210, 'R110', 'Fri 11-1'),
(311, 'Math 103', 211, 'R111', 'Mon/Wed 2-3'),
(312, 'English 103', 212, 'R112', 'Tue/Thu 9-10'),
(313, 'Science 103', 213, 'R113', 'Mon/Wed 3-4'),
(314, 'History 103', 214, 'R114', 'Tue/Thu 10-11'),
(315, 'Art 103', 215, 'R115', 'Fri 1-3'),
(316, 'Math 104', 216, 'R116', 'Mon/Wed 9-10'),
(317, 'English 104', 217, 'R117', 'Tue/Thu 11-12'),
(318, 'Science 104', 218, 'R118', 'Mon/Wed 10-11'),
(319, 'History 104', 219, 'R119', 'Tue/Thu 1-2'),
(320, 'Art 104', 220, 'R120', 'Fri 9-11'),
(321, 'Math 105', 221, 'R121', 'Mon/Wed 2-3'),
(322, 'English 105', 222, 'R122', 'Tue/Thu 2-3'),
(323, 'Science 105', 223, 'R123', 'Mon/Wed 1-2'),
(324, 'History 105', 224, 'R124', 'Tue/Thu 3-4'),
(325, 'Art 105', 225, 'R125', 'Fri 11-1'),
(326, 'Math 106', 226, 'R126', 'Mon/Wed 3-4'),
(327, 'English 106', 227, 'R127', 'Tue/Thu 9-10'),
(328, 'Science 106', 228, 'R128', 'Mon/Wed 11-12'),
(329, 'History 106', 229, 'R129', 'Tue/Thu 1-2'),
(330, 'Art 106', 230, 'R130', 'Fri 1-3'),
(331, 'Math 107', 231, 'R131', 'Mon/Wed 9-10'),
(332, 'English 107', 232, 'R132', 'Tue/Thu 10-11'),
(333, 'Science 107', 233, 'R133', 'Mon/Wed 1-2'),
(334, 'History 107', 234, 'R134', 'Tue/Thu 2-3'),
(335, 'Art 107', 235, 'R135', 'Fri 9-11'),
(336, 'Math 108', 236, 'R136', 'Mon/Wed 11-12'),
(337, 'English 108', 237, 'R137', 'Tue/Thu 3-4'),
(338, 'Science 108', 238, 'R138', 'Mon/Wed 3-4'),
(339, 'History 108', 239, 'R139', 'Tue/Thu 1-2'),
(340, 'Art 108', 240, 'R140', 'Fri 11-1'),
(341, 'Math 109', 241, 'R141', 'Mon/Wed 2-3'),
(342, 'English 109', 242, 'R142', 'Tue/Thu 9-10'),
(343, 'Science 109', 243, 'R143', 'Mon/Wed 10-11'),
(344, 'History 109', 244, 'R144', 'Tue/Thu 3-4'),
(345, 'Art 109', 245, 'R145', 'Fri 1-3'),
(346, 'Math 110', 246, 'R146', 'Mon/Wed 9-10'),
(347, 'English 110', 247, 'R147', 'Tue/Thu 11-12'),
(348, 'Science 110', 248, 'R148', 'Mon/Wed 1-2'),
(349, 'History 110', 249, 'R149', 'Tue/Thu 2-3'),
(350, 'Art 110', 250, 'R150', 'Fri 9-11');
```

### Table 4: enrollments
```
+---------------+--------+------+-----+---------+----------------+
| Field         | Type   | Null | Key | Default | Extra          |
+---------------+--------+------+-----+---------+----------------+
| enrollment_id | INT    | NO   | PRI | NULL    | AUTO_INCREMENT |
| student_id    | INT    | NO   | MUL | NULL    |                |
| class_id      | INT    | NO   | MUL | NULL    |                |
| enroll_date   | DATE   | NO   |     | NULL    |                |
+---------------+--------+------+-----+---------+----------------+

+--------------+-----------+----------+------------+
| enrollment_id| student_id| class_id | enroll_date|
+--------------+-----------+----------+------------+
| 401          | 101       | 301      | 2025-09-01 |
| 402          | 102       | 302      | 2025-09-01 |
| 403          | 103       | 303      | 2025-09-01 |
| 404          | 104       | 304      | 2025-09-01 |
| 405          | 105       | 305      | 2025-09-01 |
| 406          | 106       | 301      | 2025-09-02 |
| 407          | 107       | 302      | 2025-09-02 |
| 408          | 108       | 303      | 2025-09-02 |
| 409          | 109       | 304      | 2025-09-02 |
| 410          | 110       | 305      | 2025-09-02 |
| 411          | 111       | 306      | 2025-09-03 |
| 412          | 112       | 307      | 2025-09-03 |
| 413          | 113       | 308      | 2025-09-03 |
| 414          | 114       | 309      | 2025-09-03 |
| 415          | 115       | 310      | 2025-09-03 |
| 416          | 116       | 311      | 2025-09-04 |
| 417          | 117       | 312      | 2025-09-04 |
| 418          | 118       | 313      | 2025-09-04 |
| 419          | 119       | 314      | 2025-09-04 |
| 420          | 120       | 315      | 2025-09-04 |
| 421          | 121       | 316      | 2025-09-05 |
| 422          | 122       | 317      | 2025-09-05 |
| 423          | 123       | 318      | 2025-09-05 |
| 424          | 124       | 319      | 2025-09-05 |
| 425          | 125       | 320      | 2025-09-05 |
| 426          | 126       | 321      | 2025-09-06 |
| 427          | 127       | 322      | 2025-09-06 |
| 428          | 128       | 323      | 2025-09-06 |
| 429          | 129       | 324      | 2025-09-06 |
| 430          | 130       | 325      | 2025-09-06 |
| 431          | 131       | 326      | 2025-09-07 |
| 432          | 132       | 327      | 2025-09-07 |
| 433          | 133       | 328      | 2025-09-07 |
| 434          | 134       | 329      | 2025-09-07 |
| 435          | 135       | 330      | 2025-09-07 |
| 436          | 136       | 331      | 2025-09-08 |
| 437          | 137       | 332      | 2025-09-08 |
| 438          | 138       | 333      | 2025-09-08 |
| 439          | 139       | 334      | 2025-09-08 |
| 440          | 140       | 335      | 2025-09-08 |
| 441          | 141       | 336      | 2025-09-09 |
| 442          | 142       | 337      | 2025-09-09 |
| 443          | 143       | 338      | 2025-09-09 |
| 444          | 144       | 339      | 2025-09-09 |
| 445          | 145       | 340      | 2025-09-09 |
| 446          | 146       | 341      | 2025-09-10 |
| 447          | 147       | 342      | 2025-09-10 |
| 448          | 148       | 343      | 2025-09-10 |
| 449          | 149       | 344      | 2025-09-10 |
| 450          | 150       | 345      | 2025-09-10 |
+--------------+-----------+----------+------------+

```

```sql
CREATE TABLE enrollments (
    enrollment_id INT NOT NULL AUTO_INCREMENT,
    student_id INT NOT NULL,
    class_id INT NOT NULL,
    enroll_date DATE NOT NULL,
    PRIMARY KEY (enrollment_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (class_id) REFERENCES classes(class_id)
) ENGINE=InnoDB;

INSERT INTO enrollments (enrollment_id, student_id, class_id, enroll_date) VALUES
(401, 101, 301, '2025-09-01'),
(402, 102, 302, '2025-09-01'),
(403, 103, 303, '2025-09-01'),
(404, 104, 304, '2025-09-01'),
(405, 105, 305, '2025-09-01'),
(406, 106, 301, '2025-09-02'),
(407, 107, 302, '2025-09-02'),
(408, 108, 303, '2025-09-02'),
(409, 109, 304, '2025-09-02'),
(410, 110, 305, '2025-09-02'),
(411, 111, 306, '2025-09-03'),
(412, 112, 307, '2025-09-03'),
(413, 113, 308, '2025-09-03'),
(414, 114, 309, '2025-09-03'),
(415, 115, 310, '2025-09-03'),
(416, 116, 311, '2025-09-04'),
(417, 117, 312, '2025-09-04'),
(418, 118, 313, '2025-09-04'),
(419, 119, 314, '2025-09-04'),
(420, 120, 315, '2025-09-04'),
(421, 121, 316, '2025-09-05'),
(422, 122, 317, '2025-09-05'),
(423, 123, 318, '2025-09-05'),
(424, 124, 319, '2025-09-05'),
(425, 125, 320, '2025-09-05'),
(426, 126, 321, '2025-09-06'),
(427, 127, 322, '2025-09-06'),
(428, 128, 323, '2025-09-06'),
(429, 129, 324, '2025-09-06'),
(430, 130, 325, '2025-09-06'),
(431, 131, 326, '2025-09-07'),
(432, 132, 327, '2025-09-07'),
(433, 133, 328, '2025-09-07'),
(434, 134, 329, '2025-09-07'),
(435, 135, 330, '2025-09-07'),
(436, 136, 331, '2025-09-08'),
(437, 137, 332, '2025-09-08'),
(438, 138, 333, '2025-09-08'),
(439, 139, 334, '2025-09-08'),
(440, 140, 335, '2025-09-08'),
(441, 141, 336, '2025-09-09'),
(442, 142, 337, '2025-09-09'),
(443, 143, 338, '2025-09-09'),
(444, 144, 339, '2025-09-09'),
(445, 145, 340, '2025-09-09'),
(446, 146, 341, '2025-09-10'),
(447, 147, 342, '2025-09-10'),
(448, 148, 343, '2025-09-10'),
(449, 149, 344, '2025-09-10'),
(450, 150, 345, '2025-09-10');
```

### Table 5: grades
```
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| grade_id      | INT          | NO   | PRI | NULL    | AUTO_INCREMENT |
| enrollment_id | INT          | NO   | MUL | NULL    |                |
| grade         | CHAR(2)      | NO   |     | NULL    |                |
| score         | DECIMAL(5,2) | YES  |     | NULL    |                |
| grade_date    | DATE         | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+

+---------+---------------+-------+-------+------------+
| grade_id| enrollment_id | grade | score | grade_date |
+---------+---------------+-------+-------+------------+
| 501     | 401           | A     | 95.00 | 2025-12-01 |
| 502     | 402           | B+    | 88.50 | 2025-12-01 |
| 503     | 403           | A-    | 91.00 | 2025-12-01 |
| 504     | 404           | B     | 85.00 | 2025-12-01 |
| 505     | 405           | C+    | 78.00 | 2025-12-01 |
| 506     | 406           | B-    | 82.50 | 2025-12-02 |
| 507     | 407           | A     | 94.00 | 2025-12-02 |
| 508     | 408           | B+    | 89.00 | 2025-12-02 |
| 509     | 409           | A     | 96.00 | 2025-12-02 |
| 510     | 410           | B     | 84.00 | 2025-12-02 |
| 511     | 411           | C+    | 79.50 | 2025-12-03 |
| 512     | 412           | A-    | 92.00 | 2025-12-03 |
| 513     | 413           | B+    | 87.50 | 2025-12-03 |
| 514     | 414           | A     | 95.50 | 2025-12-03 |
| 515     | 415           | B     | 83.00 | 2025-12-03 |
| 516     | 416           | A     | 96.00 | 2025-12-04 |
| 517     | 417           | B+    | 88.00 | 2025-12-04 |
| 518     | 418           | A-    | 90.50 | 2025-12-04 |
| 519     | 419           | B     | 85.50 | 2025-12-04 |
| 520     | 420           | C+    | 78.50 | 2025-12-04 |
| 521     | 421           | A     | 94.50 | 2025-12-05 |
| 522     | 422           | B+    | 88.00 | 2025-12-05 |
| 523     | 423           | A-    | 91.50 | 2025-12-05 |
| 524     | 424           | B     | 84.50 | 2025-12-05 |
| 525     | 425           | C+    | 79.00 | 2025-12-05 |
| 526     | 426           | B-    | 82.00 | 2025-12-06 |
| 527     | 427           | A     | 95.00 | 2025-12-06 |
| 528     | 428           | B+    | 88.50 | 2025-12-06 |
| 529     | 429           | A-    | 91.00 | 2025-12-06 |
| 530     | 430           | B     | 85.00 | 2025-12-06 |
| 531     | 431           | C+    | 78.50 | 2025-12-07 |
| 532     | 432           | B     | 84.00 | 2025-12-07 |
| 533     | 433           | A     | 96.00 | 2025-12-07 |
| 534     | 434           | B+    | 88.00 | 2025-12-07 |
| 535     | 435           | A-    | 91.50 | 2025-12-07 |
| 536     | 436           | B     | 85.00 | 2025-12-08 |
| 537     | 437           | C+    | 79.00 | 2025-12-08 |
| 538     | 438           | A     | 95.50 | 2025-12-08 |
| 539     | 439           | B+    | 88.50 | 2025-12-08 |
| 540     | 440           | A-    | 91.00 | 2025-12-08 |
| 541     | 441           | B     | 84.50 | 2025-12-09 |
| 542     | 442           | A     | 96.00 | 2025-12-09 |
| 543     | 443           | B+    | 87.50 | 2025-12-09 |
| 544     | 444           | A-    | 92.00 | 2025-12-09 |
| 545     | 445           | B     | 83.50 | 2025-12-09 |
| 546     | 446           | A     | 95.00 | 2025-12-10 |
| 547     | 447           | B+    | 88.50 | 2025-12-10 |
| 548     | 448           | A-    | 91.50 | 2025-12-10 |
| 549     | 449           | B     | 85.00 | 2025-12-10 |
| 550     | 450           | C+    | 78.50 | 2025-12-10 |
+---------+---------------+-------+-------+------------+

```

```sql
CREATE TABLE grades (
    grade_id INT NOT NULL AUTO_INCREMENT,
    enrollment_id INT NOT NULL,
    grade CHAR(2) NOT NULL,
    score DECIMAL(5,2),
    grade_date DATE NOT NULL,
    PRIMARY KEY (grade_id),
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id)
) ENGINE=InnoDB;

INSERT INTO grades (grade_id, enrollment_id, grade, score, grade_date)VALUES
(501, 401, 'A', 95.00, '2025-12-01'),
(502, 402, 'B+', 88.50, '2025-12-01'),
(503, 403, 'A-', 91.00, '2025-12-01'),
(504, 404, 'B', 85.00, '2025-12-01'),
(505, 405, 'C+', 78.00, '2025-12-01'),
(506, 406, 'B-', 82.50, '2025-12-02'),
(507, 407, 'A', 94.00, '2025-12-02'),
(508, 408, 'B+', 89.00, '2025-12-02'),
(509, 409, 'A', 96.00, '2025-12-02'),
(510, 410, 'B', 84.00, '2025-12-02'),
(511, 411, 'C+', 79.50, '2025-12-03'),
(512, 412, 'A-', 92.00, '2025-12-03'),
(513, 413, 'B+', 87.50, '2025-12-03'),
(514, 414, 'A', 95.50, '2025-12-03'),
(515, 415, 'B', 83.00, '2025-12-03'),
(516, 416, 'A', 96.00, '2025-12-04'),
(517, 417, 'B+', 88.00, '2025-12-04'),
(518, 418, 'A-', 90.50, '2025-12-04'),
(519, 419, 'B', 85.50, '2025-12-04'),
(520, 420, 'C+', 78.50, '2025-12-04'),
(521, 421, 'A', 94.50, '2025-12-05'),
(522, 422, 'B+', 88.00, '2025-12-05'),
(523, 423, 'A-', 91.50, '2025-12-05'),
(524, 424, 'B', 84.50, '2025-12-05'),
(525, 425, 'C+', 79.00, '2025-12-05'),
(526, 426, 'B-', 82.00, '2025-12-06'),
(527, 427, 'A', 95.00, '2025-12-06'),
(528, 428, 'B+', 88.50, '2025-12-06'),
(529, 429, 'A-', 91.00, '2025-12-06'),
(530, 430, 'B', 85.00, '2025-12-06'),
(531, 431, 'C+', 78.50, '2025-12-07'),
(532, 432, 'B', 84.00, '2025-12-07'),
(533, 433, 'A', 96.00, '2025-12-07'),
(534, 434, 'B+', 88.00, '2025-12-07'),
(535, 435, 'A-', 91.50, '2025-12-07'),
(536, 436, 'B', 85.00, '2025-12-08'),
(537, 437, 'C+', 79.00, '2025-12-08'),
(538, 438, 'A', 95.50, '2025-12-08'),
(539, 439, 'B+', 88.50, '2025-12-08'),
(540, 440, 'A-', 91.00, '2025-12-08'),
(541, 441, 'B', 84.50, '2025-12-09'),
(542, 442, 'A', 96.00, '2025-12-09'),
(543, 443, 'B+', 87.50, '2025-12-09'),
(544, 444, 'A-', 92.00, '2025-12-09'),
(545, 445, 'B', 83.50, '2025-12-09'),
(546, 446, 'A', 95.00, '2025-12-10'),
(547, 447, 'B+', 88.50, '2025-12-10'),
(548, 448, 'A-', 91.50, '2025-12-10'),
(549, 449, 'B', 85.00, '2025-12-10'),
(550, 450, 'C+', 78.50, '2025-12-10');
```