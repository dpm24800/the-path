Perfect! Let’s generate **SQL solutions for all 30 subquery questions** based on your hospital dataset. I’ll follow the same **Set A and Set B** structure.

---

## **🏥 Set A – SQL Solutions**

### **Basic (5)**

1. **Patients older than average age**

```sql
SELECT name, age
FROM patients
WHERE age > (SELECT AVG(age) FROM patients);
```

2. **Patients with maximum age**

```sql
SELECT name, age
FROM patients
WHERE age = (SELECT MAX(age) FROM patients);
```

3. **Names of patients and total patients in Kathmandu**

```sql
SELECT name, 
       (SELECT COUNT(*) FROM patients WHERE address='Kathmandu') AS total_kathmandu_patients
FROM patients;
```

4. **Patients living in the same city as 'Anna Lee'**

```sql
SELECT name, address
FROM patients p1
WHERE address = (SELECT address FROM patients p2 WHERE p2.name='Anna Lee');
```

5. **Patients younger than every male patient**

```sql
SELECT name, age
FROM patients
WHERE age < ALL (SELECT age FROM patients WHERE gender='Male');
```

---

### **Intermediate (5)**

6. **Patients older than average age in their city**

```sql
SELECT name, age, address
FROM patients p1
WHERE age > (SELECT AVG(age) FROM patients p2 WHERE p2.address = p1.address);
```

7. **City and number of patients (subquery in FROM)**

```sql
SELECT city_stats.address, city_stats.patient_count
FROM (SELECT address, COUNT(*) AS patient_count FROM patients GROUP BY address) AS city_stats;
```

8. **Patient names with count of patients older than them**

```sql
SELECT p1.name,
       (SELECT COUNT(*) FROM patients p2 WHERE p2.age > p1.age) AS older_patients
FROM patients p1;
```

9. **Patients with age between min & max age of Lalitpur patients**

```sql
SELECT name, age
FROM patients
WHERE age BETWEEN (SELECT MIN(age) FROM patients WHERE address='Lalitpur')
              AND (SELECT MAX(age) FROM patients WHERE address='Lalitpur');
```

10. **Patients above average age of female patients**

```sql
SELECT name, age
FROM patients
GROUP BY gender, name, age
HAVING age > (SELECT AVG(age) FROM patients WHERE gender='Female');
```

---

### **Advanced (5)**

11. **Patients older than average age in same city and gender**

```sql
SELECT name, age, address, gender
FROM patients p1
WHERE age > (SELECT AVG(age) 
             FROM patients p2 
             WHERE p2.address=p1.address AND p2.gender=p1.gender);
```

12. **Patients older than average age of patients older than them**

```sql
SELECT name, age
FROM patients p1
WHERE age > (SELECT AVG(age) FROM patients p2 WHERE p2.age > p1.age);
```

13. **Cities with total patients greater than Kathmandu**

```sql
SELECT address
FROM patients
GROUP BY address
HAVING COUNT(*) > (SELECT COUNT(*) FROM patients WHERE address='Kathmandu');
```

14. **Patients above average age in cities with more than 5 patients**

```sql
SELECT name, age, address
FROM patients
WHERE age > (SELECT AVG(age) 
             FROM patients 
             WHERE address IN (SELECT address 
                               FROM patients 
                               GROUP BY address 
                               HAVING COUNT(*) > 5));
```

15. **Patients older than youngest male patient in the same city**

```sql
SELECT name, age, address
FROM patients p1
WHERE age > (SELECT MIN(age) 
             FROM patients p2 
             WHERE p2.address=p1.address AND p2.gender='Male');
```
