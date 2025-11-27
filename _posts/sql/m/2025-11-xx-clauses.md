---
layout: post
title: SQL Clauses – SQL
author: Dipak Pulami Magar
date :  2025-11-26 16:12:45 +0545
categories: sql
status: draft
---

SQL clauses are fundamental components of SQL statements that define how data is retrieved, filtered, grouped, and organized within a database. 

They allow for precise control over data manipulation and retrieval.

Here are some of the most common and important SQL clauses:

## **SELECT:**
Specifies the columns to be retrieved from a table. It can also include expressions, aggregate functions, and aliases.


```sql
    SELECT column1, column2 FROM table_name;
```

## **FROM:**
Indicates the table or tables from which to retrieve data. This clause is essential for any query that accesses data.

```sql
    SELECT * FROM table_name;
```

## **WHERE:**
Filters rows based on specified conditions. Only rows that satisfy the conditions in the `WHERE` clause are included in the result set.

```sql
    SELECT column1 FROM table_name WHERE condition;
```

## **GROUP BY:**  
Groups rows that have the same values in specified columns into summary rows, typically with aggregate functions (e.g., `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`).

```sql
    SELECT column1, COUNT(column2) FROM table_name GROUP BY column1;
```

## **HAVING:**
Filters groups created by the `GROUP BY` clause based on aggregate function results. It functions similarly to `WHERE` but operates on grouped data.

```sql
    SELECT column1, COUNT(column2) FROM table_name GROUP BY column1 HAVING COUNT(column2) > 5;
```

## **ORDER BY:**  
Sorts the result set in ascending (`ASC`) or descending (`DESC`) order based on one or more columns.

```sql
-- SELECT column1, column2 FROM table_name ORDER BY column1 ASC;
```

## **JOIN:**  
Combines rows from two or more tables based on a related column between them. Common types include `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL OUTER JOIN`.

```sql
    SELECT t1.column1, t2.column2 FROM table1 t1 JOIN table2 t2 ON t1.id = t2.id;
```

## **WITH (Common Table Expression - CTE):**  
Defines a temporary, named result set that can be referenced within a single `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statement. It enhances readability and reusability for complex queries.

```sql
    WITH CTE_Name AS (SELECT column1 FROM table_name WHERE condition)
    SELECT * FROM CTE_Name;
```