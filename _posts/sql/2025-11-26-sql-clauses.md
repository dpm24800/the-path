---
layout: post
title: SQL Clauses – SQL
author: Dipak Pulami Magar
date :  2025-11-26 16:12:45 +0545
categories: sql
status: draft
---

SQL provides clauses for filtering, sorting, and limiting the results of a query.

## 1. Filtering (WHERE clause):
The `WHERE` clause is used to extract only those records that fulfill a specified condition. This allows for selective retrieval of data based on criteria applied to one or more columns. Conditions can be combined using logical operators like `AND`, `OR`, and `NOT`.

**Syntax**:
```sql
SELECT column1, column2
FROM table_name
WHERE condition;
```

**Examples**:
```sql
-- Get customers who live in Kathmandu
SELECT * 
FROM Customers
WHERE City = 'Kathmandu';

-- Show orders where the total is greater than 5000
SELECT OrderID, TotalAmount
FROM Orders
WHERE TotalAmount > 5000;

-- List employees hired after 2023-01-01
SELECT Name, HireDate
FROM Employees
WHERE HireDate > '2023-01-01';

-- Only show products that are active
SELECT ProductName
FROM Products
WHERE Status <> 'Discontinued';

-- Filter only customers whose phone number is not empty
SELECT *
FROM Customers
WHERE Phone IS NOT NULL;

```

## 2. Sorting (ORDER BY clause):
The `ORDER BY` clause sorts the result set in ascending (`ASC`) or descending (`DESC`) order based on the values of one or more columns. By default, `ORDER BY` sorts in ascending order. Multiple columns can be specified for sorting, establishing a hierarchy of sorting criteria.
**Syntax**:
```sql
SELECT column1, column2
FROM table_name
ORDER BY column_name ASC|DESC;
```

**Examples**:
```sql
-- Show products sorted by price from highest to lowest
SELECT ProductName, Price
FROM Products
ORDER BY Price DESC;

-- Sort employees by their name in ascending order
SELECT EmployeeID, Name
FROM Employees
ORDER BY Name ASC;

-- Show newest orders at the top
SELECT OrderID, OrderDate
FROM Orders
ORDER BY OrderDate DESC;

-- Sort by grade first; if same grade, sort alphabetically
SELECT Name, Grade
FROM Students
ORDER BY Grade DESC, Name ASC;

-- Lowest stock products appear first
SELECT ProductName, Stock
FROM Inventory
ORDER BY Stock ASC;
```

## 3. Limiting (LIMIT clause):
The `LIMIT` clause restricts the number of rows returned by a query. 
It is typically used in conjunction with `ORDER BY` to retrieve a specific number of top or bottom records after sorting.
**Syntax**:
```sql
SELECT column1, column2
FROM table_name
LIMIT number_of_rows;
```
**Examples**:
```sql
-- Only display 5 products with highest price
SELECT ProductName, Price
FROM Products
ORDER BY Price DESC
LIMIT 5;

-- Get last 3 orders placed
SELECT OrderID, OrderDate
FROM Orders
ORDER BY OrderDate DESC
LIMIT 3;

-- Display the employee with the highest salary
SELECT Name, Salary
FROM Employees
ORDER BY Salary DESC
LIMIT 1;

-- Used to preview data during analysis
SELECT *
FROM Orders
LIMIT 10;

-- Get 20 customers who spent the most
SELECT CustomerID, TotalSpent
FROM Customers
ORDER BY TotalSpent DESC
LIMIT 20;

```

## 4. Combining Filtering, Sorting, and Limiting:
These clauses are often used together to achieve precise data retrieval. The general order of execution in a `SELECT` statement is `FROM`, `WHERE`, `GROUP BY` (if present), `HAVING` (if present), `SELECT`, `ORDER BY`, and finally `LIMIT`.

**Syntax**:
```sql
SELECT column1, column2
FROM table_name
WHERE condition
ORDER BY column_name ASC|DESC
LIMIT number_of_rows;
```

**Examples**:
```sql
-- Get top 5 orders from 2024 where:
-- (1) Order amount is above 10,000
-- (2) Payment status is 'Paid'
-- Sorted by amount from highest to lowest
SELECT OrderID, CustomerID, Amount, OrderDate
FROM Orders
WHERE Amount > 10000
  AND PaymentStatus = 'Paid'
  AND YEAR(OrderDate) = 2024
ORDER BY Amount DESC
LIMIT 5;


-- Show first 10 active employees who work in IT or Finance
-- Sorted by name alphabetically
SELECT EmployeeID, Name, Department, Status
FROM Employees
WHERE Status = 'Active'
  AND (Department = 'IT' OR Department = 'Finance')
ORDER BY Name ASC
LIMIT 10;


-- Get top 8 products:
-- (1) Price between 500 and 2000
-- (2) Stock is greater than 0
-- Sorted by price from low to high
SELECT ProductName, Price, Stock
FROM Products
WHERE Price BETWEEN 500 AND 2000
  AND Stock > 0
ORDER BY Price ASC
LIMIT 8;


-- Show 5 customers who:
-- (1) Have made at least 1 order
-- (2) Do NOT live in Kathmandu
-- Sorted by most spent
SELECT CustomerID, Name, City, TotalSpent
FROM Customers
WHERE TotalSpent > 0
  AND City <> 'Kathmandu'
ORDER BY TotalSpent DESC
LIMIT 5;


-- Show top 7 most recent deliveries which:
-- (1) Are NOT marked as 'Delivered'
-- (2) Are from the past 90 days
-- Sorted by delivery date (newest first)
SELECT DeliveryID, CustomerID, DeliveryDate, Status
FROM Deliveries
WHERE Status <> 'Delivered'
  AND DeliveryDate >= DATE_SUB(CURDATE(), INTERVAL 90 DAY)
ORDER BY DeliveryDate DESC
LIMIT 7;
```

**Further Readings**:
- [SQL - WHERE Clause](https://www.tutorialspoint.com/sql/sql-where-clause.htm)
- [SQL - ORDER BY Clause](https://www.tutorialspoint.com/sql/sql-order-by.htm)