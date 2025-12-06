# ✅ **LEFT JOIN SQL Answers**

---

## **1. List all patients and their appointments (include patients with no appointments).**

```sql
SELECT 
    p.patient_id,
    p.name AS patient_name,
    a.appointment_id,
    a.doctor_id,
    a.appointment_date
FROM patients p
LEFT JOIN appointments a
       ON p.patient_id = a.patient_id;
```

---

## **2. Show all doctors and the appointments they have (include doctors with no appointments).**

```sql
SELECT 
    d.doctor_id,
    d.name AS doctor_name,
    a.appointment_id,
    a.patient_id,
    a.appointment_date
FROM doctors d
LEFT JOIN appointments a
       ON d.doctor_id = a.doctor_id;
```

---

## **3. Get all patients and the medicines prescribed to them (include patients with no prescriptions).**

### (patients → appointments → prescriptions → medicines)

```sql
SELECT 
    p.patient_id,
    p.name AS patient_name,
    m.medicine_name
FROM patients p
LEFT JOIN appointments a 
       ON p.patient_id = a.patient_id
LEFT JOIN prescriptions pr
       ON a.appointment_id = pr.appointment_id
LEFT JOIN medicines m
       ON pr.medicine_id = m.medicine_id;
```

---

## **4. List all appointments and the corresponding prescriptions (include appointments without prescriptions).**

```sql
SELECT 
    a.appointment_id,
    a.patient_id,
    a.doctor_id,
    a.appointment_date,
    pr.prescription_id,
    pr.medicine_id,
    pr.dosage
FROM appointments a
LEFT JOIN prescriptions pr
       ON a.appointment_id = pr.appointment_id;
```

---

## **5. Show all doctors and the patients they have seen (include doctors who have not seen any patient).**

### (Doctors → Appointments → Patients)

```sql
SELECT 
    d.doctor_id,
    d.name AS doctor_name,
    p.patient_id,
    p.name AS patient_name
FROM doctors d
LEFT JOIN appointments a
       ON d.doctor_id = a.doctor_id
LEFT JOIN patients p
       ON a.patient_id = p.patient_id;
```