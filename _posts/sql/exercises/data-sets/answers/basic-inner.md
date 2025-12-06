
## **🏥 Set B – SQL Solutions**

### **Basic (5)**

1. **Patients younger than average age of male patients**

```sql
SELECT name, age
FROM patients
WHERE age < (SELECT AVG(age) FROM patients WHERE gender='Male');
```

2. **Patients with minimum age**

```sql
SELECT name, age
FROM patients
WHERE age = (SELECT MIN(age) FROM patients);
```

3. **Patients with total number of patients in Bhaktapur**

```sql
SELECT name, 
       (SELECT COUNT(*) FROM patients WHERE address='Bhaktapur') AS total_bhaktapur_patients
FROM patients;
```

4. **Patients living in the same city as 'David Tan'**

```sql
SELECT name, address
FROM patients p1
WHERE address = (SELECT address FROM patients p2 WHERE p2.name='David Tan');
```

5. **Patients older than every female patient**

```sql
SELECT name, age
FROM patients
WHERE age > ALL (SELECT age FROM patients WHERE gender='Female');
```

---

### **Intermediate (5)**

6. **Patients younger than average age in their city**

```sql
SELECT name, age, address
FROM patients p1
WHERE age < (SELECT AVG(age) FROM patients p2 WHERE p2.address = p1.address);
```

7. **City and average age of patients (subquery in FROM)**

```sql
SELECT city_stats.address, city_stats.avg_age
FROM (SELECT address, AVG(age) AS avg_age FROM patients GROUP BY address) AS city_stats;
```

8. **Patient names with count of patients younger than them**

```sql
SELECT p1.name,
       (SELECT COUNT(*) FROM patients p2 WHERE p2.age < p1.age) AS younger_patients
FROM patients p1;
```

9. **Patients with age between min & max age of Pokhara patients**

```sql
SELECT name, age
FROM patients
WHERE age BETWEEN (SELECT MIN(age) FROM patients WHERE address='Pokhara')
              AND (SELECT MAX(age) FROM patients WHERE address='Pokhara');
```

10. **Patients above average age of male patients**

```sql
SELECT name, age
FROM patients
GROUP BY gender, name, age
HAVING age > (SELECT AVG(age) FROM patients WHERE gender='Male');
```

---

### **Advanced (5)**

11. **Patients older than average age in same city and opposite gender**

```sql
SELECT name, age, address, gender
FROM patients p1
WHERE age > (SELECT AVG(age) 
             FROM patients p2 
             WHERE p2.address=p1.address AND p2.gender<>p1.gender);
```

12. **Patients older than average age of patients younger than them**

```sql
SELECT name, age
FROM patients p1
WHERE age > (SELECT AVG(age) FROM patients p2 WHERE p2.age < p1.age);
```

13. **Cities with total patients less than Pokhara**

```sql
SELECT address
FROM patients
GROUP BY address
HAVING COUNT(*) < (SELECT COUNT(*) FROM patients WHERE address='Pokhara');
```

14. **Patients younger than average age in cities with fewer than 6 patients**

```sql
SELECT name, age, address
FROM patients
WHERE age < (SELECT AVG(age) 
             FROM patients 
             WHERE address IN (SELECT address 
                               FROM patients 
                               GROUP BY address 
                               HAVING COUNT(*) < 6));
```

15. **Patients younger than oldest female patient in the same city**

```sql
SELECT name, age, address
FROM patients p1
WHERE age < (SELECT MAX(age) 
             FROM patients p2 
             WHERE p2.address=p1.address AND p2.gender='Female');
```
