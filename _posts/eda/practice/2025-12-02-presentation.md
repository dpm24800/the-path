---
layout: post
title: Presentation
description: 
# thumbnail: ../../../../assets/images/pandas/encoding-categorical-data.png
author: Dipak Pulami Magar
date:   2025-12-02 15:12:45 +0545
categories: pandas
status: published
---

```
"C:\Program Files\MySQL\MySQL Server 9.5\bin\mysql.exe" -u root -p
```

```sql
-- Find all distinct years
SELECT DISTINCT YEAR(date_received) AS year
FROM consumer_complaints
ORDER BY year;
```

```sql
-- Complaints in 2013
SELECT COUNT(date_received) AS records_2013 
FROM consumer_complaints  
WHERE date_received BETWEEN '2013-01-01' AND '2013-12-31';
```

```sql
-- Complaints in 2014
SELECT COUNT(date_received) AS records_2014 
FROM consumer_complaints 
WHERE date_received BETWEEN '2014-01-01' AND '2014-12-31';
```

```sql
-- Complaints in 2015
SELECT COUNT(date_received) AS records_2015 
FROM consumer_complaints 
WHERE date_received BETWEEN '2015-01-01' AND '2015-12-31';
```

```sql
-- Complaints by year (2013+2014+2015)
SELECT 
    YEAR(date_received) AS year,
    COUNT(*) AS total_complaints
FROM consumer_complaints
WHERE date_received BETWEEN '2013-01-01' AND '2015-12-31'
GROUP BY YEAR(date_received)
ORDER BY year;
```


```sql
-- Products
SELECT DISTINCT product_name As products
FROM consumer_complaints
ORDER BY product_name;
```
