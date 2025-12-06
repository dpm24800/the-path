# Sector 6: Hotel

### Table 1: guests
```
+------------+---------------+------+-----+---------+----------------+
| Field      | Type          | Null | Key | Default | Extra          |
+------------+---------------+------+-----+---------+----------------+
| guest_id   | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| first_name | VARCHAR(50)   | NO   |     | NULL    |                |
| last_name  | VARCHAR(50)   | NO   |     | NULL    |                |
| email      | VARCHAR(100)  | YES  | UNI | NULL    |                |
| phone      | VARCHAR(20)   | YES  |     | NULL    |                |
| nationality| VARCHAR(50)   | NO   |     | NULL    |                |
+------------+---------------+------+-----+---------+----------------+

+----------+------------+-----------+-------------------------+----------------+----------------+
| guest_id | first_name | last_name | email                   | phone          | nationality    |
+----------+------------+-----------+-------------------------+----------------+----------------+
| 1        | John       | Smith     | john.smith@example.com  | +1-202-555-0101| USA            |
| 2        | Maria      | Garcia    | maria.garcia@example.com| +34-912-555-010| Spain          |
| 3        | Chen       | Li        | chen.li@example.com     | +86-10-5555-01 | China          |
| 4        | Hiroshi    | Tanaka    | hiro.tanaka@example.jp  | +81-3-5555-01  | Japan          |
| 5        | Emma       | Brown     | emma.brown@example.com  | +44-20-5555-01 | UK             |
| 6        | Ahmed      | Khan      | ahmed.khan@example.ae   | +971-4-555-0101| UAE            |
| 7        | Sarah      | Johnson   | sarah.johnson@example.com| +1-202-555-0202| USA           |
| 8        | Pedro      | Alvarez   | pedro.alvarez@example.com| +34-912-555-020| Spain         |
| 9        | Li         | Wei       | li.wei@example.com      | +86-21-5555-02 | China          |
| 10       | Yuki       | Sato      | yuki.sato@example.jp    | +81-3-5555-02  | Japan          |
| 11       | Olivia     | Williams  | olivia.williams@example.com| +44-20-5555-02 | UK           |
| 12       | Khalid     | Al-Mansoor| khalid.mansoor@example.ae| +971-4-555-0202| UAE           |
| 13       | David      | Miller    | david.miller@example.com| +1-202-555-0303| USA            |
| 14       | Sofia      | Fernandez | sofia.fernandez@example.com| +34-912-555-030| Spain         |
| 15       | Wang       | Mei       | wang.mei@example.com    | +86-10-5555-03 | China          |
| 16       | Takashi    | Yamamoto  | takashi.yamamoto@example.jp| +81-3-5555-03| Japan         |
| 17       | Isabella   | Taylor    | isabella.taylor@example.com| +44-20-5555-03| UK            |
| 18       | Fatima     | Al-Hadid  | fatima.alhadid@example.ae| +971-4-555-0303| UAE          |
| 19       | Michael    | Davis     | michael.davis@example.com| +1-202-555-0404| USA           |
| 20       | Lucia      | Martinez  | lucia.martinez@example.com| +34-912-555-040| Spain        |
| 21       | Zhou       | Fang      | zhou.fang@example.com   | +86-21-5555-04 | China          |
| 22       | Kenji      | Kobayashi | kenji.kobayashi@example.jp| +81-3-5555-04| Japan         |
| 23       | Emily      | Wilson    | emily.wilson@example.com| +44-20-5555-04 | UK             |
| 24       | Omar       | Al-Farsi  | omar.alfarsi@example.ae | +971-4-555-0404| UAE           |
| 25       | Daniel     | Anderson  | daniel.anderson@example.com| +1-202-555-0505| USA          |
| 26       | Carmen     | Lopez     | carmen.lopez@example.com| +34-912-555-050| Spain         |
| 27       | Li         | Jie       | li.jie@example.com      | +86-10-5555-05 | China          |
| 28       | Haruto     | Nakamura  | haruto.nakamura@example.jp| +81-3-5555-05| Japan         |
| 29       | Grace      | Hall      | grace.hall@example.com  | +44-20-5555-05 | UK             |
| 30       | Aisha      | Al-Khalid | aisha.alkhalid@example.ae| +971-4-555-0505| UAE          |
| 31       | James      | Scott     | james.scott@example.com | +1-202-555-0606 | USA           |
| 32       | Elena      | Sanchez   | elena.sanchez@example.com| +34-912-555-060| Spain        |
| 33       | Zhang      | Lei       | zhang.lei@example.com   | +86-21-5555-06 | China          |
| 34       | Yui        | Nakamoto  | yui.nakamoto@example.jp | +81-3-5555-06 | Japan          |
| 35       | Chloe      | Moore     | chloe.moore@example.com | +44-20-5555-06 | UK             |
| 36       | Hamad      | Al-Saidi  | hamad.alsaidi@example.ae| +971-4-555-0606| UAE          |
| 37       | Matthew    | Thompson  | matthew.thompson@example.com| +1-202-555-0707| USA       |
| 38       | Ana        | Ruiz      | ana.ruiz@example.com    | +34-912-555-070| Spain         |
| 39       | Liu        | Xin       | liu.xin@example.com     | +86-10-5555-07 | China          |
| 40       | Riku       | Matsumoto | riku.matsumoto@example.jp| +81-3-5555-07| Japan         |
| 41       | Sophie     | Clark     | sophie.clark@example.com| +44-20-5555-07 | UK            |
| 42       | Zayed      | Al-Mansouri| zayed.almansouri@example.ae| +971-4-555-0707| UAE         |
| 43       | Ryan       | Lewis     | ryan.lewis@example.com  | +1-202-555-0808 | USA           |
| 44       | Marta      | Gonzalez  | marta.gonzalez@example.com| +34-912-555-080| Spain        |
| 45       | Wu         | Hao       | wu.hao@example.com      | +86-21-5555-08 | China          |
| 46       | Sora       | Fujimoto  | sora.fujimoto@example.jp| +81-3-5555-08 | Japan          |
| 47       | Lily       | Adams     | lily.adams@example.com  | +44-20-5555-08 | UK             |
| 48       | Noura      | Al-Zahra  | noura.alzahra@example.ae| +971-4-555-0808| UAE          |
| 49       | Ethan      | Baker     | ethan.baker@example.com | +1-202-555-0909 | USA           |
| 50       | Sofia      | Romero    | sofia.romero@example.com| +34-912-555-090| Spain        |
+----------+------------+-----------+-------------------------+----------------+----------------+

```

```sql
CREATE TABLE guests (
    guest_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    nationality VARCHAR(50) NOT NULL,
    PRIMARY KEY (guest_id)
) ENGINE=InnoDB;

INSERT INTO guests (guest_id, first_name, last_name, email, phone, nationality) VALUES
(1, 'John', 'Smith', 'john.smith@example.com', '+1-202-555-0101', 'USA'),
(2, 'Maria', 'Garcia', 'maria.garcia@example.com', '+34-912-555-010', 'Spain'),
(3, 'Chen', 'Li', 'chen.li@example.com', '+86-10-5555-01', 'China'),
(4, 'Hiroshi', 'Tanaka', 'hiro.tanaka@example.jp', '+81-3-5555-01', 'Japan'),
(5, 'Emma', 'Brown', 'emma.brown@example.com', '+44-20-5555-01', 'UK'),
(6, 'Ahmed', 'Khan', 'ahmed.khan@example.ae', '+971-4-555-0101', 'UAE'),
(7, 'Sarah', 'Johnson', 'sarah.johnson@example.com', '+1-202-555-0202', 'USA'),
(8, 'Pedro', 'Alvarez', 'pedro.alvarez@example.com', '+34-912-555-020', 'Spain'),
(9, 'Li', 'Wei', 'li.wei@example.com', '+86-21-5555-02', 'China'),
(10, 'Yuki', 'Sato', 'yuki.sato@example.jp', '+81-3-5555-02', 'Japan'),
(11, 'Olivia', 'Williams', 'olivia.williams@example.com', '+44-20-5555-02', 'UK'),
(12, 'Khalid', 'Al-Mansoor', 'khalid.mansoor@example.ae', '+971-4-555-0202', 'UAE'),
(13, 'David', 'Miller', 'david.miller@example.com', '+1-202-555-0303', 'USA'),
(14, 'Sofia', 'Fernandez', 'sofia.fernandez@example.com', '+34-912-555-030', 'Spain'),
(15, 'Wang', 'Mei', 'wang.mei@example.com', '+86-10-5555-03', 'China'),
(16, 'Takashi', 'Yamamoto', 'takashi.yamamoto@example.jp', '+81-3-5555-03', 'Japan'),
(17, 'Isabella', 'Taylor', 'isabella.taylor@example.com', '+44-20-5555-03', 'UK'),
(18, 'Fatima', 'Al-Hadid', 'fatima.alhadid@example.ae', '+971-4-555-0303', 'UAE'),
(19, 'Michael', 'Davis', 'michael.davis@example.com', '+1-202-555-0404', 'USA'),
(20, 'Lucia', 'Martinez', 'lucia.martinez@example.com', '+34-912-555-040', 'Spain'),
(21, 'Zhou', 'Fang', 'zhou.fang@example.com', '+86-21-5555-04', 'China'),
(22, 'Kenji', 'Kobayashi', 'kenji.kobayashi@example.jp', '+81-3-5555-04', 'Japan'),
(23, 'Emily', 'Wilson', 'emily.wilson@example.com', '+44-20-5555-04', 'UK'),
(24, 'Omar', 'Al-Farsi', 'omar.alfarsi@example.ae', '+971-4-555-0404', 'UAE'),
(25, 'Daniel', 'Anderson', 'daniel.anderson@example.com', '+1-202-555-0505', 'USA'),
(26, 'Carmen', 'Lopez', 'carmen.lopez@example.com', '+34-912-555-050', 'Spain'),
(27, 'Li', 'Jie', 'li.jie@example.com', '+86-10-5555-05', 'China'),
(28, 'Haruto', 'Nakamura', 'haruto.nakamura@example.jp', '+81-3-5555-05', 'Japan'),
(29, 'Grace', 'Hall', 'grace.hall@example.com', '+44-20-5555-05', 'UK'),
(30, 'Aisha', 'Al-Khalid', 'aisha.alkhalid@example.ae', '+971-4-555-0505', 'UAE'),
(31, 'James', 'Scott', 'james.scott@example.com', '+1-202-555-0606', 'USA'),
(32, 'Elena', 'Sanchez', 'elena.sanchez@example.com', '+34-912-555-060', 'Spain'),
(33, 'Zhang', 'Lei', 'zhang.lei@example.com', '+86-21-5555-06', 'China'),
(34, 'Yui', 'Nakamoto', 'yui.nakamoto@example.jp', '+81-3-5555-06', 'Japan'),
(35, 'Chloe', 'Moore', 'chloe.moore@example.com', '+44-20-5555-06', 'UK'),
(36, 'Hamad', 'Al-Saidi', 'hamad.alsaidi@example.ae', '+971-4-555-0606', 'UAE'),
(37, 'Matthew', 'Thompson', 'matthew.thompson@example.com', '+1-202-555-0707', 'USA'),
(38, 'Ana', 'Ruiz', 'ana.ruiz@example.com', '+34-912-555-070', 'Spain'),
(39, 'Liu', 'Xin', 'liu.xin@example.com', '+86-10-5555-07', 'China'),
(40, 'Riku', 'Matsumoto', 'riku.matsumoto@example.jp', '+81-3-5555-07', 'Japan'),
(41, 'Sophie', 'Clark', 'sophie.clark@example.com', '+44-20-5555-07', 'UK'),
(42, 'Zayed', 'Al-Mansouri', 'zayed.almansouri@example.ae', '+971-4-555-0707', 'UAE'),
(43, 'Ryan', 'Lewis', 'ryan.lewis@example.com', '+1-202-555-0808', 'USA'),
(44, 'Marta', 'Gonzalez', 'marta.gonzalez@example.com', '+34-912-555-080', 'Spain'),
(45, 'Wu', 'Hao', 'wu.hao@example.com', '+86-21-5555-08', 'China'),
(46, 'Sora', 'Fujimoto', 'sora.fujimoto@example.jp', '+81-3-5555-08', 'Japan'),
(47, 'Lily', 'Adams', 'lily.adams@example.com', '+44-20-5555-08', 'UK'),
(48, 'Noura', 'Al-Zahra', 'noura.alzahra@example.ae', '+971-4-555-0808', 'UAE'),
(49, 'Ethan', 'Baker', 'ethan.baker@example.com', '+1-202-555-0909', 'USA'),
(50, 'Sofia', 'Romero', 'sofia.romero@example.com', '+34-912-555-090', 'Spain');
```

### Table 2: rooms
```
+---------------+---------------+------+-----+---------+----------------+
| Field         | Type          | Null | Key | Default | Extra          |
+---------------+---------------+------+-----+---------+----------------+
| room_id       | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| room_number   | VARCHAR(10)   | NO   | UNI | NULL    |                |
| room_type     | VARCHAR(20)   | NO   |     | NULL    |                |
| price_per_night| DECIMAL(8,2) | NO   |     | 0.00    |                |
| status        | VARCHAR(20)   | NO   |     | 'Available' |             |
+---------------+---------------+------+-----+---------+----------------+

+---------+-------------+-----------+----------------+------------+
| room_id | room_number | room_type | price_per_night| status     |
+---------+-------------+-----------+----------------+------------+
| 1       | 101         | Single    | 100.00         | Available  |
| 2       | 102         | Single    | 100.00         | Booked     |
| 3       | 103         | Single    | 100.00         | Available  |
| 4       | 104         | Single    | 100.00         | Maintenance|
| 5       | 105         | Single    | 100.00         | Booked     |
| 6       | 201         | Double    | 150.00         | Available  |
| 7       | 202         | Double    | 150.00         | Booked     |
| 8       | 203         | Double    | 150.00         | Available  |
| 9       | 204         | Double    | 150.00         | Available  |
| 10      | 205         | Double    | 150.00         | Booked     |
| 11      | 301         | Suite     | 250.00         | Available  |
| 12      | 302         | Suite     | 250.00         | Booked     |
| 13      | 303         | Suite     | 250.00         | Maintenance|
| 14      | 304         | Suite     | 250.00         | Available  |
| 15      | 305         | Suite     | 250.00         | Booked     |
| 16      | 401         | Deluxe    | 300.00         | Available  |
| 17      | 402         | Deluxe    | 300.00         | Booked     |
| 18      | 403         | Deluxe    | 300.00         | Available  |
| 19      | 404         | Deluxe    | 300.00         | Booked     |
| 20      | 405         | Deluxe    | 300.00         | Available  |
| 21      | 501         | Single    | 100.00         | Booked     |
| 22      | 502         | Single    | 100.00         | Available  |
| 23      | 503         | Single    | 100.00         | Available  |
| 24      | 504         | Single    | 100.00         | Booked     |
| 25      | 505         | Single    | 100.00         | Available  |
| 26      | 601         | Double    | 150.00         | Available  |
| 27      | 602         | Double    | 150.00         | Booked     |
| 28      | 603         | Double    | 150.00         | Available  |
| 29      | 604         | Double    | 150.00         | Booked     |
| 30      | 605         | Double    | 150.00         | Available  |
| 31      | 701         | Suite     | 250.00         | Booked     |
| 32      | 702         | Suite     | 250.00         | Available  |
| 33      | 703         | Suite     | 250.00         | Booked     |
| 34      | 704         | Suite     | 250.00         | Available  |
| 35      | 705         | Suite     | 250.00         | Booked     |
| 36      | 801         | Deluxe    | 300.00         | Available  |
| 37      | 802         | Deluxe    | 300.00         | Booked     |
| 38      | 803         | Deluxe    | 300.00         | Available  |
| 39      | 804         | Deluxe    | 300.00         | Available  |
| 40      | 805         | Deluxe    | 300.00         | Booked     |
| 41      | 901         | Single    | 100.00         | Available  |
| 42      | 902         | Single    | 100.00         | Booked     |
| 43      | 903         | Single    | 100.00         | Available  |
| 44      | 904         | Single    | 100.00         | Booked     |
| 45      | 905         | Single    | 100.00         | Available  |
| 46      | 1001        | Double    | 150.00         | Available  |
| 47      | 1002        | Double    | 150.00         | Booked     |
| 48      | 1003        | Double    | 150.00         | Available  |
| 49      | 1004        | Double    | 150.00         | Booked     |
| 50      | 1005        | Double    | 150.00         | Available  |
+---------+-------------+-----------+----------------+------------+

```

```sql
CREATE TABLE rooms (
    room_id INT NOT NULL AUTO_INCREMENT,
    room_number VARCHAR(10) NOT NULL UNIQUE,
    room_type VARCHAR(20) NOT NULL,
    price_per_night DECIMAL(8,2) NOT NULL DEFAULT 0.00,
    status VARCHAR(20) NOT NULL DEFAULT 'Available',
    PRIMARY KEY (room_id)
) ENGINE=InnoDB;

INSERT INTO rooms (room_id, room_number, room_type, price_per_night, status) VALUES
(1, '101', 'Single', 100.00, 'Available'),
(2, '102', 'Single', 100.00, 'Booked'),
(3, '103', 'Single', 100.00, 'Available'),
(4, '104', 'Single', 100.00, 'Maintenance'),
(5, '105', 'Single', 100.00, 'Booked'),
(6, '201', 'Double', 150.00, 'Available'),
(7, '202', 'Double', 150.00, 'Booked'),
(8, '203', 'Double', 150.00, 'Available'),
(9, '204', 'Double', 150.00, 'Available'),
(10, '205', 'Double', 150.00, 'Booked'),
(11, '301', 'Suite', 250.00, 'Available'),
(12, '302', 'Suite', 250.00, 'Booked'),
(13, '303', 'Suite', 250.00, 'Maintenance'),
(14, '304', 'Suite', 250.00, 'Available'),
(15, '305', 'Suite', 250.00, 'Booked'),
(16, '401', 'Deluxe', 300.00, 'Available'),
(17, '402', 'Deluxe', 300.00, 'Booked'),
(18, '403', 'Deluxe', 300.00, 'Available'),
(19, '404', 'Deluxe', 300.00, 'Booked'),
(20, '405', 'Deluxe', 300.00, 'Available'),
(21, '501', 'Single', 100.00, 'Booked'),
(22, '502', 'Single', 100.00, 'Available'),
(23, '503', 'Single', 100.00, 'Available'),
(24, '504', 'Single', 100.00, 'Booked'),
(25, '505', 'Single', 100.00, 'Available'),
(26, '601', 'Double', 150.00, 'Available'),
(27, '602', 'Double', 150.00, 'Booked'),
(28, '603', 'Double', 150.00, 'Available'),
(29, '604', 'Double', 150.00, 'Booked'),
(30, '605', 'Double', 150.00, 'Available'),
(31, '701', 'Suite', 250.00, 'Booked'),
(32, '702', 'Suite', 250.00, 'Available'),
(33, '703', 'Suite', 250.00, 'Booked'),
(34, '704', 'Suite', 250.00, 'Available'),
(35, '705', 'Suite', 250.00, 'Booked'),
(36, '801', 'Deluxe', 300.00, 'Available'),
(37, '802', 'Deluxe', 300.00, 'Booked'),
(38, '803', 'Deluxe', 300.00, 'Available'),
(39, '804', 'Deluxe', 300.00, 'Available'),
(40, '805', 'Deluxe', 300.00, 'Booked'),
(41, '901', 'Single', 100.00, 'Available'),
(42, '902', 'Single', 100.00, 'Booked'),
(43, '903', 'Single', 100.00, 'Available'),
(44, '904', 'Single', 100.00, 'Booked'),
(45, '905', 'Single', 100.00, 'Available'),
(46, '1001', 'Double', 150.00, 'Available'),
(47, '1002', 'Double', 150.00, 'Booked'),
(48, '1003', 'Double', 150.00, 'Available'),
(49, '1004', 'Double', 150.00, 'Booked'),
(50, '1005', 'Double', 150.00, 'Available');
```

### Table 3: bookings
```
+---------------+---------------+------+-----+---------+----------------+
| Field         | Type          | Null | Key | Default | Extra          |
+---------------+---------------+------+-----+---------+----------------+
| booking_id    | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| guest_id      | INT           | NO   | MUL | NULL    |                |
| room_id       | INT           | NO   | MUL | NULL    |                |
| check_in      | DATE          | NO   |     | NULL    |                |
| check_out     | DATE          | NO   |     | NULL    |                |
| booking_date  | DATE          | NO   |     | NULL    |                |
| status        | VARCHAR(20)   | NO   |     | 'Booked'|                |
+---------------+---------------+------+-----+---------+----------------+

+------------+---------+---------+------------+------------+--------------+--------+
| booking_id | guest_id| room_id | check_in   | check_out  | booking_date | status |
+------------+---------+---------+------------+------------+--------------+--------+
| 1          | 1       | 101     | 2025-12-01 | 2025-12-05 | 2025-11-20   | Booked |
| 2          | 2       | 102     | 2025-12-02 | 2025-12-06 | 2025-11-21   | Checked-in |
| 3          | 3       | 103     | 2025-12-03 | 2025-12-04 | 2025-11-22   | Cancelled |
| 4          | 4       | 104     | 2025-12-05 | 2025-12-10 | 2025-11-23   | Booked |
| 5          | 5       | 105     | 2025-12-06 | 2025-12-08 | 2025-11-24   | Checked-out |
| 6          | 6       | 201     | 2025-12-01 | 2025-12-03 | 2025-11-25   | Booked |
| 7          | 7       | 202     | 2025-12-02 | 2025-12-06 | 2025-11-26   | Booked |
| 8          | 8       | 203     | 2025-12-04 | 2025-12-07 | 2025-11-27   | Cancelled |
| 9          | 9       | 204     | 2025-12-05 | 2025-12-09 | 2025-11-28   | Booked |
| 10         | 10      | 205     | 2025-12-06 | 2025-12-10 | 2025-11-29   | Checked-in |
| 11         | 11      | 301     | 2025-12-01 | 2025-12-04 | 2025-11-30   | Booked |
| 12         | 12      | 302     | 2025-12-03 | 2025-12-06 | 2025-12-01   | Booked |
| 13         | 13      | 303     | 2025-12-02 | 2025-12-05 | 2025-12-01   | Cancelled |
| 14         | 14      | 304     | 2025-12-05 | 2025-12-08 | 2025-12-02   | Checked-in |
| 15         | 15      | 305     | 2025-12-06 | 2025-12-09 | 2025-12-03   | Booked |
| 16         | 16      | 401     | 2025-12-01 | 2025-12-03 | 2025-12-04   | Checked-out |
| 17         | 17      | 402     | 2025-12-02 | 2025-12-05 | 2025-12-05   | Booked |
| 18         | 18      | 403     | 2025-12-03 | 2025-12-07 | 2025-12-05   | Booked |
| 19         | 19      | 404     | 2025-12-04 | 2025-12-08 | 2025-12-06   | Cancelled |
| 20         | 20      | 405     | 2025-12-05 | 2025-12-09 | 2025-12-06   | Booked |
| 21         | 21      | 501     | 2025-12-01 | 2025-12-03 | 2025-12-06   | Booked |
| 22         | 22      | 502     | 2025-12-02 | 2025-12-05 | 2025-12-07   | Checked-in |
| 23         | 23      | 503     | 2025-12-03 | 2025-12-07 | 2025-12-07   | Booked |
| 24         | 24      | 504     | 2025-12-04 | 2025-12-08 | 2025-12-07   | Booked |
| 25         | 25      | 505     | 2025-12-05 | 2025-12-09 | 2025-12-07   | Checked-out |
| 26         | 26      | 601     | 2025-12-01 | 2025-12-03 | 2025-12-07   | Booked |
| 27         | 27      | 602     | 2025-12-02 | 2025-12-06 | 2025-12-07   | Booked |
| 28         | 28      | 603     | 2025-12-03 | 2025-12-07 | 2025-12-07   | Cancelled |
| 29         | 29      | 604     | 2025-12-04 | 2025-12-08 | 2025-12-07   | Booked |
| 30         | 30      | 605     | 2025-12-05 | 2025-12-09 | 2025-12-07   | Booked |
| 31         | 31      | 701     | 2025-12-01 | 2025-12-04 | 2025-12-07   | Booked |
| 32         | 32      | 702     | 2025-12-03 | 2025-12-06 | 2025-12-07   | Checked-in |
| 33         | 33      | 703     | 2025-12-02 | 2025-12-05 | 2025-12-07   | Booked |
| 34         | 34      | 704     | 2025-12-05 | 2025-12-08 | 2025-12-07   | Booked |
| 35         | 35      | 705     | 2025-12-06 | 2025-12-09 | 2025-12-07   | Checked-out |
| 36         | 36      | 801     | 2025-12-01 | 2025-12-03 | 2025-12-07   | Booked |
| 37         | 37      | 802     | 2025-12-02 | 2025-12-05 | 2025-12-07   | Booked |
| 38         | 38      | 803     | 2025-12-03 | 2025-12-07 | 2025-12-07   | Cancelled |
| 39         | 39      | 804     | 2025-12-04 | 2025-12-08 | 2025-12-07   | Booked |
| 40         | 40      | 805     | 2025-12-05 | 2025-12-09 | 2025-12-07   | Booked |
| 41         | 41      | 901     | 2025-12-01 | 2025-12-03 | 2025-12-07   | Checked-in |
| 42         | 42      | 902     | 2025-12-02 | 2025-12-05 | 2025-12-07   | Booked |
| 43         | 43      | 903     | 2025-12-03 | 2025-12-07 | 2025-12-07   | Booked |
| 44         | 44      | 904     | 2025-12-04 | 2025-12-08 | 2025-12-07   | Cancelled |
| 45         | 45      | 905     | 2025-12-05 | 2025-12-09 | 2025-12-07   | Booked |
| 46         | 46      | 1001    | 2025-12-01 | 2025-12-03 | 2025-12-07   | Booked |
| 47         | 47      | 1002    | 2025-12-02 | 2025-12-05 | 2025-12-07   | Booked |
| 48         | 48      | 1003    | 2025-12-03 | 2025-12-07 | 2025-12-07   | Cancelled |
| 49         | 49      | 1004    | 2025-12-04 | 2025-12-08 | 2025-12-07   | Booked |
| 50         | 50      | 1005    | 2025-12-05 | 2025-12-09 | 2025-12-07   | Booked |
+------------+---------+---------+------------+------------+--------------+--------+
```

```sql
CREATE TABLE bookings (
    booking_id INT NOT NULL AUTO_INCREMENT,
    guest_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL,
    booking_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Booked',
    PRIMARY KEY (booking_id),
    FOREIGN KEY (guest_id) REFERENCES guests(guest_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
) ENGINE=InnoDB;

INSERT INTO bookings (booking_id, guest_id, room_id, check_in, check_out, booking_date, status) VALUES
(1, 1, '101', '2025-12-01', '2025-12-05', '2025-11-20', 'Booked'),
(2, 2, '102', '2025-12-02', '2025-12-06', '2025-11-21', 'Checked-in'),
(3, 3, '103', '2025-12-03', '2025-12-04', '2025-11-22', 'Cancelled'),
(4, 4, '104', '2025-12-05', '2025-12-10', '2025-11-23', 'Booked'),
(5, 5, '105', '2025-12-06', '2025-12-08', '2025-11-24', 'Checked-out'),
(6, 6, '201', '2025-12-01', '2025-12-03', '2025-11-25', 'Booked'),
(7, 7, '202', '2025-12-02', '2025-12-06', '2025-11-26', 'Booked'),
(8, 8, '203', '2025-12-04', '2025-12-07', '2025-11-27', 'Cancelled'),
(9, 9, '204', '2025-12-05', '2025-12-09', '2025-11-28', 'Booked'),
(10, 10, '205', '2025-12-06', '2025-12-10', '2025-11-29', 'Checked-in'),
(11, 11, '301', '2025-12-01', '2025-12-04', '2025-11-30', 'Booked'),
(12, 12, '302', '2025-12-03', '2025-12-06', '2025-12-01', 'Booked'),
(13, 13, '303', '2025-12-02', '2025-12-05', '2025-12-01', 'Cancelled'),
(14, 14, '304', '2025-12-05', '2025-12-08', '2025-12-02', 'Checked-in'),
(15, 15, '305', '2025-12-06', '2025-12-09', '2025-12-03', 'Booked'),
(16, 16, '401', '2025-12-01', '2025-12-03', '2025-12-04', 'Checked-out'),
(17, 17, '402', '2025-12-02', '2025-12-05', '2025-12-05', 'Booked'),
(18, 18, '403', '2025-12-03', '2025-12-07', '2025-12-05', 'Booked'),
(19, 19, '404', '2025-12-04', '2025-12-08', '2025-12-06', 'Cancelled'),
(20, 20, '405', '2025-12-05', '2025-12-09', '2025-12-06', 'Booked'),
(21, 21, '501', '2025-12-01', '2025-12-03', '2025-12-06', 'Booked'),
(22, 22, '502', '2025-12-02', '2025-12-05', '2025-12-07', 'Checked-in'),
(23, 23, '503', '2025-12-03', '2025-12-07', '2025-12-07', 'Booked'),
(24, 24, '504', '2025-12-04', '2025-12-08', '2025-12-07', 'Booked'),
(25, 25, '505', '2025-12-05', '2025-12-09', '2025-12-07', 'Checked-out'),
(26, 26, '601', '2025-12-01', '2025-12-03', '2025-12-07', 'Booked'),
(27, 27, '602', '2025-12-02', '2025-12-06', '2025-12-07', 'Booked'),
(28, 28, '603', '2025-12-03', '2025-12-07', '2025-12-07', 'Cancelled'),
(29, 29, '604', '2025-12-04', '2025-12-08', '2025-12-07', 'Booked'),
(30, 30, '605', '2025-12-05', '2025-12-09', '2025-12-07', 'Booked'),
(31, 31, '701', '2025-12-01', '2025-12-04', '2025-12-07', 'Booked'),
(32, 32, '702', '2025-12-03', '2025-12-06', '2025-12-07', 'Checked-in'),
(33, 33, '703', '2025-12-02', '2025-12-05', '2025-12-07', 'Booked'),
(34, 34, '704', '2025-12-05', '2025-12-08', '2025-12-07', 'Booked'),
(35, 35, '705', '2025-12-06', '2025-12-09', '2025-12-07', 'Checked-out'),
(36, 36, '801', '2025-12-01', '2025-12-03', '2025-12-07', 'Booked'),
(37, 37, '802', '2025-12-02', '2025-12-05', '2025-12-07', 'Booked'),
(38, 38, '803', '2025-12-03', '2025-12-07', '2025-12-07', 'Cancelled'),
(39, 39, '804', '2025-12-04', '2025-12-08', '2025-12-07', 'Booked'),
(40, 40, '805', '2025-12-05', '2025-12-09', '2025-12-07', 'Booked'),
(41, 41, '901', '2025-12-01', '2025-12-03', '2025-12-07', 'Checked-in'),
(42, 42, '902', '2025-12-02', '2025-12-05', '2025-12-07', 'Booked'),
(43, 43, '903', '2025-12-03', '2025-12-07', '2025-12-07', 'Booked'),
(44, 44, '904', '2025-12-04', '2025-12-08', '2025-12-07', 'Cancelled'),
(45, 45, '905', '2025-12-05', '2025-12-09', '2025-12-07', 'Booked'),
(46, 46, '1001', '2025-12-01', '2025-12-03', '2025-12-07', 'Booked'),
(47, 47, '1002', '2025-12-02', '2025-12-05', '2025-12-07', 'Booked'),
(48, 48, '1003', '2025-12-03', '2025-12-07', '2025-12-07', 'Cancelled'),
(49, 49, '1004', '2025-12-04', '2025-12-08', '2025-12-07', 'Booked'),
(50, 50, '1005', '2025-12-05', '2025-12-09', '2025-12-07', 'Booked');
```

### Table 4: staff
```
+-------------+---------------+------+-----+---------+----------------+
| Field       | Type          | Null | Key | Default | Extra          |
+-------------+---------------+------+-----+---------+----------------+
| staff_id    | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| first_name  | VARCHAR(50)   | NO   |     | NULL    |                |
| last_name   | VARCHAR(50)   | NO   |     | NULL    |                |
| role        | VARCHAR(50)   | NO   |     | NULL    |                |
| department  | VARCHAR(50)   | NO   |     | NULL    |                |
| hire_date   | DATE          | NO   |     | NULL    |                |
| salary      | DECIMAL(10,2) | NO   |     | 0.00    |                |
+-------------+---------------+------+-----+---------+----------------+

+---------+------------+-----------+----------------+------------+------------+---------+
| staff_id| first_name | last_name | role           | department | hire_date  | salary  |
+---------+------------+-----------+----------------+------------+------------+---------+
| 1       | John       | Smith     | Receptionist   | Front Desk | 2022-01-10 | 2500.00 |
| 2       | Maria      | Garcia    | Housekeeper    | Housekeeping| 2021-03-15| 2000.00 |
| 3       | Chen       | Li        | Chef           | Kitchen    | 2020-07-20 | 3500.00 |
| 4       | Hiroshi    | Tanaka    | Manager        | Front Desk | 2019-05-05 | 5000.00 |
| 5       | Emma       | Brown     | Concierge      | Front Desk | 2023-02-12 | 2700.00 |
| 6       | Ahmed      | Khan      | Waiter         | Restaurant | 2021-09-01 | 2200.00 |
| 7       | Sarah      | Johnson   | Bartender      | Restaurant | 2022-06-18 | 2300.00 |
| 8       | Pedro      | Alvarez   | Housekeeper    | Housekeeping| 2020-11-20| 2000.00 |
| 9       | Li         | Wei       | Sous Chef      | Kitchen    | 2021-01-30 | 3200.00 |
| 10      | Yuki       | Sato      | Manager        | Restaurant | 2018-08-15 | 4800.00 |
| 11      | Olivia     | Williams  | Receptionist   | Front Desk | 2022-04-12 | 2500.00 |
| 12      | Khalid     | Al-Mansoor| Housekeeper    | Housekeeping| 2021-10-05| 2000.00 |
| 13      | David      | Miller    | Chef           | Kitchen    | 2019-06-18 | 3500.00 |
| 14      | Sofia      | Fernandez | Bartender      | Restaurant | 2022-09-21 | 2300.00 |
| 15      | Wang       | Mei       | Concierge      | Front Desk | 2023-01-10 | 2700.00 |
| 16      | Takashi    | Yamamoto  | Waiter         | Restaurant | 2022-07-14 | 2200.00 |
| 17      | Isabella   | Taylor    | Receptionist   | Front Desk | 2021-03-18 | 2500.00 |
| 18      | Fatima     | Al-Hadid  | Housekeeper    | Housekeeping| 2020-05-25| 2000.00 |
| 19      | Michael    | Davis     | Chef           | Kitchen    | 2018-11-02 | 3500.00 |
| 20      | Lucia      | Martinez  | Manager        | Front Desk | 2017-12-12 | 5000.00 |
| 21      | Zhou       | Fang      | Bartender      | Restaurant | 2021-06-07 | 2300.00 |
| 22      | Kenji      | Kobayashi | Sous Chef      | Kitchen    | 2020-03-15 | 3200.00 |
| 23      | Emily      | Wilson    | Receptionist   | Front Desk | 2022-08-08 | 2500.00 |
| 24      | Omar       | Al-Farsi  | Waiter         | Restaurant | 2021-02-12 | 2200.00 |
| 25      | Daniel     | Anderson  | Chef           | Kitchen    | 2019-01-21 | 3500.00 |
| 26      | Carmen     | Lopez     | Housekeeper    | Housekeeping| 2020-10-15| 2000.00 |
| 27      | Li         | Jie       | Concierge      | Front Desk | 2023-03-05 | 2700.00 |
| 28      | Haruto     | Nakamura  | Receptionist   | Front Desk | 2022-05-12 | 2500.00 |
| 29      | Grace      | Hall      | Bartender      | Restaurant | 2021-11-18 | 2300.00 |
| 30      | Aisha      | Al-Khalid | Manager        | Housekeeping| 2019-09-02| 5000.00 |
| 31      | Matthew    | Thompson  | Waiter         | Restaurant | 2022-03-25 | 2200.00 |
| 32      | Ana        | Ruiz      | Receptionist   | Front Desk | 2022-01-15 | 2500.00 |
| 33      | Liu        | Xin       | Chef           | Kitchen    | 2019-08-20 | 3500.00 |
| 34      | Riku       | Matsumoto | Sous Chef      | Kitchen    | 2020-04-18 | 3200.00 |
| 35      | Chloe      | Moore     | Housekeeper    | Housekeeping| 2021-05-22| 2000.00 |
| 36      | Hamad      | Al-Saidi  | Bartender      | Restaurant | 2021-12-01 | 2300.00 |
| 37      | Matthew    | Thompson  | Receptionist   | Front Desk | 2022-03-25 | 2500.00 |
| 38      | Elena      | Sanchez   | Chef           | Kitchen    | 2019-07-10 | 3500.00 |
| 39      | Zhang      | Lei       | Sous Chef      | Kitchen    | 2020-02-15 | 3200.00 |
| 40      | Yui        | Nakamoto  | Receptionist   | Front Desk | 2022-06-12 | 2500.00 |
| 41      | Sophie     | Clark     | Manager        | Restaurant | 2018-10-15 | 4800.00 |
| 42      | Zayed      | Al-Mansouri| Waiter        | Restaurant | 2022-01-20 | 2200.00 |
| 43      | Ryan       | Lewis     | Receptionist   | Front Desk | 2022-02-14 | 2500.00 |
| 44      | Marta      | Gonzalez  | Chef           | Kitchen    | 2019-03-08 | 3500.00 |
| 45      | Wu         | Hao       | Housekeeper    | Housekeeping| 2020-08-10| 2000.00 |
| 46      | Sora       | Fujimoto  | Concierge      | Front Desk | 2023-04-01 | 2700.00 |
| 47      | Lily       | Adams     | Bartender      | Restaurant | 2021-09-15 | 2300.00 |
| 48      | Noura      | Al-Zahra  | Housekeeper    | Housekeeping| 2020-11-05| 2000.00 |
| 49      | Ethan      | Baker     | Chef           | Kitchen    | 2019-06-30 | 3500.00 |
| 50      | Sofia      | Romero    | Receptionist   | Front Desk | 2022-05-25 | 2500.00 |
+---------+------------+-----------+----------------+------------+------------+---------+
```

```sql
CREATE TABLE staff (
    staff_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role VARCHAR(50) NOT NULL,
    department VARCHAR(50) NOT NULL,
    hire_date DATE NOT NULL,
    salary DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    PRIMARY KEY (staff_id)
) ENGINE=InnoDB;

INSERT INTO staff (staff_id, first_name, last_name, role, department, hire_date, salary) VALUES
(1, 'John', 'Smith', 'Receptionist', 'Front Desk', '2022-01-10', 2500.00),
(2, 'Maria', 'Garcia', 'Housekeeper', 'Housekeeping', '2021-03-15', 2000.00),
(3, 'Chen', 'Li', 'Chef', 'Kitchen', '2020-07-20', 3500.00),
(4, 'Hiroshi', 'Tanaka', 'Manager', 'Front Desk', '2019-05-05', 5000.00),
(5, 'Emma', 'Brown', 'Concierge', 'Front Desk', '2023-02-12', 2700.00),
(6, 'Ahmed', 'Khan', 'Waiter', 'Restaurant', '2021-09-01', 2200.00),
(7, 'Sarah', 'Johnson', 'Bartender', 'Restaurant', '2022-06-18', 2300.00),
(8, 'Pedro', 'Alvarez', 'Housekeeper', 'Housekeeping', '2020-11-20', 2000.00),
(9, 'Li', 'Wei', 'Sous Chef', 'Kitchen', '2021-01-30', 3200.00),
(10, 'Yuki', 'Sato', 'Manager', 'Restaurant', '2018-08-15', 4800.00),
(11, 'Olivia', 'Williams', 'Receptionist', 'Front Desk', '2022-04-12', 2500.00),
(12, 'Khalid', 'Al-Mansoor', 'Housekeeper', 'Housekeeping', '2021-10-05', 2000.00),
(13, 'David', 'Miller', 'Chef', 'Kitchen', '2019-06-18', 3500.00),
(14, 'Sofia', 'Fernandez', 'Bartender', 'Restaurant', '2022-09-21', 2300.00),
(15, 'Wang', 'Mei', 'Concierge', 'Front Desk', '2023-01-10', 2700.00),
(16, 'Takashi', 'Yamamoto', 'Waiter', 'Restaurant', '2022-07-14', 2200.00),
(17, 'Isabella', 'Taylor', 'Receptionist', 'Front Desk', '2021-03-18', 2500.00),
(18, 'Fatima', 'Al-Hadid', 'Housekeeper', 'Housekeeping', '2020-05-25', 2000.00),
(19, 'Michael', 'Davis', 'Chef', 'Kitchen', '2018-11-02', 3500.00),
(20, 'Lucia', 'Martinez', 'Manager', 'Front Desk', '2017-12-12', 5000.00),
(21, 'Zhou', 'Fang', 'Bartender', 'Restaurant', '2021-06-07', 2300.00),
(22, 'Kenji', 'Kobayashi', 'Sous Chef', 'Kitchen', '2020-03-15', 3200.00),
(23, 'Emily', 'Wilson', 'Receptionist', 'Front Desk', '2022-08-08', 2500.00),
(24, 'Omar', 'Al-Farsi', 'Waiter', 'Restaurant', '2021-02-12', 2200.00),
(25, 'Daniel', 'Anderson', 'Chef', 'Kitchen', '2019-01-21', 3500.00),
(26, 'Carmen', 'Lopez', 'Housekeeper', 'Housekeeping', '2020-10-15', 2000.00),
(27, 'Li', 'Jie', 'Concierge', 'Front Desk', '2023-03-05', 2700.00),
(28, 'Haruto', 'Nakamura', 'Receptionist', 'Front Desk', '2022-05-12', 2500.00),
(29, 'Grace', 'Hall', 'Bartender', 'Restaurant', '2021-11-18', 2300.00),
(30, 'Aisha', 'Al-Khalid', 'Manager', 'Housekeeping', '2019-09-02', 5000.00),
(31, 'Matthew', 'Thompson', 'Waiter', 'Restaurant', '2022-03-25', 2200.00),
(32, 'Ana', 'Ruiz', 'Receptionist', 'Front Desk', '2022-01-15', 2500.00),
(33, 'Liu', 'Xin', 'Chef', 'Kitchen', '2019-08-20', 3500.00),
(34, 'Riku', 'Matsumoto', 'Sous Chef', 'Kitchen', '2020-04-18', 3200.00),
(35, 'Chloe', 'Moore', 'Housekeeper', 'Housekeeping', '2021-05-22', 2000.00),
(36, 'Hamad', 'Al-Saidi', 'Bartender', 'Restaurant', '2021-12-01', 2300.00),
(37, 'Matthew', 'Thompson', 'Receptionist', 'Front Desk', '2022-03-25', 2500.00),
(38, 'Elena', 'Sanchez', 'Chef', 'Kitchen', '2019-07-10', 3500.00),
(39, 'Zhang', 'Lei', 'Sous Chef', 'Kitchen', '2020-02-15', 3200.00),
(40, 'Yui', 'Nakamoto', 'Receptionist', 'Front Desk', '2022-06-12', 2500.00),
(41, 'Sophie', 'Clark', 'Manager', 'Restaurant', '2018-10-15', 4800.00),
(42, 'Zayed', 'Al-Mansouri', 'Waiter', 'Restaurant', '2022-01-20', 2200.00),
(43, 'Ryan', 'Lewis', 'Receptionist', 'Front Desk', '2022-02-14', 2500.00),
(44, 'Marta', 'Gonzalez', 'Chef', 'Kitchen', '2019-03-08', 3500.00),
(45, 'Wu', 'Hao', 'Housekeeper', 'Housekeeping', '2020-08-10', 2000.00),
(46, 'Sora', 'Fujimoto', 'Concierge', 'Front Desk', '2023-04-01', 2700.00),
(47, 'Lily', 'Adams', 'Bartender', 'Restaurant', '2021-09-15', 2300.00),
(48, 'Noura', 'Al-Zahra', 'Housekeeper', 'Housekeeping', '2020-11-05', 2000.00),
(49, 'Ethan', 'Baker', 'Chef', 'Kitchen', '2019-06-30', 3500.00),
(50, 'Sofia', 'Romero', 'Receptionist', 'Front Desk', '2022-05-25', 2500.00);
```

### Table 5: services
```
+----------------+---------------+------+-----+---------+----------------+
| Field          | Type          | Null | Key | Default | Extra          |
+----------------+---------------+------+-----+---------+----------------+
| service_id     | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| booking_id     | INT           | NO   | MUL | NULL    |                |
| staff_id       | INT           | NO   | MUL | NULL    |                |
| service_type   | VARCHAR(50)   | NO   |     | NULL    |                |
| service_date   | DATE          | NO   |     | NULL    |                |
| charge         | DECIMAL(8,2)  | NO   |     | 0.00    |                |
+----------------+---------------+------+-----+---------+----------------+

+-----------+-----------+---------+----------------+------------+--------+
| service_id| booking_id| staff_id| service_type   | service_date| charge |
+-----------+-----------+---------+----------------+------------+--------+
| 1         | 1         | 2       | Room Cleaning  | 2025-12-02 | 50.00  |
| 2         | 1         | 3       | Food Delivery  | 2025-12-02 | 100.00 |
| 3         | 2         | 6       | Room Service   | 2025-12-03 | 80.00  |
| 4         | 3         | 7       | Bar Service    | 2025-12-04 | 60.00  |
| 5         | 4         | 2       | Room Cleaning  | 2025-12-06 | 50.00  |
| 6         | 5         | 3       | Food Delivery  | 2025-12-07 | 120.00 |
| 7         | 6         | 2       | Room Cleaning  | 2025-12-02 | 50.00  |
| 8         | 7         | 6       | Room Service   | 2025-12-03 | 80.00  |
| 9         | 8         | 7       | Bar Service    | 2025-12-04 | 60.00  |
| 10        | 9         | 2       | Room Cleaning  | 2025-12-06 | 50.00  |
| 11        | 10        | 3       | Food Delivery  | 2025-12-07 | 100.00 |
| 12        | 11        | 6       | Room Service   | 2025-12-08 | 80.00  |
| 13        | 12        | 7       | Bar Service    | 2025-12-09 | 60.00  |
| 14        | 13        | 2       | Room Cleaning  | 2025-12-10 | 50.00  |
| 15        | 14        | 3       | Food Delivery  | 2025-12-11 | 100.00 |
| 16        | 15        | 6       | Room Service   | 2025-12-12 | 80.00  |
| 17        | 16        | 7       | Bar Service    | 2025-12-13 | 60.00  |
| 18        | 17        | 2       | Room Cleaning  | 2025-12-14 | 50.00  |
| 19        | 18        | 3       | Food Delivery  | 2025-12-15 | 120.00 |
| 20        | 19        | 6       | Room Service   | 2025-12-16 | 80.00  |
| 21        | 20        | 7       | Bar Service    | 2025-12-17 | 60.00  |
| 22        | 21        | 2       | Room Cleaning  | 2025-12-18 | 50.00  |
| 23        | 22        | 3       | Food Delivery  | 2025-12-19 | 100.00 |
| 24        | 23        | 6       | Room Service   | 2025-12-20 | 80.00  |
| 25        | 24        | 7       | Bar Service    | 2025-12-21 | 60.00  |
| 26        | 25        | 2       | Room Cleaning  | 2025-12-22 | 50.00  |
| 27        | 26        | 3       | Food Delivery  | 2025-12-23 | 100.00 |
| 28        | 27        | 6       | Room Service   | 2025-12-24 | 80.00  |
| 29        | 28        | 7       | Bar Service    | 2025-12-25 | 60.00  |
| 30        | 29        | 2       | Room Cleaning  | 2025-12-26 | 50.00  |
| 31        | 30        | 3       | Food Delivery  | 2025-12-27 | 100.00 |
| 32        | 31        | 6       | Room Service   | 2025-12-28 | 80.00  |
| 33        | 32        | 7       | Bar Service    | 2025-12-29 | 60.00  |
| 34        | 33        | 2       | Room Cleaning  | 2025-12-30 | 50.00  |
| 35        | 34        | 3       | Food Delivery  | 2025-12-31 | 100.00 |
| 36        | 35        | 6       | Room Service   | 2026-01-01 | 80.00  |
| 37        | 36        | 7       | Bar Service    | 2026-01-02 | 60.00  |
| 38        | 37        | 2       | Room Cleaning  | 2026-01-03 | 50.00  |
| 39        | 38        | 3       | Food Delivery  | 2026-01-04 | 100.00 |
| 40        | 39        | 6       | Room Service   | 2026-01-05 | 80.00  |
| 41        | 40        | 7       | Bar Service    | 2026-01-06 | 60.00  |
| 42        | 41        | 2       | Room Cleaning  | 2026-01-07 | 50.00  |
| 43        | 42        | 3       | Food Delivery  | 2026-01-08 | 100.00 |
| 44        | 43        | 6       | Room Service   | 2026-01-09 | 80.00  |
| 45        | 44        | 7       | Bar Service    | 2026-01-10 | 60.00  |
| 46        | 45        | 2       | Room Cleaning  | 2026-01-11 | 50.00  |
| 47        | 46        | 3       | Food Delivery  | 2026-01-12 | 100.00 |
| 48        | 47        | 6       | Room Service   | 2026-01-13 | 80.00  |
| 49        | 48        | 7       | Bar Service    | 2026-01-14 | 60.00  |
| 50        | 49        | 2       | Room Cleaning  | 2026-01-15 | 50.00  |
+-----------+-----------+---------+----------------+------------+--------+
```

```sql
CREATE TABLE services (
    service_id INT NOT NULL AUTO_INCREMENT,
    booking_id INT NOT NULL,
    staff_id INT NOT NULL,
    service_type VARCHAR(50) NOT NULL,
    service_date DATE NOT NULL,
    charge DECIMAL(8,2) NOT NULL DEFAULT 0.00,
    PRIMARY KEY (service_id),
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
) ENGINE=InnoDB;

INSERT INTO services (service_id, booking_id, staff_id, service_type, service_date, charge) VALUES
(1, 1, 2, 'Room Cleaning', '2025-12-02', 50.00),
(2, 1, 3, 'Food Delivery', '2025-12-02', 100.00),
(3, 2, 6, 'Room Service', '2025-12-03', 80.00),
(4, 3, 7, 'Bar Service', '2025-12-04', 60.00),
(5, 4, 2, 'Room Cleaning', '2025-12-06', 50.00),
(6, 5, 3, 'Food Delivery', '2025-12-07', 120.00),
(7, 6, 2, 'Room Cleaning', '2025-12-02', 50.00),
(8, 7, 6, 'Room Service', '2025-12-03', 80.00),
(9, 8, 7, 'Bar Service', '2025-12-04', 60.00),
(10, 9, 2, 'Room Cleaning', '2025-12-06', 50.00),
(11, 10, 3, 'Food Delivery', '2025-12-07', 100.00),
(12, 11, 6, 'Room Service', '2025-12-08', 80.00),
(13, 12, 7, 'Bar Service', '2025-12-09', 60.00),
(14, 13, 2, 'Room Cleaning', '2025-12-10', 50.00),
(15, 14, 3, 'Food Delivery', '2025-12-11', 100.00),
(16, 15, 6, 'Room Service', '2025-12-12', 80.00),
(17, 16, 7, 'Bar Service', '2025-12-13', 60.00),
(18, 17, 2, 'Room Cleaning', '2025-12-14', 50.00),
(19, 18, 3, 'Food Delivery', '2025-12-15', 120.00),
(20, 19, 6, 'Room Service', '2025-12-16', 80.00),
(21, 20, 7, 'Bar Service', '2025-12-17', 60.00),
(22, 21, 2, 'Room Cleaning', '2025-12-18', 50.00),
(23, 22, 3, 'Food Delivery', '2025-12-19', 100.00),
(24, 23, 6, 'Room Service', '2025-12-20', 80.00),
(25, 24, 7, 'Bar Service', '2025-12-21', 60.00),
(26, 25, 2, 'Room Cleaning', '2025-12-22', 50.00),
(27, 26, 3, 'Food Delivery', '2025-12-23', 100.00),
(28, 27, 6, 'Room Service', '2025-12-24', 80.00),
(29, 28, 7, 'Bar Service', '2025-12-25', 60.00),
(30, 29, 2, 'Room Cleaning', '2025-12-26', 50.00),
(31, 30, 3, 'Food Delivery', '2025-12-27', 100.00),
(32, 31, 6, 'Room Service', '2025-12-28', 80.00),
(33, 32, 7, 'Bar Service', '2025-12-29', 60.00),
(34, 33, 2, 'Room Cleaning', '2025-12-30', 50.00),
(35, 34, 3, 'Food Delivery', '2025-12-31', 100.00),
(36, 35, 6, 'Room Service', '2026-01-01', 80.00),
(37, 36, 7, 'Bar Service', '2026-01-02', 60.00),
(38, 37, 2, 'Room Cleaning', '2026-01-03', 50.00),
(39, 38, 3, 'Food Delivery', '2026-01-04', 100.00),
(40, 39, 6, 'Room Service', '2026-01-05', 80.00),
(41, 40, 7, 'Bar Service', '2026-01-06', 60.00),
(42, 41, 2, 'Room Cleaning', '2026-01-07', 50.00),
(43, 42, 3, 'Food Delivery', '2026-01-08', 100.00),
(44, 43, 6, 'Room Service', '2026-01-09', 80.00),
(45, 44, 7, 'Bar Service', '2026-01-10', 60.00),
(46, 45, 2, 'Room Cleaning', '2026-01-11', 50.00),
(47, 46, 3, 'Food Delivery', '2026-01-12', 100.00),
(48, 47, 6, 'Room Service', '2026-01-13', 80.00),
(49, 48, 7, 'Bar Service', '2026-01-14', 60.00),
(50, 49, 2, 'Room Cleaning', '2026-01-15', 50.00);
```