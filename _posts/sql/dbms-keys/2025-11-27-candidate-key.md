Perfect! Let’s rewrite **Candidate Key** in the **exact format** you requested:

---

### **Candidate Key**

**Definition:**
A **Candidate Key** is a **minimal set of columns that can uniquely identify each row** in a table. A table can have one or more candidate keys, but only one is selected as the primary key.

---

**Key Points:**

1. Must **uniquely identify** each row.
2. Must be **minimal** — no extra columns.
3. A table can have **multiple candidate keys**.
4. One candidate key is chosen as the **Primary Key**.
5. Remaining candidate keys become **Alternate Keys**.

---

**Example: SQL Code with Comments**

```sql
CREATE TABLE Employees (
    EmployeeID INT,                -- Candidate Key: can uniquely identify each employee
    Email VARCHAR(100) NOT NULL,   -- Candidate Key: also uniquely identifies an employee
    NationalID VARCHAR(20) NOT NULL -- Candidate Key: another unique identifier
);

-- Choosing Primary Key
ALTER TABLE Employees
ADD PRIMARY KEY (EmployeeID);      -- Primary Key selected from candidate keys

-- Alternate Keys (other candidate keys)
ALTER TABLE Employees
ADD UNIQUE (Email);               -- Email as alternate key
ALTER TABLE Employees
ADD UNIQUE (NationalID);          -- NationalID as alternate key
```

---

**Key Examples from Code:**

* **Candidate Keys:** `EmployeeID`, `Email`, `NationalID`
* **Primary Key:** `EmployeeID`
* **Alternate Keys:** `Email`, `NationalID`

---

**Relationship Summary:**

* **Super Key → Candidate Key → Primary/Alternate Key → Unique Key**
* Candidate Key is a **minimal super key**.
* Primary Key is **one chosen candidate key**.
* Alternate Keys are **other candidate keys**.
* All candidate and alternate keys are **unique keys**.

