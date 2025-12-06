
## **🏥 Hospital Dataset Subquery Questions**

### **Set A**

#### **Basic (5)**
1. Find all patients whose age is greater than the average age of all patients. *(Non-Correlated, WHERE clause)*
2. List all patients whose age is equal to the maximum age in the table. *(Non-Correlated, WHERE clause)*
3. Retrieve the names of patients and the total number of patients in Kathmandu. *(Subquery in SELECT)*
4. List patients who live in the same city as ‘Anna Lee’. *(Correlated, WHERE clause)*
5. Show all patients who are younger than every male patient. *(Non-Correlated, WHERE clause with `< ALL`)*

#### **Intermediate (5)**
6. Find patients whose age is greater than the average age of patients in their city. *(Correlated, WHERE clause)*
7. List each city and the number of patients in that city. *(Subquery in FROM)*
8. Retrieve patient names along with the count of patients older than them. *(Correlated, SELECT clause)*
9. Show all patients whose age is between the minimum and maximum age of patients from Lalitpur. *(Non-Correlated, WHERE clause)*
10. List all patients whose age is above the average age of female patients. *(Non-Correlated, HAVING clause on aggregated subquery)*

#### **Advanced (5)**
11. Find patients whose age is greater than the average age of patients in the same city and same gender. *(Correlated, WHERE clause)*
12. List patients whose age is greater than the average age of patients older than them. *(Correlated, SELECT clause)*
13. Retrieve cities where the total number of patients is greater than the total number of patients in Kathmandu. *(Subquery in HAVING clause)*
14. Find patients whose age is above the average age of all patients who live in a city with more than 5 patients. *(Nested subquery in HAVING)*
15. List patients whose age is greater than the age of the youngest male patient in the same city. *(Correlated, WHERE clause)*

---

### **Set B**

#### **Basic (5)**

1. List all patients whose age is equal to the youngest patient. *(Non-Correlated, WHERE clause)*
2. Show patients who live in the same city as ‘Mark Kim’. *(Correlated, WHERE clause)*
3. Retrieve names of patients and total patients in each city. *(Subquery in SELECT)*
4. List patients whose age is less than the average age of all patients. *(Non-Correlated, WHERE clause)*
5. Find patients who are older than every patient in Bhaktapur. *(Non-Correlated, WHERE clause with `> ALL`)*

#### **Intermediate (5)**

6. Show patients older than the average age of patients of the same gender. *(Correlated, WHERE clause)*
7. Retrieve cities and average age of patients in each city. *(Subquery in FROM)*
8. List patients along with the number of patients younger than them. *(Correlated, SELECT clause)*
9. Find patients whose age is between the minimum and maximum age of patients from Pokhara. *(Non-Correlated, WHERE clause)*
10. Show patients whose age is above the average age of male patients. *(Non-Correlated, HAVING clause)*

#### **Advanced (5)**

11. Find patients whose age is greater than the average age of patients in the same city but opposite gender. *(Correlated, WHERE clause)*
12. List patients whose age is greater than the average age of patients older than themselves in the same city. *(Nested correlated, SELECT clause)*
13. Retrieve cities where total patients exceed the total number of patients in Lalitpur. *(Subquery in HAVING clause)*
14. Find patients whose age is greater than the age of the youngest patient living in cities with more than 4 patients. *(Nested subquery, WHERE clause)*
15. List patients whose age is greater than the average age of all patients with the same first letter in their name. *(Correlated, WHERE clause with string function)*