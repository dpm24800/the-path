# Sector 1. Hospital 
###  Table 1: patients

```
+------------+---------------+------+-----+---------+----------------+
| Field      | Type          | Null | Key | Default | Extra          |
+------------+---------------+------+-----+---------+----------------+
| patient_id | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| name       | VARCHAR(50)   | NO   |     | NULL    |                |
| age        | INT           | YES  |     | NULL    |                |
| gender     | VARCHAR(10)   | YES  |     | NULL    |                |
| phone      | VARCHAR(15)   | YES  |     | NULL    |                |
| address    | VARCHAR(100)  | YES  |     | NULL    |                |
+------------+---------------+------+-----+---------+----------------+

+------------+----------------+-----+--------+------------+-------------------+
| patient_id | name           | age | gender | phone      | address           |
+------------+----------------+-----+--------+------------+-------------------+
| 101        | Anna Lee       | 30  | Female | 9801234567| Kathmandu         |
| 102        | Mark Kim       | 45  | Male   | 9812345678| Lalitpur          |
| 103        | Sophie Li      | 22  | Female | 9823456789| Bhaktapur         |
| 104        | John Doe       | 55  | Male   | 9834567890| Pokhara           |
| 105        | Emily Ray      | 40  | Female | 9845678901| Kathmandu         |
| 106        | David Tan      | 35  | Male   | 9856789012| Lalitpur          |
| 107        | Rachel Wu      | 28  | Female | 9867890123| Bhaktapur         |
| 108        | Peter Pan      | 60  | Male   | 9878901234| Pokhara           |
| 109        | Lisa Green     | 33  | Female | 9809876543| Kathmandu         |
| 110        | James Brown    | 47  | Male   | 9818765432| Lalitpur          |
| 111        | Nancy White    | 25  | Female | 9827654321| Bhaktapur         |
| 112        | Tom Black      | 50  | Male   | 9836543210| Pokhara           |
| 113        | Carol Smith    | 38  | Female | 9845432109| Kathmandu         |
| 114        | Mike Johnson   | 42  | Male   | 9854321098| Lalitpur          |
| 115        | Amy Davis      | 29  | Female | 9863210987| Bhaktapur         |
| 116        | Brian Lee      | 55  | Male   | 9872109876| Pokhara           |
| 117        | Laura Kim      | 36  | Female | 9801098765| Kathmandu         |
| 118        | Kevin Tan      | 41  | Male   | 9810987654| Lalitpur          |
| 119        | Tina Wu        | 27  | Female | 9829876543| Bhaktapur         |
| 120        | Adam Pan       | 53  | Male   | 9838765432| Pokhara           |
| 121        | Eva Green      | 34  | Female | 9847654321| Kathmandu         |
| 122        | Ryan Brown     | 46  | Male   | 9856543210| Lalitpur          |
| 123        | Chloe White    | 23  | Female | 9865432109| Bhaktapur         |
| 124        | Eric Black     | 51  | Male   | 9874321098| Pokhara           |
| 125        | Grace Smith    | 37  | Female | 9803210987| Kathmandu         |
| 126        | Jason Johnson  | 43  | Male   | 9812109876| Lalitpur          |
| 127        | Olivia Davis   | 26  | Female | 9821098765| Bhaktapur         |
| 128        | Frank Lee      | 56  | Male   | 9830987654| Pokhara           |
| 129        | Sophia Kim     | 32  | Female | 9849876543| Kathmandu         |
| 130        | Daniel Tan     | 44  | Male   | 9858765432| Lalitpur          |
| 131        | Mia Wu         | 24  | Female | 9867654321| Bhaktapur         |
| 132        | Leo Pan        | 52  | Male   | 9876543210| Pokhara           |
| 133        | Ella Green     | 39  | Female | 9805432109| Kathmandu         |
| 134        | Jack Brown     | 48  | Male   | 9814321098| Lalitpur          |
| 135        | Lily White     | 28  | Female | 9823210987| Bhaktapur         |
| 136        | Henry Black    | 57  | Male   | 9832109876| Pokhara           |
| 137        | Zoe Smith      | 31  | Female | 9841098765| Kathmandu         |
| 138        | Paul Johnson   | 45  | Male   | 9850987654| Lalitpur          |
| 139        | Ava Davis      | 29  | Female | 9869876543| Bhaktapur         |
| 140        | Owen Lee       | 54  | Male   | 9878765432| Pokhara           |
| 141        | Ruby Kim       | 33  | Female | 9807654321| Kathmandu         |
| 142        | Sean Tan       | 49  | Male   | 9816543210| Lalitpur          |
| 143        | Ella Wu        | 27  | Female | 9825432109| Bhaktapur         |
| 144        | Luke Pan       | 55  | Male   | 9834321098| Pokhara           |
| 145        | Ivy Green      | 35  | Female | 9843210987| Kathmandu         |
| 146        | Carl Brown     | 46  | Male   | 9852109876| Lalitpur          |
| 147        | Emma White     | 22  | Female | 9861098765| Bhaktapur         |
| 148        | Mark Black     | 50  | Male   | 9870987654| Pokhara           |
| 149        | Sophie Smith   | 38  | Female | 9809876543| Kathmandu         |
| 150        | Adam Johnson   | 41  | Male   | 9818765432| Lalitpur          |
+------------+----------------+-----+--------+------------+-------------------+
```

```sql
CREATE TABLE patients (
    patient_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    age INT,
    gender VARCHAR(10),
    phone VARCHAR(15),
    address VARCHAR(100),
    PRIMARY KEY (patient_id)
) ENGINE=InnoDB;

INSERT INTO patients (name, age, gender, phone, address) VALUES
('Anna Lee', 30, 'Female', '9801234567', 'Kathmandu'),
('Mark Kim', 45, 'Male', '9812345678', 'Lalitpur'),
('Sophie Li', 22, 'Female', '9823456789', 'Bhaktapur'),
('John Doe', 55, 'Male', '9834567890', 'Pokhara'),
('Emily Ray', 40, 'Female', '9845678901', 'Kathmandu'),
('David Tan', 35, 'Male', '9856789012', 'Lalitpur'),
('Rachel Wu', 28, 'Female', '9867890123', 'Bhaktapur'),
('Peter Pan', 60, 'Male', '9878901234', 'Pokhara'),
('Lisa Green', 33, 'Female', '9809876543', 'Kathmandu'),
('James Brown', 47, 'Male', '9818765432', 'Lalitpur'),
('Nancy White', 25, 'Female', '9827654321', 'Bhaktapur'),
('Tom Black', 50, 'Male', '9836543210', 'Pokhara'),
('Carol Smith', 38, 'Female', '9845432109', 'Kathmandu'),
('Mike Johnson', 42, 'Male', '9854321098', 'Lalitpur'),
('Amy Davis', 29, 'Female', '9863210987', 'Bhaktapur'),
('Brian Lee', 55, 'Male', '9872109876', 'Pokhara'),
('Laura Kim', 36, 'Female', '9801098765', 'Kathmandu'),
('Kevin Tan', 41, 'Male', '9810987654', 'Lalitpur'),
('Tina Wu', 27, 'Female', '9829876543', 'Bhaktapur'),
('Adam Pan', 53, 'Male', '9838765432', 'Pokhara'),
('Eva Green', 34, 'Female', '9847654321', 'Kathmandu'),
('Ryan Brown', 46, 'Male', '9856543210', 'Lalitpur'),
('Chloe White', 23, 'Female', '9865432109', 'Bhaktapur'),
('Eric Black', 51, 'Male', '9874321098', 'Pokhara'),
('Grace Smith', 37, 'Female', '9803210987', 'Kathmandu'),
('Jason Johnson', 43, 'Male', '9812109876', 'Lalitpur'),
('Olivia Davis', 26, 'Female', '9821098765', 'Bhaktapur'),
('Frank Lee', 56, 'Male', '9830987654', 'Pokhara'),
('Sophia Kim', 32, 'Female', '9849876543', 'Kathmandu'),
('Daniel Tan', 44, 'Male', '9858765432', 'Lalitpur'),
('Mia Wu', 24, 'Female', '9867654321', 'Bhaktapur'),
('Leo Pan', 52, 'Male', '9876543210', 'Pokhara'),
('Ella Green', 39, 'Female', '9805432109', 'Kathmandu'),
('Jack Brown', 48, 'Male', '9814321098', 'Lalitpur'),
('Lily White', 28, 'Female', '9823210987', 'Bhaktapur'),
('Henry Black', 57, 'Male', '9832109876', 'Pokhara'),
('Zoe Smith', 31, 'Female', '9841098765', 'Kathmandu'),
('Paul Johnson', 45, 'Male', '9850987654', 'Lalitpur'),
('Ava Davis', 29, 'Female', '9869876543', 'Bhaktapur'),
('Owen Lee', 54, 'Male', '9878765432', 'Pokhara'),
('Ruby Kim', 33, 'Female', '9807654321', 'Kathmandu'),
('Sean Tan', 49, 'Male', '9816543210', 'Lalitpur'),
('Ella Wu', 27, 'Female', '9825432109', 'Bhaktapur'),
('Luke Pan', 55, 'Male', '9834321098', 'Pokhara'),
('Ivy Green', 35, 'Female', '9843210987', 'Kathmandu'),
('Carl Brown', 46, 'Male', '9852109876', 'Lalitpur'),
('Emma White', 22, 'Female', '9861098765', 'Bhaktapur'),
('Mark Black', 50, 'Male', '9870987654', 'Pokhara'),
('Sophie Smith', 38, 'Female', '9809876543', 'Kathmandu'),
('Adam Johnson', 41, 'Male', '9818765432', 'Lalitpur');
```

### Table 2. doctors

```
+-----------+---------------+------+-----+---------+----------------+
| Field     | Type          | Null | Key | Default | Extra          |
+-----------+---------------+------+-----+---------+----------------+
| doctor_id | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| name      | VARCHAR(50)   | NO   |     | NULL    |                |
| specialty | VARCHAR(50)   | NO   |     | NULL    |                |
| phone     | VARCHAR(15)   | YES  |     | NULL    |                |
| department| VARCHAR(50)   | YES  |     | NULL    |                |
+-----------+---------------+------+-----+---------+----------------+

+-----------+----------------+----------------+------------+-------------+
| doctor_id | name           | specialty      | phone      | department  |
+-----------+----------------+----------------+------------+-------------+
| 201       | Dr. Smith      | Cardiology     | 9801110001 | Heart       |
| 202       | Dr. Allen      | Neurology      | 9801110002 | Brain       |
| 203       | Dr. Wong       | Pediatrics     | 9801110003 | Children    |
| 204       | Dr. Khan       | Orthopedic     | 9801110004 | Bones       |
| 205       | Dr. Roy        | ENT            | 9801110005 | ENT         |
| 206       | Dr. Patel      | Dermatology    | 9801110006 | Skin        |
| 207       | Dr. Mehta      | Gastroenterology|9801110007 | Digestive  |
| 208       | Dr. Gupta      | Oncology       | 9801110008 | Cancer      |
| 209       | Dr. Sharma     | Ophthalmology  | 9801110009 | Eye         |
| 210       | Dr. Iyer       | Psychiatry     | 9801110010 | Mental      |
| 211       | Dr. Das        | Cardiology     | 9801110011 | Heart       |
| 212       | Dr. Reddy      | Neurology      | 9801110012 | Brain       |
| 213       | Dr. Choudhury  | Pediatrics     | 9801110013 | Children    |
| 214       | Dr. Nair       | Orthopedic     | 9801110014 | Bones       |
| 215       | Dr. Singh      | ENT            | 9801110015 | ENT         |
| 216       | Dr. Verma      | Dermatology    | 9801110016 | Skin        |
| 217       | Dr. Joshi      | Gastroenterology|9801110017 | Digestive  |
| 218       | Dr. Kapoor     | Oncology       | 9801110018 | Cancer      |
| 219       | Dr. Ramesh     | Ophthalmology  | 9801110019 | Eye         |
| 220       | Dr. Bhat       | Psychiatry     | 9801110020 | Mental      |
| 221       | Dr. Rao        | Cardiology     | 9801110021 | Heart       |
| 222       | Dr. Kaur       | Neurology      | 9801110022 | Brain       |
| 223       | Dr. Mehra      | Pediatrics     | 9801110023 | Children    |
| 224       | Dr. Joshi      | Orthopedic     | 9801110024 | Bones       |
| 225       | Dr. Sinha      | ENT            | 9801110025 | ENT         |
| 226       | Dr. Raju       | Dermatology    | 9801110026 | Skin        |
| 227       | Dr. Verma      | Gastroenterology|9801110027 | Digestive  |
| 228       | Dr. Dutta      | Oncology       | 9801110028 | Cancer      |
| 229       | Dr. Nair       | Ophthalmology  | 9801110029 | Eye         |
| 230       | Dr. Sharma     | Psychiatry     | 9801110030 | Mental      |
| 231       | Dr. Mehta      | Cardiology     | 9801110031 | Heart       |
| 232       | Dr. Gupta      | Neurology      | 9801110032 | Brain       |
| 233       | Dr. Khan       | Pediatrics     | 9801110033 | Children    |
| 234       | Dr. Roy        | Orthopedic     | 9801110034 | Bones       |
| 235       | Dr. Patel      | ENT            | 9801110035 | ENT         |
| 236       | Dr. Allen      | Dermatology    | 9801110036 | Skin        |
| 237       | Dr. Smith      | Gastroenterology|9801110037 | Digestive  |
| 238       | Dr. Reddy      | Oncology       | 9801110038 | Cancer      |
| 239       | Dr. Das        | Ophthalmology  | 9801110039 | Eye         |
| 240       | Dr. Choudhury  | Psychiatry     | 9801110040 | Mental      |
| 241       | Dr. Iyer       | Cardiology     | 9801110041 | Heart       |
| 242       | Dr. Sharma     | Neurology      | 9801110042 | Brain       |
| 243       | Dr. Kapoor     | Pediatrics     | 9801110043 | Children    |
| 244       | Dr. Singh      | Orthopedic     | 9801110044 | Bones       |
| 245       | Dr. Ramesh     | ENT            | 9801110045 | ENT         |
| 246       | Dr. Joshi      | Dermatology    | 9801110046 | Skin        |
| 247       | Dr. Bhat       | Gastroenterology|9801110047 | Digestive  |
| 248       | Dr. Mehra      | Oncology       | 9801110048 | Cancer      |
| 249       | Dr. Nair       | Ophthalmology  | 9801110049 | Eye         |
| 250       | Dr. Verma      | Psychiatry     | 9801110050 | Mental      |
+-----------+----------------+----------------+------------+-------------+
```

```sql
CREATE TABLE doctors (
    doctor_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    specialty VARCHAR(50) NOT NULL,
    phone VARCHAR(15),
    department VARCHAR(50),
    PRIMARY KEY (doctor_id)
) ENGINE=InnoDB;

INSERT INTO doctors (name, specialty, phone, department) VALUES
-- ('Dr. Smith','Cardiology','9801110001','Heart'),
-- ('Dr. Allen','Neurology','9801110002','Brain'),
-- ('Dr. Wong','Pediatrics','9801110003','Children'),
-- ('Dr. Khan','Orthopedic','9801110004','Bones'),
-- ('Dr. Roy','ENT','9801110005','ENT'),
-- ('Dr. Patel','Dermatology','9801110006','Skin'),
-- ('Dr. Mehta','Gastroenterology','9801110007','Digestive'),
-- ('Dr. Gupta','Oncology','9801110008','Cancer'),
-- ('Dr. Sharma','Ophthalmology','9801110009','Eye'),
-- ('Dr. Iyer','Psychiatry','9801110010','Mental');
('Dr. Das','Cardiology','9801110011','Heart'),
('Dr. Reddy','Neurology','9801110012','Brain'),
('Dr. Choudhury','Pediatrics','9801110013','Children'),
('Dr. Nair','Orthopedic','9801110014','Bones'),
('Dr. Singh','ENT','9801110015','ENT'),
('Dr. Verma','Dermatology','9801110016','Skin'),
('Dr. Joshi','Gastroenterology','9801110017','Digestive'),
('Dr. Kapoor','Oncology','9801110018','Cancer'),
('Dr. Ramesh','Ophthalmology','9801110019','Eye'),
('Dr. Bhat','Psychiatry','9801110020','Mental');
-- ('Dr. Rao','Cardiology','9801110021','Heart'),
-- ('Dr. Kaur','Neurology','9801110022','Brain'),
-- ('Dr. Mehra','Pediatrics','9801110023','Children'),
-- ('Dr. Joshi','Orthopedic','9801110024','Bones'),
-- ('Dr. Sinha','ENT','9801110025','ENT'),
-- ('Dr. Raju','Dermatology','9801110026','Skin'),
-- ('Dr. Verma','Gastroenterology','9801110027','Digestive'),
-- ('Dr. Dutta','Oncology','9801110028','Cancer'),
-- ('Dr. Nair','Ophthalmology','9801110029','Eye'),
-- ('Dr. Sharma','Psychiatry','9801110030','Mental'),
-- ('Dr. Mehta','Cardiology','9801110031','Heart'),
-- ('Dr. Gupta','Neurology','9801110032','Brain'),
-- ('Dr. Khan','Pediatrics','9801110033','Children'),
-- ('Dr. Roy','Orthopedic','9801110034','Bones'),
-- ('Dr. Patel','ENT','9801110035','ENT'),
-- ('Dr. Allen','Dermatology','9801110036','Skin'),
-- ('Dr. Smith','Gastroenterology','9801110037','Digestive'),
-- ('Dr. Reddy','Oncology','9801110038','Cancer'),
-- ('Dr. Das','Ophthalmology','9801110039','Eye'),
-- ('Dr. Choudhury','Psychiatry','9801110040','Mental'),
-- ('Dr. Iyer','Cardiology','9801110041','Heart'),
-- ('Dr. Sharma','Neurology','9801110042','Brain'),
-- ('Dr. Kapoor','Pediatrics','9801110043','Children'),
-- ('Dr. Singh','Orthopedic','9801110044','Bones'),
-- ('Dr. Ramesh','ENT','9801110045','ENT'),
-- ('Dr. Joshi','Dermatology','9801110046','Skin'),
-- ('Dr. Bhat','Gastroenterology','9801110047','Digestive'),
-- ('Dr. Mehra','Oncology','9801110048','Cancer'),
-- ('Dr. Nair','Ophthalmology','9801110049','Eye'),
-- ('Dr. Verma','Psychiatry','9801110050','Mental');
```

### Table 3: appointments

```
+-----------------+------------+------+-----+---------+----------------+
| Field           | Type       | Null | Key | Default | Extra          |
+-----------------+------------+------+-----+---------+----------------+
| appointment_id  | INT        | NO   | PRI | NULL    | AUTO_INCREMENT |
| patient_id      | INT        | NO   | MUL | NULL    |                |
| doctor_id       | INT        | NO   | MUL | NULL    |                |
| appointment_date| DATE       | NO   |     | NULL    |                |
| status          | VARCHAR(20)| YES  |     | 'Pending' |              |
+-----------------+------------+------+-----+---------+----------------+

+----------------+------------+-----------+----------------+-----------+
| appointment_id | patient_id | doctor_id | appointment_date| status    |
+----------------+------------+-----------+----------------+-----------+
| 301            | 101        | 201       | 2025-12-01     | Completed |
| 302            | 102        | 202       | 2025-12-02     | Pending   |
| 303            | 103        | 203       | 2025-12-03     | Completed |
| 304            | 104        | 204       | 2025-12-04     | Cancelled |
| 305            | 105        | 205       | 2025-12-05     | Completed |
| 306            | 106        | 206       | 2025-12-06     | Pending   |
| 307            | 107        | 207       | 2025-12-07     | Completed |
| 308            | 108        | 208       | 2025-12-08     | Completed |
| 309            | 109        | 209       | 2025-12-09     | Cancelled |
| 310            | 110        | 210       | 2025-12-10     | Completed |
| 311            | 111        | 201       | 2025-12-11     | Pending   |
| 312            | 112        | 202       | 2025-12-12     | Completed |
| 313            | 113        | 203       | 2025-12-13     | Completed |
| 314            | 114        | 204       | 2025-12-14     | Cancelled |
| 315            | 115        | 205       | 2025-12-15     | Completed |
| 316            | 116        | 206       | 2025-12-16     | Pending   |
| 317            | 117        | 207       | 2025-12-17     | Completed |
| 318            | 118        | 208       | 2025-12-18     | Completed |
| 319            | 119        | 209       | 2025-12-19     | Cancelled |
| 320            | 120        | 210       | 2025-12-20     | Completed |
| 321            | 121        | 201       | 2025-12-21     | Completed |
| 322            | 122        | 202       | 2025-12-22     | Pending   |
| 323            | 123        | 203       | 2025-12-23     | Completed |
| 324            | 124        | 204       | 2025-12-24     | Completed |
| 325            | 125        | 205       | 2025-12-25     | Cancelled |
| 326            | 126        | 206       | 2025-12-26     | Completed |
| 327            | 127        | 207       | 2025-12-27     | Completed |
| 328            | 128        | 208       | 2025-12-28     | Pending   |
| 329            | 129        | 209       | 2025-12-29     | Completed |
| 330            | 130        | 210       | 2025-12-30     | Completed |
| 331            | 131        | 201       | 2025-12-31     | Cancelled |
| 332            | 132        | 202       | 2026-01-01     | Completed |
| 333            | 133        | 203       | 2026-01-02     | Completed |
| 334            | 134        | 204       | 2026-01-03     | Completed |
| 335            | 135        | 205       | 2026-01-04     | Pending   |
| 336            | 136        | 206       | 2026-01-05     | Completed |
| 337            | 137        | 207       | 2026-01-06     | Completed |
| 338            | 138        | 208       | 2026-01-07     | Cancelled |
| 339            | 139        | 209       | 2026-01-08     | Completed |
| 340            | 140        | 210       | 2026-01-09     | Completed |
| 341            | 141        | 201       | 2026-01-10     | Pending   |
| 342            | 142        | 202       | 2026-01-11     | Completed |
| 343            | 143        | 203       | 2026-01-12     | Completed |
| 344            | 144        | 204       | 2026-01-13     | Cancelled |
| 345            | 145        | 205       | 2026-01-14     | Completed |
| 346            | 146        | 206       | 2026-01-15     | Pending   |
| 347            | 147        | 207       | 2026-01-16     | Completed |
| 348            | 148        | 208       | 2026-01-17     | Completed |
| 349            | 149        | 209       | 2026-01-18     | Cancelled |
| 350            | 150        | 210       | 2026-01-19     | Completed |
+----------------+------------+-----------+----------------+-----------+
```

```sql
CREATE TABLE appointments (
    appointment_id INT NOT NULL AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending',
    PRIMARY KEY (appointment_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
) ENGINE=InnoDB;

INSERT INTO appointments (patient_id, doctor_id, appointment_date, status) VALUES
(101,201,'2025-12-01','Completed'),
(102,202,'2025-12-02','Pending'),
(103,203,'2025-12-03','Completed'),
(104,204,'2025-12-04','Cancelled'),
(105,205,'2025-12-05','Completed'),
(106,206,'2025-12-06','Pending'),
(107,207,'2025-12-07','Completed'),
(108,208,'2025-12-08','Completed'),
(109,209,'2025-12-09','Cancelled'),
(110,210,'2025-12-10','Completed'),
(111,201,'2025-12-11','Pending'),
(112,202,'2025-12-12','Completed'),
(113,203,'2025-12-13','Completed'),
(114,204,'2025-12-14','Cancelled'),
(115,205,'2025-12-15','Completed'),
(116,206,'2025-12-16','Pending'),
(117,207,'2025-12-17','Completed'),
(118,208,'2025-12-18','Completed'),
(119,209,'2025-12-19','Cancelled'),
(120,210,'2025-12-20','Completed'),
(121,201,'2025-12-21','Completed'),
(122,202,'2025-12-22','Pending'),
(123,203,'2025-12-23','Completed'),
(124,204,'2025-12-24','Completed'),
(125,205,'2025-12-25','Cancelled'),
(126,206,'2025-12-26','Completed'),
(127,207,'2025-12-27','Completed'),
(128,208,'2025-12-28','Pending'),
(129,209,'2025-12-29','Completed'),
(130,210,'2025-12-30','Completed'),
(131,201,'2025-12-31','Cancelled'),
(132,202,'2026-01-01','Completed'),
(133,203,'2026-01-02','Completed'),
(134,204,'2026-01-03','Completed'),
(135,205,'2026-01-04','Pending'),
(136,206,'2026-01-05','Completed'),
(137,207,'2026-01-06','Completed'),
(138,208,'2026-01-07','Cancelled'),
(139,209,'2026-01-08','Completed'),
(140,210,'2026-01-09','Completed'),
(141,201,'2026-01-10','Pending'),
(142,202,'2026-01-11','Completed'),
(143,203,'2026-01-12','Completed'),
(144,204,'2026-01-13','Cancelled'),
(145,205,'2026-01-14','Completed'),
(146,206,'2026-01-15','Pending'),
(147,207,'2026-01-16','Completed'),
(148,208,'2026-01-17','Completed'),
(149,209,'2026-01-18','Cancelled'),
(150,210,'2026-01-19','Completed');

```

### Table 4: prescriptions
```
+-------------------+---------------+------+-----+---------+----------------+
| Field             | Type          | Null | Key | Default | Extra          |
+-------------------+---------------+------+-----+---------+----------------+
| prescription_id   | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| appointment_id    | INT           | NO   | MUL | NULL    |                |
| medicine_name     | VARCHAR(50)   | NO   |     | NULL    |                |
| dosage            | VARCHAR(50)   | YES  |     | NULL    |                |
| duration_days     | INT           | YES  |     | NULL    |                |
| notes             | VARCHAR(200)  | YES  |     | NULL    |                |
+-------------------+---------------+------+-----+---------+----------------+

+----------------+----------------+----------------+--------+---------------+---------------------------+
| prescription_id| appointment_id | medicine_name  | dosage | duration_days | notes                     |
+----------------+----------------+----------------+--------+---------------+---------------------------+
| 401            | 301            | Paracetamol    | 500mg  | 5             | Take after meals          |
| 402            | 302            | Ibuprofen      | 400mg  | 7             | Take with water           |
| 403            | 303            | Amoxicillin    | 250mg  | 10            | Morning and evening       |
| 404            | 304            | Metformin      | 500mg  | 30            | For diabetes              |
| 405            | 305            | Omeprazole     | 20mg   | 14            | Before breakfast          |
| 406            | 306            | Cetirizine     | 10mg   | 7             | For allergy               |
| 407            | 307            | Amlodipine     | 5mg    | 30            | Blood pressure            |
| 408            | 308            | Azithromycin   | 500mg  | 3             | Take once daily           |
| 409            | 309            | Paracetamol    | 500mg  | 5             | Take after meals          |
| 410            | 310            | Ibuprofen      | 400mg  | 7             | Take with water           |
| 411            | 311            | Amoxicillin    | 250mg  | 10            | Morning and evening       |
| 412            | 312            | Metformin      | 500mg  | 30            | For diabetes              |
| 413            | 313            | Omeprazole     | 20mg   | 14            | Before breakfast          |
| 414            | 314            | Cetirizine     | 10mg   | 7             | For allergy               |
| 415            | 315            | Amlodipine     | 5mg    | 30            | Blood pressure            |
| 416            | 316            | Azithromycin   | 500mg  | 3             | Take once daily           |
| 417            | 317            | Paracetamol    | 500mg  | 5             | Take after meals          |
| 418            | 318            | Ibuprofen      | 400mg  | 7             | Take with water           |
| 419            | 319            | Amoxicillin    | 250mg  | 10            | Morning and evening       |
| 420            | 320            | Metformin      | 500mg  | 30            | For diabetes              |
| 421            | 321            | Omeprazole     | 20mg   | 14            | Before breakfast          |
| 422            | 322            | Cetirizine     | 10mg   | 7             | For allergy               |
| 423            | 323            | Amlodipine     | 5mg    | 30            | Blood pressure            |
| 424            | 324            | Azithromycin   | 500mg  | 3             | Take once daily           |
| 425            | 325            | Paracetamol    | 500mg  | 5             | Take after meals          |
| 426            | 326            | Ibuprofen      | 400mg  | 7             | Take with water           |
| 427            | 327            | Amoxicillin    | 250mg  | 10            | Morning and evening       |
| 428            | 328            | Metformin      | 500mg  | 30            | For diabetes              |
| 429            | 329            | Omeprazole     | 20mg   | 14            | Before breakfast          |
| 430            | 330            | Cetirizine     | 10mg   | 7             | For allergy               |
| 431            | 331            | Amlodipine     | 5mg    | 30            | Blood pressure            |
| 432            | 332            | Azithromycin   | 500mg  | 3             | Take once daily           |
| 433            | 333            | Paracetamol    | 500mg  | 5             | Take after meals          |
| 434            | 334            | Ibuprofen      | 400mg  | 7             | Take with water           |
| 435            | 335            | Amoxicillin    | 250mg  | 10            | Morning and evening       |
| 436            | 336            | Metformin      | 500mg  | 30            | For diabetes              |
| 437            | 337            | Omeprazole     | 20mg   | 14            | Before breakfast          |
| 438            | 338            | Cetirizine     | 10mg   | 7             | For allergy               |
| 439            | 339            | Amlodipine     | 5mg    | 30            | Blood pressure            |
| 440            | 340            | Azithromycin   | 500mg  | 3             | Take once daily           |
| 441            | 341            | Paracetamol    | 500mg  | 5             | Take after meals          |
| 442            | 342            | Ibuprofen      | 400mg  | 7             | Take with water           |
| 443            | 343            | Amoxicillin    | 250mg  | 10            | Morning and evening       |
| 444            | 344            | Metformin      | 500mg  | 30            | For diabetes              |
| 445            | 345            | Omeprazole     | 20mg   | 14            | Before breakfast          |
| 446            | 346            | Cetirizine     | 10mg   | 7             | For allergy               |
| 447            | 347            | Amlodipine     | 5mg    | 30            | Blood pressure            |
| 448            | 348            | Azithromycin   | 500mg  | 3             | Take once daily           |
| 449            | 349            | Paracetamol    | 500mg  | 5             | Take after meals          |
| 450            | 350            | Ibuprofen      | 400mg  | 7             | Take with water           |
+----------------+----------------+----------------+--------+---------------+---------------------------+
```

```sql
CREATE TABLE prescriptions (
    prescription_id INT NOT NULL AUTO_INCREMENT,
    appointment_id INT NOT NULL,
    medicine_name VARCHAR(50) NOT NULL,
    dosage VARCHAR(50),
    duration_days INT,
    notes VARCHAR(200),
    PRIMARY KEY (prescription_id),
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id)
) ENGINE=InnoDB;

INSERT INTO prescriptions (prescription_id, appointment_id, medicine_name, dosage, duration_days, notes) VALUES
(401, 301, 'Paracetamol', '500mg', 5, 'Take after meals'),
(402, 302, 'Ibuprofen', '400mg', 7, 'Take with water'),
(403, 303, 'Amoxicillin', '250mg', 10, 'Morning and evening'),
(404, 304, 'Metformin', '500mg', 30, 'For diabetes'),
(405, 305, 'Omeprazole', '20mg', 14, 'Before breakfast'),
(406, 306, 'Cetirizine', '10mg', 7, 'For allergy'),
(407, 307, 'Amlodipine', '5mg', 30, 'Blood pressure'),
(408, 308, 'Azithromycin', '500mg', 3, 'Take once daily'),
(409, 309, 'Paracetamol', '500mg', 5, 'Take after meals'),
(410, 310, 'Ibuprofen', '400mg', 7, 'Take with water'),
(411, 311, 'Amoxicillin', '250mg', 10, 'Morning and evening'),
(412, 312, 'Metformin', '500mg', 30, 'For diabetes'),
(413, 313, 'Omeprazole', '20mg', 14, 'Before breakfast'),
(414, 314, 'Cetirizine', '10mg', 7, 'For allergy'),
(415, 315, 'Amlodipine', '5mg', 30, 'Blood pressure'),
(416, 316, 'Azithromycin', '500mg', 3, 'Take once daily'),
(417, 317, 'Paracetamol', '500mg', 5, 'Take after meals'),
(418, 318, 'Ibuprofen', '400mg', 7, 'Take with water'),
(419, 319, 'Amoxicillin', '250mg', 10, 'Morning and evening'),
(420, 320, 'Metformin', '500mg', 30, 'For diabetes'),
(421, 321, 'Omeprazole', '20mg', 14, 'Before breakfast'),
(422, 322, 'Cetirizine', '10mg', 7, 'For allergy'),
(423, 323, 'Amlodipine', '5mg', 30, 'Blood pressure'),
(424, 324, 'Azithromycin', '500mg', 3, 'Take once daily'),
(425, 325, 'Paracetamol', '500mg', 5, 'Take after meals'),
(426, 326, 'Ibuprofen', '400mg', 7, 'Take with water'),
(427, 327, 'Amoxicillin', '250mg', 10, 'Morning and evening'),
(428, 328, 'Metformin', '500mg', 30, 'For diabetes'),
(429, 329, 'Omeprazole', '20mg', 14, 'Before breakfast'),
(430, 330, 'Cetirizine', '10mg', 7, 'For allergy'),
(431, 331, 'Amlodipine', '5mg', 30, 'Blood pressure'),
(432, 332, 'Azithromycin', '500mg', 3, 'Take once daily'),
(433, 333, 'Paracetamol', '500mg', 5, 'Take after meals'),
(434, 334, 'Ibuprofen', '400mg', 7, 'Take with water'),
(435, 335, 'Amoxicillin', '250mg', 10, 'Morning and evening'),
(436, 336, 'Metformin', '500mg', 30, 'For diabetes'),
(437, 337, 'Omeprazole', '20mg', 14, 'Before breakfast'),
(438, 338, 'Cetirizine', '10mg', 7, 'For allergy'),
(439, 339, 'Amlodipine', '5mg', 30, 'Blood pressure'),
(440, 340, 'Azithromycin', '500mg', 3, 'Take once daily'),
(441, 341, 'Paracetamol', '500mg', 5, 'Take after meals'),
(442, 342, 'Ibuprofen', '400mg', 7, 'Take with water'),
(443, 343, 'Amoxicillin', '250mg', 10, 'Morning and evening'),
(444, 344, 'Metformin', '500mg', 30, 'For diabetes'),
(445, 345, 'Omeprazole', '20mg', 14, 'Before breakfast'),
(446, 346, 'Cetirizine', '10mg', 7, 'For allergy'),
(447, 347, 'Amlodipine', '5mg', 30, 'Blood pressure'),
(448, 348, 'Azithromycin', '500mg', 3, 'Take once daily'),
(449, 349, 'Paracetamol', '500mg', 5, 'Take after meals'),
(450, 350, 'Ibuprofen', '400mg', 7, 'Take with water');
```

### Table 5: medical_tests

```
+-----------------+---------------+------+-----+---------+----------------+
| Field           | Type          | Null | Key | Default | Extra          |
+-----------------+---------------+------+-----+---------+----------------+
| test_id         | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| appointment_id  | INT           | NO   | MUL | NULL    |                |
| test_name       | VARCHAR(50)   | NO   |     | NULL    |                |
| test_date       | DATE          | NO   |     | NULL    |                |
| result          | VARCHAR(100)  | YES  |     | NULL    |                |
+-----------------+---------------+------+-----+---------+----------------+

+---------+----------------+----------------+------------+----------------+
| test_id | appointment_id | test_name      | test_date  | result         |
+---------+----------------+----------------+------------+----------------+
| 501     | 301            | Blood Test     | 2025-12-01 | Normal         |
| 502     | 302            | X-Ray          | 2025-12-02 | Fracture       |
| 503     | 303            | MRI Scan       | 2025-12-03 | Clear          |
| 504     | 304            | ECG            | 2025-12-04 | Abnormal       |
| 505     | 305            | Ultrasound     | 2025-12-05 | Normal         |
| 506     | 306            | Blood Test     | 2025-12-06 | High WBC       |
| 507     | 307            | X-Ray          | 2025-12-07 | Normal         |
| 508     | 308            | MRI Scan       | 2025-12-08 | Minor Issue    |
| 509     | 309            | ECG            | 2025-12-09 | Normal         |
| 510     | 310            | Ultrasound     | 2025-12-10 | Cyst Detected  |
| 511     | 311            | Blood Test     | 2025-12-11 | Normal         |
| 512     | 312            | X-Ray          | 2025-12-12 | Fracture       |
| 513     | 313            | MRI Scan       | 2025-12-13 | Clear          |
| 514     | 314            | ECG            | 2025-12-14 | Abnormal       |
| 515     | 315            | Ultrasound     | 2025-12-15 | Normal         |
| 516     | 316            | Blood Test     | 2025-12-16 | Low Hemoglobin |
| 517     | 317            | X-Ray          | 2025-12-17 | Normal         |
| 518     | 318            | MRI Scan       | 2025-12-18 | Minor Issue    |
| 519     | 319            | ECG            | 2025-12-19 | Normal         |
| 520     | 320            | Ultrasound     | 2025-12-20 | Normal         |
| 521     | 321            | Blood Test     | 2025-12-21 | High Sugar     |
| 522     | 322            | X-Ray          | 2025-12-22 | Normal         |
| 523     | 323            | MRI Scan       | 2025-12-23 | Clear          |
| 524     | 324            | ECG            | 2025-12-24 | Abnormal       |
| 525     | 325            | Ultrasound     | 2025-12-25 | Normal         |
| 526     | 326            | Blood Test     | 2025-12-26 | Low Iron       |
| 527     | 327            | X-Ray          | 2025-12-27 | Normal         |
| 528     | 328            | MRI Scan       | 2025-12-28 | Clear          |
| 529     | 329            | ECG            | 2025-12-29 | Abnormal       |
| 530     | 330            | Ultrasound     | 2025-12-30 | Cyst Detected  |
| 531     | 331            | Blood Test     | 2025-12-31 | Normal         |
| 532     | 332            | X-Ray          | 2026-01-01 | Fracture       |
| 533     | 333            | MRI Scan       | 2026-01-02 | Clear          |
| 534     | 334            | ECG            | 2026-01-03 | Normal         |
| 535     | 335            | Ultrasound     | 2026-01-04 | Normal         |
| 536     | 336            | Blood Test     | 2026-01-05 | High WBC       |
| 537     | 337            | X-Ray          | 2026-01-06 | Normal         |
| 538     | 338            | MRI Scan       | 2026-01-07 | Minor Issue    |
| 539     | 339            | ECG            | 2026-01-08 | Normal         |
| 540     | 340            | Ultrasound     | 2026-01-09 | Normal         |
| 541     | 341            | Blood Test     | 2026-01-10 | Low Hemoglobin |
| 542     | 342            | X-Ray          | 2026-01-11 | Normal         |
| 543     | 343            | MRI Scan       | 2026-01-12 | Clear          |
| 544     | 344            | ECG            | 2026-01-13 | Abnormal       |
| 545     | 345            | Ultrasound     | 2026-01-14 | Normal         |
| 546     | 346            | Blood Test     | 2026-01-15 | High Sugar     |
| 547     | 347            | X-Ray          | 2026-01-16 | Normal         |
| 548     | 348            | MRI Scan       | 2026-01-17 | Clear          |
| 549     | 349            | ECG            | 2026-01-18 | Abnormal       |
| 550     | 350            | Ultrasound     | 2026-01-19 | Normal         |
+---------+----------------+----------------+------------+----------------+
```

```sql
CREATE TABLE medical_tests (
    test_id INT NOT NULL AUTO_INCREMENT,
    appointment_id INT NOT NULL,
    test_name VARCHAR(50) NOT NULL,
    test_date DATE NOT NULL,
    result VARCHAR(100),
    PRIMARY KEY (test_id),
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id)
) ENGINE=InnoDB;


INSERT INTO medical_tests (test_id, appointment_id, test_name, test_date, result)VALUES
(501, 301, 'Blood Test', '2025-12-01', 'Normal'),
(502, 302, 'X-Ray', '2025-12-02', 'Fracture'),
(503, 303, 'MRI Scan', '2025-12-03', 'Clear'),
(504, 304, 'ECG', '2025-12-04', 'Abnormal'),
(505, 305, 'Ultrasound', '2025-12-05', 'Normal'),
(506, 306, 'Blood Test', '2025-12-06', 'High WBC'),
(507, 307, 'X-Ray', '2025-12-07', 'Normal'),
(508, 308, 'MRI Scan', '2025-12-08', 'Minor Issue'),
(509, 309, 'ECG', '2025-12-09', 'Normal'),
(510, 310, 'Ultrasound', '2025-12-10', 'Cyst Detected'),
(511, 311, 'Blood Test', '2025-12-11', 'Normal'),
(512, 312, 'X-Ray', '2025-12-12', 'Fracture'),
(513, 313, 'MRI Scan', '2025-12-13', 'Clear'),
(514, 314, 'ECG', '2025-12-14', 'Abnormal'),
(515, 315, 'Ultrasound', '2025-12-15', 'Normal'),
(516, 316, 'Blood Test', '2025-12-16', 'Low Hemoglobin'),
(517, 317, 'X-Ray', '2025-12-17', 'Normal'),
(518, 318, 'MRI Scan', '2025-12-18', 'Minor Issue'),
(519, 319, 'ECG', '2025-12-19', 'Normal'),
(520, 320, 'Ultrasound', '2025-12-20', 'Normal'),
(521, 321, 'Blood Test', '2025-12-21', 'High Sugar'),
(522, 322, 'X-Ray', '2025-12-22', 'Normal'),
(523, 323, 'MRI Scan', '2025-12-23', 'Clear'),
(524, 324, 'ECG', '2025-12-24', 'Abnormal'),
(525, 325, 'Ultrasound', '2025-12-25', 'Normal'),
(526, 326, 'Blood Test', '2025-12-26', 'Low Iron'),
(527, 327, 'X-Ray', '2025-12-27', 'Normal'),
(528, 328, 'MRI Scan', '2025-12-28', 'Clear'),
(529, 329, 'ECG', '2025-12-29', 'Abnormal'),
(530, 330, 'Ultrasound', '2025-12-30', 'Cyst Detected'),
(531, 331, 'Blood Test', '2025-12-31', 'Normal'),
(532, 332, 'X-Ray', '2026-01-01', 'Fracture'),
(533, 333, 'MRI Scan', '2026-01-02', 'Clear'),
(534, 334, 'ECG', '2026-01-03', 'Normal'),
(535, 335, 'Ultrasound', '2026-01-04', 'Normal'),
(536, 336, 'Blood Test', '2026-01-05', 'High WBC'),
(537, 337, 'X-Ray', '2026-01-06', 'Normal'),
(538, 338, 'MRI Scan', '2026-01-07', 'Minor Issue'),
(539, 339, 'ECG', '2026-01-08', 'Normal'),
(540, 340, 'Ultrasound', '2026-01-09', 'Normal'),
(541, 341, 'Blood Test', '2026-01-10', 'Low Hemoglobin'),
(542, 342, 'X-Ray', '2026-01-11', 'Normal'),
(543, 343, 'MRI Scan', '2026-01-12', 'Clear'),
(544, 344, 'ECG', '2026-01-13', 'Abnormal'),
(545, 345, 'Ultrasound', '2026-01-14', 'Normal'),
(546, 346, 'Blood Test', '2026-01-15', 'High Sugar'),
(547, 347, 'X-Ray', '2026-01-16', 'Normal'),
(548, 348, 'MRI Scan', '2026-01-17', 'Clear'),
(549, 349, 'ECG', '2026-01-18', 'Abnormal'),
(550, 350, 'Ultrasound', '2026-01-19', 'Normal');
```