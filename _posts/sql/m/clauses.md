

## **Clauses**
WHERE
ORDER BY
LIMIT

CREATE TABLE IF NOT EXISTS library(
	library_id INT PRIMARY KEY,
	student_id INT FOREIGN KEY,
	books VARCHAR(100) NOT NULL,
	fine FLOAT DEFAULT 0.0,
	age INT UNIQUE,
	CONSTRAINT age_check CHECK (age>=20)
);

**Creating a database**

**Creating a table**:
```sql
-- CREATE TABLE IF NOT EXISTS table_name;


```sql
CREATE TABLE IF NOT EXISTS practice;
	col INT,
	col2 VARCHAR(10)
	col3 INT,
	col4 FLOAT,
)
```

**Inserting data into table**:
```sql
INSERT INTO table_name
(field1, field2, field3, field4) VALUES
(value11, 'value12', 'value13', value14),
(value21, 'value22', 'value23, value24),
(value31, 'value32', 'value33', value34);
```

Dropping a database

Dropping a table
```sql
-- DROP TABLE database_name.table_name;
DROP TABLE test.tbl_test;


## Operators
**AND**:
**OR**
**NOT**
**Examples**:
```sql
SELECT * FROM library WHERE fine > 0; -- WHERE clause for setting conditions
SELECT * FROM library WHERE fine > 20 AND fine <50; -- setting multiple conditions with AND
SELECT * FROM library WHERE books = 'Pandas Basics' OR books = 'NumPy Basics';
SELECT * FROM library WHERE books NOT IN ('Pandas Basics');
```

**IN**
**BETWEEN**

**Examples**:
```sql
SELECT * FROM library WHERE books IN ('Pandas Basics', 'NumPy Basics');
SELECT * FROM library WHERE books NOT IN('Pandas Basics', 'NumPy Basics');
SELECT * FROM library WHERE age BETWEEN 25 AND 60;
```
