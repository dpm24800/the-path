
### Table 1: doctors
```
-- Table: doctors
+----------------+--------------+
| Field          | Type         |
+----------------+--------------+
| doctor_id      | INT          |
| name           | VARCHAR(50)  |
| specialty      | VARCHAR(50)  |
+----------------+--------------+

+-----------+-------------+-------------+
| doctor_id | name        | specialty   |
+-----------+-------------+-------------+
|         1 | Dr. Smith   | Cardiology  |
|         2 | Dr. Patel   | Neurology   |
|         3 | Dr. Johnson | Orthopedics |
|         4 | Dr. Lee     | Pediatrics  |
+-----------+-------------+-------------+
```

```sql
CREATE TABLE doctors (
    doctor_id INT PRIMARY KEY,
    name VARCHAR(50),
    specialty VARCHAR(50)
);

INSERT INTO doctors (doctor_id, name, specialty) VALUES
(1, 'Dr. Smith', 'Cardiology'),
(2, 'Dr. Patel', 'Neurology'),
(3, 'Dr. Johnson', 'Orthopedics'),
(4, 'Dr. Lee', 'Pediatrics');
```

---

### Table 2: patients

```
-- Table: patients
+----------------+---------------+
| Field          | Type          |
+----------------+---------------+
| patient_id     | INT           |
| name           | VARCHAR(50)   |
| age            | INT           |
| gender         | VARCHAR(10)   |
+----------------+---------------+

+------------+--------+------+--------+
| patient_id | name   | age  | gender |
+------------+--------+------+--------+
|        101 | Anna   |   30 | Female |
|        102 | Mark   |   45 | Male   |
|        103 | Sophie |   22 | Female |
|        104 | John   |   55 | Male   |
+------------+--------+------+--------+
```

```sql
CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    gender VARCHAR(10)
);

INSERT INTO patients (patient_id, name, age, gender) VALUES
(101, 'Anna', 30, 'Female'),
(102, 'Mark', 45, 'Male'),
(103, 'Sophie', 22, 'Female'),
(104, 'John', 55, 'Male');
```

---

### Table 3: appointments

```
-- Table: appointments
+------------------+---------------+
| Field            | Type          |
+------------------+---------------+
| appointment_id   | INT           |
| patient_id       | INT           |
| doctor_id        | INT           |
| date_            | DATE          |
+------------------+---------------+

+----------------+------------+-----------+------------+
| appointment_id | patient_id | doctor_id | date_      |
+----------------+------------+-----------+------------+
|           1001 |        101 |         1 | 2024-01-15 |
|           1002 |        102 |         1 | 2024-01-16 |
|           1003 |        103 |         2 | 2024-02-01 |
|           1004 |        104 |         3 | 2024-02-11 |
|           1005 |        101 |         4 | 2024-03-05 |
+----------------+------------+-----------+------------+
```

```sql
CREATE TABLE appointments (
    appointment_id INT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    date_ DATE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

INSERT INTO appointments (appointment_id, patient_id, doctor_id, date_) VALUES
(1001, 101, 1, '2024-01-15'),
(1002, 102, 1, '2024-01-16'),
(1003, 103, 2, '2024-02-01'),
(1004, 104, 3, '2024-02-11'),
(1005, 101, 4, '2024-03-05');
```

---
### Table 4: treatments
```
-- Table: treatments
+----------------+----------------+
| Field          | Type           |
+----------------+----------------+
| treatment_id   | INT            |
| appointment_id | INT            |
| description    | VARCHAR(100)   |
| cost           | INT            |
+----------------+----------------+

+--------------+----------------+----------------+------+
| treatment_id | appointment_id | description    | cost |
+--------------+----------------+----------------+------+
|         5001 |           1001 | Heart Checkup  |  200 |
|         5002 |           1003 | MRI Scan       |  600 |
|         5003 |           1004 | Bone X-Ray     |  150 |
|         5004 |           1005 | Vaccination    |  120 |
+--------------+----------------+----------------+------+
```

```sql
CREATE TABLE treatments (
    treatment_id INT PRIMARY KEY,
    appointment_id INT,
    description VARCHAR(100),
    cost INT,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id)
);

INSERT INTO treatments (treatment_id, appointment_id, description, cost) VALUES
(5001, 1001, 'Heart Checkup', 200),
(5002, 1003, 'MRI Scan', 600),
(5003, 1004, 'Bone X-Ray', 150),
(5004, 1005, 'Vaccination', 120);
```