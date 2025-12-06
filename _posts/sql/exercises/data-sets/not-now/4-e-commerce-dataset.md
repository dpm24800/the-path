# Sector 4: E-commerce

### Table 1: categories
```
+-------------+---------------+------+-----+---------+-------+
| Field       | Type          | Null | Key | Default | Extra |
+-------------+---------------+------+-----+---------+-------+
| category_id | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| category_name | VARCHAR(50) | NO   |     | NULL    |                |
| parent_id   | INT           | YES  | MUL | NULL    |                |
+-------------+---------------+------+-----+---------+-------+

+-------------+----------------------+-----------+
| category_id | category_name        | parent_id |
+-------------+----------------------+-----------+
| 101         | Electronics          | NULL      |
| 102         | Computers            | 101       |
| 103         | Laptops              | 102       |
| 104         | Desktops             | 102       |
| 105         | Tablets              | 102       |
| 106         | Smartphones          | 101       |
| 107         | Home Appliances      | NULL      |
| 108         | Kitchen              | 107       |
| 109         | Refrigerators        | 108       |
| 110         | Microwaves           | 108       |
| 111         | Washing Machines     | 107       |
| 112         | Fashion              | NULL      |
| 113         | Men                  | 112       |
| 114         | Women                | 112       |
| 115         | Accessories          | 112       |
| 116         | Beauty               | NULL      |
| 117         | Skincare             | 116       |
| 118         | Makeup               | 116       |
| 119         | Books                | NULL      |
| 120         | Fiction              | 119       |
| 121         | Non-Fiction          | 119       |
| 122         | Sports               | NULL      |
| 123         | Fitness Equipment    | 122       |
| 124         | Outdoor Gear         | 122       |
| 125         | Toys                 | NULL      |
+-------------+----------------------+-----------+

```

```sql
CREATE TABLE categories (
    category_id INT NOT NULL AUTO_INCREMENT,
    category_name VARCHAR(50) NOT NULL,
    parent_id INT,
    PRIMARY KEY (category_id),
    FOREIGN KEY (parent_id) REFERENCES categories(category_id)
) ENGINE=InnoDB;

INSERT INTO categories (category_name, parent_id) VALUES
('Electronics',NULL),
('Computers',101),
('Laptops',102),
('Desktops',102),
('Tablets',102),
('Smartphones',101),
('Home Appliances',NULL),
('Kitchen',107),
('Refrigerators',108),
('Microwaves',108),
('Washing Machines',107),
('Fashion',NULL),
('Men',112),
('Women',112),
('Accessories',112),
('Beauty',NULL),
('Skincare',116),
('Makeup',116),
('Books',NULL),
('Fiction',119),
('Non-Fiction',119),
('Sports',NULL),
('Fitness Equipment',122),
('Outdoor Gear',122),
('Toys',NULL);
```

### Table 2: products
```
+-------------+---------------+------+-----+---------+----------------+
| Field       | Type          | Null | Key | Default | Extra          |
+-------------+---------------+------+-----+---------+----------------+
| product_id  | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| product_name| VARCHAR(100)  | NO   |     | NULL    |                |
| category_id | INT           | NO   | MUL | NULL    |                |
| price       | DECIMAL(10,2) | NO   |     | 0.00    |                |
| stock_qty   | INT           | NO   |     | 0       |                |
| sold_qty    | INT           | NO   |     | 0       |                |
| rating      | DECIMAL(3,2)  | YES  |     | NULL    |                |
+-------------+---------------+------+-----+---------+----------------+

+------------+----------------------+------------+---------+----------+---------+--------+
| product_id | product_name         | category_id| price   | stock_qty| sold_qty| rating |
+------------+----------------------+------------+---------+----------+---------+--------+
| 201        | Dell XPS 13          | 103        | 1200.00 | 15       | 50      | 4.8    |
| 202        | MacBook Pro 14       | 103        | 2200.00 | 10       | 40      | 4.7    |
| 203        | HP Pavilion Desktop  | 104        | 800.00  | 20       | 30      | 4.3    |
| 204        | iPad Air             | 105        | 600.00  | 25       | 60      | 4.6    |
| 205        | Samsung Galaxy S23   | 106        | 999.00  | 30       | 70      | 4.5    |
| 206        | LG Refrigerator 300L | 109        | 1200.00 | 8        | 15      | 4.4    |
| 207        | Samsung Microwave    | 110        | 250.00  | 12       | 20      | 4.2    |
| 208        | Bosch Washing Machine| 111        | 700.00  | 7        | 18      | 4.3    |
| 209        | Men Leather Jacket   | 113        | 150.00  | 50       | 100     | 4.6    |
| 210        | Women Handbag        | 114        | 120.00  | 40       | 90      | 4.7    |
| 211        | Fashion Sunglasses   | 115        | 80.00   | 60       | 120     | 4.5    |
| 212        | Skincare Set         | 117        | 50.00   | 70       | 100     | 4.6    |
| 213        | Makeup Kit           | 118        | 75.00   | 60       | 80      | 4.5    |
| 214        | Fiction Bestseller   | 120        | 20.00   | 100      | 300     | 4.8    |
| 215        | Non-Fiction Classic  | 121        | 25.00   | 80       | 200     | 4.7    |
| 216        | Treadmill Pro        | 123        | 1200.00 | 5        | 12      | 4.4    |
| 217        | Yoga Mat Deluxe      | 124        | 35.00   | 50       | 90      | 4.6    |
| 218        | Lego Star Wars Set   | 125        | 150.00  | 20       | 40      | 4.9    |
| 219        | iMac 24              | 104        | 1800.00 | 10       | 25      | 4.6    |
| 220        | Samsung Galaxy Tab   | 105        | 550.00  | 20       | 45      | 4.5    |
| 221        | Acer Predator Laptop | 103        | 1500.00 | 12       | 30      | 4.7    |
| 222        | HP Envy Laptop       | 103        | 1100.00 | 18       | 40      | 4.5    |
| 223        | iPhone 14            | 106        | 1099.00 | 25       | 60      | 4.6    |
| 224        | Sony Microwave       | 110        | 200.00  | 15       | 25      | 4.3    |
| 225        | Whirlpool Refrigerator | 109      | 1300.00 | 6        | 10      | 4.4    |
| 226        | Men Sneakers         | 113        | 90.00   | 60       | 110     | 4.7    |
| 227        | Women Dress          | 114        | 80.00   | 50       | 100     | 4.6    |
| 228        | Smartwatch Pro       | 106        | 250.00  | 30       | 70      | 4.5    |
| 229        | Gaming Mouse         | 102        | 75.00   | 100      | 200     | 4.6    |
| 230        | Mechanical Keyboard  | 102        | 120.00  | 80       | 150     | 4.7    |
| 231        | Blender Pro          | 108        | 60.00   | 25       | 40      | 4.4    |
| 232        | Coffee Maker Deluxe  | 108        | 80.00   | 30       | 50      | 4.5    |
| 233        | Men Jeans            | 113        | 50.00   | 70       | 120     | 4.6    |
| 234        | Women Jacket         | 114        | 120.00  | 40       | 80      | 4.7    |
| 235        | Hair Dryer           | 116        | 30.00   | 60       | 90      | 4.5    |
| 236        | Facial Cream         | 117        | 40.00   | 50       | 80      | 4.6    |
| 237        | Novel Collection Set | 120        | 60.00   | 30       | 70      | 4.8    |
| 238        | Science Book Set     | 121        | 70.00   | 25       | 50      | 4.7    |
| 239        | Exercise Bike        | 123        | 800.00  | 10       | 20      | 4.4    |
| 240        | Dumbbell Set         | 123        | 150.00  | 20       | 50      | 4.6    |
| 241        | Football             | 124        | 25.00   | 100      | 200     | 4.5    |
| 242        | Basketball           | 124        | 30.00   | 80       | 150     | 4.6    |
| 243        | Drone X Pro          | 101        | 500.00  | 15       | 25      | 4.7    |
| 244        | GoPro Hero           | 101        | 400.00  | 10       | 20      | 4.8    |
| 245        | Tablet Samsung Tab S8| 105        | 650.00  | 12       | 30      | 4.6    |
| 246        | Kindle Paperwhite    | 119        | 130.00  | 25       | 60      | 4.8    |
| 247        | Gaming Chair Pro     | 102        | 200.00  | 10       | 25      | 4.5    |
| 248        | Men T-Shirt          | 113        | 25.00   | 80       | 150     | 4.6    |
| 249        | Women Skirt          | 114        | 35.00   | 60       | 120     | 4.7    |
| 250        | Toy Car Set          | 125        | 45.00   | 30       | 60      | 4.8    |
+------------+----------------------+------------+---------+----------+---------+--------+
```

```sql
CREATE TABLE products (
    product_id INT NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category_id INT NOT NULL,
    price DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    stock_qty INT NOT NULL DEFAULT 0,
    sold_qty INT NOT NULL DEFAULT 0,
    rating DECIMAL(3,2),
    PRIMARY KEY (product_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
) ENGINE=InnoDB;

INSERT INTO products (product_id, product_name, category_id, price, stock_qty, sold_qty, rating) VALUES
(201, 'Dell XPS 13', 103, 1200.00, 15, 50, 4.8),
(202, 'MacBook Pro 14', 103, 2200.00, 10, 40, 4.7),
(203, 'HP Pavilion Desktop', 104, 800.00, 20, 30, 4.3),
(204, 'iPad Air', 105, 600.00, 25, 60, 4.6),
(205, 'Samsung Galaxy S23', 106, 999.00, 30, 70, 4.5),
(206, 'LG Refrigerator 300L', 109, 1200.00, 8, 15, 4.4),
(207, 'Samsung Microwave', 110, 250.00, 12, 20, 4.2),
(208, 'Bosch Washing Machine', 111, 700.00, 7, 18, 4.3),
(209, 'Men Leather Jacket', 113, 150.00, 50, 100, 4.6),
(210, 'Women Handbag', 114, 120.00, 40, 90, 4.7),
(211, 'Fashion Sunglasses', 115, 80.00, 60, 120, 4.5),
(212, 'Skincare Set', 117, 50.00, 70, 100, 4.6),
(213, 'Makeup Kit', 118, 75.00, 60, 80, 4.5),
(214, 'Fiction Bestseller', 120, 20.00, 100, 300, 4.8),
(215, 'Non-Fiction Classic', 121, 25.00, 80, 200, 4.7),
(216, 'Treadmill Pro', 123, 1200.00, 5, 12, 4.4),
(217, 'Yoga Mat Deluxe', 124, 35.00, 50, 90, 4.6),
(218, 'Lego Star Wars Set', 125, 150.00, 20, 40, 4.9),
(219, 'iMac 24', 104, 1800.00, 10, 25, 4.6),
(220, 'Samsung Galaxy Tab', 105, 550.00, 20, 45, 4.5),
(221, 'Acer Predator Laptop', 103, 1500.00, 12, 30, 4.7),
(222, 'HP Envy Laptop', 103, 1100.00, 18, 40, 4.5),
(223, 'iPhone 14', 106, 1099.00, 25, 60, 4.6),
(224, 'Sony Microwave', 110, 200.00, 15, 25, 4.3),
(225, 'Whirlpool Refrigerator', 109, 1300.00, 6, 10, 4.4),
(226, 'Men Sneakers', 113, 90.00, 60, 110, 4.7),
(227, 'Women Dress', 114, 80.00, 50, 100, 4.6),
(228, 'Smartwatch Pro', 106, 250.00, 30, 70, 4.5),
(229, 'Gaming Mouse', 102, 75.00, 100, 200, 4.6),
(230, 'Mechanical Keyboard', 102, 120.00, 80, 150, 4.7),
(231, 'Blender Pro', 108, 60.00, 25, 40, 4.4),
(232, 'Coffee Maker Deluxe', 108, 80.00, 30, 50, 4.5),
(233, 'Men Jeans', 113, 50.00, 70, 120, 4.6),
(234, 'Women Jacket', 114, 120.00, 40, 80, 4.7),
(235, 'Hair Dryer', 116, 30.00, 60, 90, 4.5),
(236, 'Facial Cream', 117, 40.00, 50, 80, 4.6),
(237, 'Novel Collection Set', 120, 60.00, 30, 70, 4.8),
(238, 'Science Book Set', 121, 70.00, 25, 50, 4.7),
(239, 'Exercise Bike', 123, 800.00, 10, 20, 4.4),
(240, 'Dumbbell Set', 123, 150.00, 20, 50, 4.6),
(241, 'Football', 124, 25.00, 100, 200, 4.5),
(242, 'Basketball', 124, 30.00, 80, 150, 4.6),
(243, 'Drone X Pro', 101, 500.00, 15, 25, 4.7),
(244, 'GoPro Hero', 101, 400.00, 10, 20, 4.8),
(245, 'Tablet Samsung Tab S8', 105, 650.00, 12, 30, 4.6),
(246, 'Kindle Paperwhite', 119, 130.00, 25, 60, 4.8),
(247, 'Gaming Chair Pro', 102, 200.00, 10, 25, 4.5),
(248, 'Men T-Shirt', 113, 25.00, 80, 150, 4.6),
(249, 'Women Skirt', 114, 35.00, 60, 120, 4.7),
(250, 'Toy Car Set', 125, 45.00, 30, 60, 4.8);
```

### Table 3: customers
```
+-------------+---------------+------+-----+---------+----------------+
| Field       | Type          | Null | Key | Default | Extra          |
+-------------+---------------+------+-----+---------+----------------+
| customer_id | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| first_name  | VARCHAR(50)   | NO   |     | NULL    |                |
| last_name   | VARCHAR(50)   | NO   |     | NULL    |                |
| email       | VARCHAR(100)  | NO   | UNI | NULL    |                |
| phone       | VARCHAR(15)   | YES  |     | NULL    |                |
| join_date   | DATE          | NO   |     | NULL    |                |
| address     | VARCHAR(150)  | YES  |     | NULL    |                |
+-------------+---------------+------+-----+---------+----------------+

+-------------+------------+-----------+-------------------------+-------------+------------+-------------------------+
| customer_id | first_name | last_name | email                   | phone       | join_date  | address                 |
+-------------+------------+-----------+-------------------------+-------------+------------+-------------------------+
| 301         | Alice      | Smith     | alice.smith@mail.com    | 9876500001  | 2023-01-05 | 123 Main St, City A    |
| 302         | Bob        | Johnson   | bob.johnson@mail.com    | 9876500002  | 2023-01-10 | 456 Oak Ave, City B    |
| 303         | Charlie    | Brown     | charlie.brown@mail.com  | 9876500003  | 2023-01-15 | 789 Pine Rd, City C    |
| 304         | David      | Wilson    | david.wilson@mail.com   | 9876500004  | 2023-01-20 | 12 Elm St, City D      |
| 305         | Emma       | Taylor    | emma.taylor@mail.com    | 9876500005  | 2023-01-25 | 34 Maple St, City E    |
| 306         | Frank      | Anderson  | frank.anderson@mail.com | 9876500006  | 2023-02-01 | 56 Cedar Rd, City F    |
| 307         | Grace      | Thomas    | grace.thomas@mail.com   | 9876500007  | 2023-02-05 | 78 Birch Ln, City G    |
| 308         | Henry      | Jackson   | henry.jackson@mail.com  | 9876500008  | 2023-02-10 | 90 Walnut Ave, City H  |
| 309         | Isabella   | White     | isabella.white@mail.com | 9876500009  | 2023-02-15 | 11 Cherry St, City I   |
| 310         | Jack       | Harris    | jack.harris@mail.com    | 9876500010  | 2023-02-20 | 22 Ash Rd, City J      |
| 311         | Karen      | Martin    | karen.martin@mail.com   | 9876500011  | 2023-02-25 | 33 Poplar St, City K   |
| 312         | Liam       | Thompson  | liam.thompson@mail.com  | 9876500012  | 2023-03-01 | 44 Spruce Ave, City L  |
| 313         | Mia        | Garcia    | mia.garcia@mail.com     | 9876500013  | 2023-03-05 | 55 Fir Rd, City M      |
| 314         | Noah       | Martinez  | noah.martinez@mail.com  | 9876500014  | 2023-03-10 | 66 Hemlock Ln, City N  |
| 315         | Olivia     | Robinson  | olivia.robinson@mail.com| 9876500015  | 2023-03-15 | 77 Cypress St, City O  |
| 316         | Paul       | Clark     | paul.clark@mail.com     | 9876500016  | 2023-03-20 | 88 Pinecone Rd, City P |
| 317         | Quinn      | Rodriguez | quinn.rodriguez@mail.com| 9876500017 | 2023-03-25 | 99 Willow Ave, City Q  |
| 318         | Rachel     | Lewis     | rachel.lewis@mail.com   | 9876500018  | 2023-03-30 | 101 Maple St, City R   |
| 319         | Samuel     | Lee       | samuel.lee@mail.com     | 9876500019  | 2023-04-05 | 202 Oak Rd, City S     |
| 320         | Tina       | Walker    | tina.walker@mail.com    | 9876500020  | 2023-04-10 | 303 Pine St, City T    |
| 321         | Ursula     | Hall      | ursula.hall@mail.com    | 9876500021  | 2023-04-15 | 404 Cedar Ln, City U   |
| 322         | Victor     | Allen     | victor.allen@mail.com   | 9876500022  | 2023-04-20 | 505 Birch Rd, City V   |
| 323         | Wendy      | Young     | wendy.young@mail.com    | 9876500023  | 2023-04-25 | 606 Spruce St, City W  |
| 324         | Xavier     | Hernandez | xavier.hernandez@mail.com| 9876500024| 2023-05-01 | 707 Fir Ave, City X    |
| 325         | Yvonne     | King      | yvonne.king@mail.com    | 9876500025  | 2023-05-05 | 808 Hemlock Rd, City Y |
| 326         | Zachary    | Wright    | zachary.wright@mail.com | 9876500026  | 2023-05-10 | 909 Cypress Ln, City Z |
| 327         | Abigail    | Lopez     | abigail.lopez@mail.com  | 9876500027  | 2023-05-15 | 123 Elm St, City A1    |
| 328         | Brandon    | Hill      | brandon.hill@mail.com   | 9876500028  | 2023-05-20 | 234 Maple Ave, City B1 |
| 329         | Chloe      | Scott     | chloe.scott@mail.com    | 9876500029  | 2023-05-25 | 345 Oak Rd, City C1    |
| 330         | Daniel     | Green     | daniel.green@mail.com   | 9876500030  | 2023-05-30 | 456 Pine Ln, City D1   |
| 331         | Ella       | Adams     | ella.adams@mail.com     | 9876500031  | 2023-06-05 | 567 Cedar St, City E1  |
| 332         | Felix      | Baker     | felix.baker@mail.com    | 9876500032  | 2023-06-10 | 678 Birch Rd, City F1  |
| 333         | Gabriella  | Nelson    | gabriella.nelson@mail.com| 9876500033| 2023-06-15 | 789 Spruce Ave, City G1|
| 334         | Harrison   | Carter    | harrison.carter@mail.com| 9876500034  | 2023-06-20 | 890 Fir Rd, City H1    |
| 335         | Isabelle   | Mitchell  | isabelle.mitchell@mail.com| 9876500035| 2023-06-25 | 901 Hemlock Ln, City I1|
| 336         | Jason      | Perez     | jason.perez@mail.com    | 9876500036  | 2023-07-01 | 101 Cypress St, City J1|
| 337         | Kaitlyn    | Roberts   | kaitlyn.roberts@mail.com| 9876500037 | 2023-07-05 | 202 Elm Rd, City K1    |
| 338         | Leo        | Turner    | leo.turner@mail.com     | 9876500038  | 2023-07-10 | 303 Maple Ln, City L1  |
| 339         | Madison    | Phillips  | madison.phillips@mail.com|9876500039| 2023-07-15 | 404 Oak St, City M1    |
| 340         | Nathan     | Campbell  | nathan.campbell@mail.com| 9876500040| 2023-07-20 | 505 Pine Ave, City N1  |
| 341         | Olivia     | Parker    | olivia.parker@mail.com  | 9876500041 | 2023-07-25 | 606 Cedar Rd, City O1  |
| 342         | Patrick    | Evans     | patrick.evans@mail.com  | 9876500042 | 2023-07-30 | 707 Birch Ln, City P1  |
| 343         | Quinn      | Edwards   | quinn.edwards@mail.com  | 9876500043 | 2023-08-05 | 808 Spruce St, City Q1 |
| 344         | Riley      | Collins   | riley.collins@mail.com  | 9876500044 | 2023-08-10 | 909 Fir Rd, City R1    |
| 345         | Sophia     | Stewart   | sophia.stewart@mail.com | 9876500045 | 2023-08-15 | 101 Hemlock Ave, City S1|
| 346         | Thomas     | Sanchez   | thomas.sanchez@mail.com | 9876500046 | 2023-08-20 | 202 Cypress Rd, City T1|
| 347         | Uma        | Morris    | uma.morris@mail.com     | 9876500047 | 2023-08-25 | 303 Elm St, City U1    |
| 348         | Vincent    | Rogers    | vincent.rogers@mail.com | 9876500048 | 2023-08-30 | 404 Maple Rd, City V1  |
| 349         | Willow     | Reed      | willow.reed@mail.com    | 9876500049 | 2023-09-05 | 505 Oak Ln, City W1    |
| 350         | Xavier     | Cook      | xavier.cook@mail.com    | 9876500050 | 2023-09-10 | 606 Pine St, City X1   |
+-------------+------------+-----------+-------------------------+-------------+------------+-------------------------+
```

```sql
CREATE TABLE customers (
    customer_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15),
    join_date DATE NOT NULL,
    address VARCHAR(150),
    PRIMARY KEY (customer_id)
) ENGINE=InnoDB;

INSERT INTO customers (customer_id, first_name, last_name, email, phone, join_date, address) VALUES
(301, 'Alice', 'Smith', 'alice.smith@mail.com', '9876500001', '2023-01-05', '123 Main St, City A'),
(302, 'Bob', 'Johnson', 'bob.johnson@mail.com', '9876500002', '2023-01-10', '456 Oak Ave, City B'),
(303, 'Charlie', 'Brown', 'charlie.brown@mail.com', '9876500003', '2023-01-15', '789 Pine Rd, City C'),
(304, 'David', 'Wilson', 'david.wilson@mail.com', '9876500004', '2023-01-20', '12 Elm St, City D'),
(305, 'Emma', 'Taylor', 'emma.taylor@mail.com', '9876500005', '2023-01-25', '34 Maple St, City E'),
(306, 'Frank', 'Anderson', 'frank.anderson@mail.com', '9876500006', '2023-02-01', '56 Cedar Rd, City F'),
(307, 'Grace', 'Thomas', 'grace.thomas@mail.com', '9876500007', '2023-02-05', '78 Birch Ln, City G'),
(308, 'Henry', 'Jackson', 'henry.jackson@mail.com', '9876500008', '2023-02-10', '90 Walnut Ave, City H'),
(309, 'Isabella', 'White', 'isabella.white@mail.com', '9876500009', '2023-02-15', '11 Cherry St, City I'),
(310, 'Jack', 'Harris', 'jack.harris@mail.com', '9876500010', '2023-02-20', '22 Ash Rd, City J'),
(311, 'Karen', 'Martin', 'karen.martin@mail.com', '9876500011', '2023-02-25', '33 Poplar St, City K'),
(312, 'Liam', 'Thompson', 'liam.thompson@mail.com', '9876500012', '2023-03-01', '44 Spruce Ave, City L'),
(313, 'Mia', 'Garcia', 'mia.garcia@mail.com', '9876500013', '2023-03-05', '55 Fir Rd, City M'),
(314, 'Noah', 'Martinez', 'noah.martinez@mail.com', '9876500014', '2023-03-10', '66 Hemlock Ln, City N'),
(315, 'Olivia', 'Robinson', 'olivia.robinson@mail.com', '9876500015', '2023-03-15', '77 Cypress St, City O'),
(316, 'Paul', 'Clark', 'paul.clark@mail.com', '9876500016', '2023-03-20', '88 Pinecone Rd, City P'),
(317, 'Quinn', 'Rodriguez', 'quinn.rodriguez@mail.com', '9876500017', '2023-03-25', '99 Willow Ave, City Q'),
(318, 'Rachel', 'Lewis', 'rachel.lewis@mail.com', '9876500018', '2023-03-30', '101 Maple St, City R'),
(319, 'Samuel', 'Lee', 'samuel.lee@mail.com', '9876500019', '2023-04-05', '202 Oak Rd, City S'),
(320, 'Tina', 'Walker', 'tina.walker@mail.com', '9876500020', '2023-04-10', '303 Pine St, City T'),
(321, 'Ursula', 'Hall', 'ursula.hall@mail.com', '9876500021', '2023-04-15', '404 Cedar Ln, City U'),
(322, 'Victor', 'Allen', 'victor.allen@mail.com', '9876500022', '2023-04-20', '505 Birch Rd, City V'),
(323, 'Wendy', 'Young', 'wendy.young@mail.com', '9876500023', '2023-04-25', '606 Spruce St, City W'),
(324, 'Xavier', 'Hernandez', 'xavier.hernandez@mail.com', '9876500024', '2023-05-01', '707 Fir Ave, City X'),
(325, 'Yvonne', 'King', 'yvonne.king@mail.com', '9876500025', '2023-05-05', '808 Hemlock Rd, City Y'),
(326, 'Zachary', 'Wright', 'zachary.wright@mail.com', '9876500026', '2023-05-10', '909 Cypress Ln, City Z'),
(327, 'Abigail', 'Lopez', 'abigail.lopez@mail.com', '9876500027', '2023-05-15', '123 Elm St, City A1'),
(328, 'Brandon', 'Hill', 'brandon.hill@mail.com', '9876500028', '2023-05-20', '234 Maple Ave, City B1'),
(329, 'Chloe', 'Scott', 'chloe.scott@mail.com', '9876500029', '2023-05-25', '345 Oak Rd, City C1'),
(330, 'Daniel', 'Green', 'daniel.green@mail.com', '9876500030', '2023-05-30', '456 Pine Ln, City D1'),
(331, 'Ella', 'Adams', 'ella.adams@mail.com', '9876500031', '2023-06-05', '567 Cedar St, City E1'),
(332, 'Felix', 'Baker', 'felix.baker@mail.com', '9876500032', '2023-06-10', '678 Birch Rd, City F1'),
(333, 'Gabriella', 'Nelson', 'gabriella.nelson@mail.com', '9876500033', '2023-06-15', '789 Spruce Ave, City G1'),
(334, 'Harrison', 'Carter', 'harrison.carter@mail.com', '9876500034', '2023-06-20', '890 Fir Rd, City H1'),
(335, 'Isabelle', 'Mitchell', 'isabelle.mitchell@mail.com', '9876500035', '2023-06-25', '901 Hemlock Ln, City I1'),
(336, 'Jason', 'Perez', 'jason.perez@mail.com', '9876500036', '2023-07-01', '101 Cypress St, City J1'),
(337, 'Kaitlyn', 'Roberts', 'kaitlyn.roberts@mail.com', '9876500037', '2023-07-05', '202 Elm Rd, City K1'),
(338, 'Leo', 'Turner', 'leo.turner@mail.com', '9876500038', '2023-07-10', '303 Maple Ln, City L1'),
(339, 'Madison', 'Phillips', 'madison.phillips@mail.com', '9876500039', '2023-07-15', '404 Oak St, City M1'),
(340, 'Nathan', 'Campbell', 'nathan.campbell@mail.com', '9876500040', '2023-07-20', '505 Pine Ave, City N1'),
(341, 'Olivia', 'Parker', 'olivia.parker@mail.com', '9876500041', '2023-07-25', '606 Cedar Rd, City O1'),
(342, 'Patrick', 'Evans', 'patrick.evans@mail.com', '9876500042', '2023-07-30', '707 Birch Ln, City P1'),
(343, 'Quinn', 'Edwards', 'quinn.edwards@mail.com', '9876500043', '2023-08-05', '808 Spruce St, City Q1'),
(344, 'Riley', 'Collins', 'riley.collins@mail.com', '9876500044', '2023-08-10', '909 Fir Rd, City R1'),
(345, 'Sophia', 'Stewart', 'sophia.stewart@mail.com', '9876500045', '2023-08-15', '101 Hemlock Ave, City S1'),
(346, 'Thomas', 'Sanchez', 'thomas.sanchez@mail.com', '9876500046', '2023-08-20', '202 Cypress Rd, City T1'),
(347, 'Uma', 'Morris', 'uma.morris@mail.com', '9876500047', '2023-08-25', '303 Elm St, City U1'),
(348, 'Vincent', 'Rogers', 'vincent.rogers@mail.com', '9876500048', '2023-08-30', '404 Maple Rd, City V1'),
(349, 'Willow', 'Reed', 'willow.reed@mail.com', '9876500049', '2023-09-05', '505 Oak Ln, City W1'),
(350, 'Xavier', 'Cook', 'xavier.cook@mail.com', '9876500050', '2023-09-10', '606 Pine St, City X1');
```

### Table 4: orders
```
+------------+------------+------+-----+---------+----------------+
| Field      | Type       | Null | Key | Default | Extra          |
+------------+------------+------+-----+---------+----------------+
| order_id   | INT        | NO   | PRI | NULL    | AUTO_INCREMENT |
| customer_id| INT        | NO   | MUL | NULL    |                |
| order_date | DATE       | NO   |     | NULL    |                |
| total_amt  | DECIMAL(10,2)| NO |     | 0.00    |                |
| status     | VARCHAR(20)| NO   |     | 'Pending' |              |
+------------+------------+------+-----+---------+----------------+

+----------+-------------+------------+----------+---------+
| order_id | customer_id | order_date | total_amt| status  |
+----------+-------------+------------+----------+---------+
| 1001     | 301         | 2023-02-01 | 1200.00  | Shipped |
| 1002     | 302         | 2023-02-03 | 2200.00  | Delivered|
| 1003     | 303         | 2023-02-05 | 800.00   | Cancelled|
| 1004     | 304         | 2023-02-07 | 600.00   | Shipped  |
| 1005     | 305         | 2023-02-10 | 999.00   | Delivered|
| 1006     | 306         | 2023-02-12 | 1200.00  | Pending  |
| 1007     | 307         | 2023-02-15 | 250.00   | Shipped  |
| 1008     | 308         | 2023-02-17 | 700.00   | Delivered|
| 1009     | 309         | 2023-02-20 | 150.00   | Shipped  |
| 1010     | 310         | 2023-02-22 | 120.00   | Pending  |
| 1011     | 311         | 2023-02-25 | 50.00    | Delivered|
| 1012     | 312         | 2023-03-01 | 75.00    | Shipped  |
| 1013     | 313         | 2023-03-03 | 20.00    | Delivered|
| 1014     | 314         | 2023-03-05 | 25.00    | Cancelled|
| 1015     | 315         | 2023-03-07 | 1200.00  | Shipped  |
| 1016     | 316         | 2023-03-10 | 35.00    | Delivered|
| 1017     | 317         | 2023-03-12 | 45.00    | Pending  |
| 1018     | 318         | 2023-03-15 | 60.00    | Shipped  |
| 1019     | 319         | 2023-03-17 | 80.00    | Delivered|
| 1020     | 320         | 2023-03-20 | 150.00   | Shipped  |
| 1021     | 321         | 2023-03-22 | 200.00   | Delivered|
| 1022     | 322         | 2023-03-25 | 300.00   | Shipped  |
| 1023     | 323         | 2023-03-27 | 400.00   | Pending  |
| 1024     | 324         | 2023-03-30 | 500.00   | Shipped  |
| 1025     | 325         | 2023-04-02 | 600.00   | Delivered|
| 1026     | 326         | 2023-04-05 | 700.00   | Cancelled|
| 1027     | 327         | 2023-04-07 | 800.00   | Shipped  |
| 1028     | 328         | 2023-04-10 | 900.00   | Delivered|
| 1029     | 329         | 2023-04-12 | 1000.00  | Shipped  |
| 1030     | 330         | 2023-04-15 | 1100.00  | Pending  |
| 1031     | 331         | 2023-04-17 | 1200.00  | Delivered|
| 1032     | 332         | 2023-04-20 | 1300.00  | Shipped  |
| 1033     | 333         | 2023-04-22 | 1400.00  | Cancelled|
| 1034     | 334         | 2023-04-25 | 1500.00  | Shipped  |
| 1035     | 335         | 2023-04-27 | 1600.00  | Delivered|
| 1036     | 336         | 2023-04-30 | 1700.00  | Shipped  |
| 1037     | 337         | 2023-05-02 | 1800.00  | Pending  |
| 1038     | 338         | 2023-05-05 | 1900.00  | Shipped  |
| 1039     | 339         | 2023-05-07 | 2000.00  | Delivered|
| 1040     | 340         | 2023-05-10 | 2100.00  | Shipped  |
| 1041     | 341         | 2023-05-12 | 2200.00  | Pending  |
| 1042     | 342         | 2023-05-15 | 2300.00  | Shipped  |
| 1043     | 343         | 2023-05-17 | 2400.00  | Delivered|
| 1044     | 344         | 2023-05-20 | 2500.00  | Shipped  |
| 1045     | 345         | 2023-05-22 | 2600.00  | Pending  |
| 1046     | 346         | 2023-05-25 | 2700.00  | Shipped  |
| 1047     | 347         | 2023-05-27 | 2800.00  | Delivered|
| 1048     | 348         | 2023-05-30 | 2900.00  | Shipped  |
| 1049     | 349         | 2023-06-02 | 3000.00  | Pending  |
| 1050     | 350         | 2023-06-05 | 3100.00  | Shipped  |
+----------+-------------+------------+----------+---------+
```

```sql
CREATE TABLE orders (
    order_id INT NOT NULL AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    total_amt DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    status VARCHAR(20) NOT NULL DEFAULT 'Pending',
    PRIMARY KEY (order_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
) ENGINE=InnoDB;

INSERT INTO orders (order_id, customer_id, order_date, total_amt, status) VALUES
(1001, 301, '2023-02-01', 1200.00, 'Shipped'),
(1002, 302, '2023-02-03', 2200.00, 'Delivered'),
(1003, 303, '2023-02-05', 800.00, 'Cancelled'),
(1004, 304, '2023-02-07', 600.00, 'Shipped'),
(1005, 305, '2023-02-10', 999.00, 'Delivered'),
(1006, 306, '2023-02-12', 1200.00, 'Pending'),
(1007, 307, '2023-02-15', 250.00, 'Shipped'),
(1008, 308, '2023-02-17', 700.00, 'Delivered'),
(1009, 309, '2023-02-20', 150.00, 'Shipped'),
(1010, 310, '2023-02-22', 120.00, 'Pending'),
(1011, 311, '2023-02-25', 50.00, 'Delivered'),
(1012, 312, '2023-03-01', 75.00, 'Shipped'),
(1013, 313, '2023-03-03', 20.00, 'Delivered'),
(1014, 314, '2023-03-05', 25.00, 'Cancelled'),
(1015, 315, '2023-03-07', 1200.00, 'Shipped'),
(1016, 316, '2023-03-10', 35.00, 'Delivered'),
(1017, 317, '2023-03-12', 45.00, 'Pending'),
(1018, 318, '2023-03-15', 60.00, 'Shipped'),
(1019, 319, '2023-03-17', 80.00, 'Delivered'),
(1020, 320, '2023-03-20', 150.00, 'Shipped'),
(1021, 321, '2023-03-22', 200.00, 'Delivered'),
(1022, 322, '2023-03-25', 300.00, 'Shipped'),
(1023, 323, '2023-03-27', 400.00, 'Pending'),
(1024, 324, '2023-03-30', 500.00, 'Shipped'),
(1025, 325, '2023-04-02', 600.00, 'Delivered'),
(1026, 326, '2023-04-05', 700.00, 'Cancelled'),
(1027, 327, '2023-04-07', 800.00, 'Shipped'),
(1028, 328, '2023-04-10', 900.00, 'Delivered'),
(1029, 329, '2023-04-12', 1000.00, 'Shipped'),
(1030, 330, '2023-04-15', 1100.00, 'Pending'),
(1031, 331, '2023-04-17', 1200.00, 'Delivered'),
(1032, 332, '2023-04-20', 1300.00, 'Shipped'),
(1033, 333, '2023-04-22', 1400.00, 'Cancelled'),
(1034, 334, '2023-04-25', 1500.00, 'Shipped'),
(1035, 335, '2023-04-27', 1600.00, 'Delivered'),
(1036, 336, '2023-04-30', 1700.00, 'Shipped'),
(1037, 337, '2023-05-02', 1800.00, 'Pending'),
(1038, 338, '2023-05-05', 1900.00, 'Shipped'),
(1039, 339, '2023-05-07', 2000.00, 'Delivered'),
(1040, 340, '2023-05-10', 2100.00, 'Shipped'),
(1041, 341, '2023-05-12', 2200.00, 'Pending'),
(1042, 342, '2023-05-15', 2300.00, 'Shipped'),
(1043, 343, '2023-05-17', 2400.00, 'Delivered'),
(1044, 344, '2023-05-20', 2500.00, 'Shipped'),
(1045, 345, '2023-05-22', 2600.00, 'Pending'),
(1046, 346, '2023-05-25', 2700.00, 'Shipped'),
(1047, 347, '2023-05-27', 2800.00, 'Delivered'),
(1048, 348, '2023-05-30', 2900.00, 'Shipped'),
(1049, 349, '2023-06-02', 3000.00, 'Pending'),
(1050, 350, '2023-06-05', 3100.00, 'Shipped');
```


### Table 5: order_items
```
+------------+---------------+------+-----+---------+----------------+
| Field      | Type          | Null | Key | Default | Extra          |
+------------+---------------+------+-----+---------+----------------+
| item_id    | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| order_id   | INT           | NO   | MUL | NULL    |                |
| product_id | INT           | NO   | MUL | NULL    |                |
| quantity   | INT           | NO   |     | 1       |                |
| unit_price | DECIMAL(10,2) | NO   |     | 0.00    |                |
| total_amt  | DECIMAL(10,2) | NO   |     | 0.00    |                |
+------------+---------------+------+-----+---------+----------------+

+--------+----------+------------+----------+-----------+-----------+
| item_id| order_id | product_id | quantity | unit_price| total_amt |
+--------+----------+------------+----------+-----------+-----------+
| 1      | 1001     | 201        | 1        | 1200.00   | 1200.00   |
| 2      | 1002     | 202        | 1        | 2200.00   | 2200.00   |
| 3      | 1003     | 203        | 1        | 800.00    | 800.00    |
| 4      | 1004     | 204        | 1        | 600.00    | 600.00    |
| 5      | 1005     | 205        | 1        | 999.00    | 999.00    |
| 6      | 1006     | 206        | 1        | 1200.00   | 1200.00   |
| 7      | 1007     | 207        | 1        | 250.00    | 250.00    |
| 8      | 1008     | 208        | 1        | 700.00    | 700.00    |
| 9      | 1009     | 209        | 2        | 150.00    | 300.00    |
| 10     | 1010     | 210        | 1        | 120.00    | 120.00    |
| 11     | 1011     | 212        | 1        | 50.00     | 50.00     |
| 12     | 1012     | 213        | 1        | 75.00     | 75.00     |
| 13     | 1013     | 214        | 1        | 20.00     | 20.00     |
| 14     | 1014     | 215        | 1        | 25.00     | 25.00     |
| 15     | 1015     | 216        | 1        | 1200.00   | 1200.00   |
| 16     | 1016     | 217        | 2        | 35.00     | 70.00     |
| 17     | 1017     | 218        | 1        | 150.00    | 150.00    |
| 18     | 1018     | 219        | 1        | 1800.00   | 1800.00   |
| 19     | 1019     | 220        | 1        | 550.00    | 550.00    |
| 20     | 1020     | 221        | 1        | 1500.00   | 1500.00   |
| 21     | 1021     | 222        | 1        | 1100.00   | 1100.00   |
| 22     | 1022     | 223        | 1        | 1099.00   | 1099.00   |
| 23     | 1023     | 224        | 1        | 200.00    | 200.00    |
| 24     | 1024     | 225        | 1        | 1300.00   | 1300.00   |
| 25     | 1025     | 226        | 2        | 90.00     | 180.00    |
| 26     | 1026     | 227        | 1        | 80.00     | 80.00     |
| 27     | 1027     | 228        | 1        | 250.00    | 250.00    |
| 28     | 1028     | 229        | 1        | 75.00     | 75.00     |
| 29     | 1029     | 230        | 1        | 120.00    | 120.00    |
| 30     | 1030     | 231        | 1        | 60.00     | 60.00     |
| 31     | 1031     | 232        | 1        | 80.00     | 80.00     |
| 32     | 1032     | 233        | 2        | 50.00     | 100.00    |
| 33     | 1033     | 234        | 1        | 120.00    | 120.00    |
| 34     | 1034     | 235        | 1        | 30.00     | 30.00     |
| 35     | 1035     | 236        | 1        | 40.00     | 40.00     |
| 36     | 1036     | 237        | 1        | 60.00     | 60.00     |
| 37     | 1037     | 238        | 1        | 70.00     | 70.00     |
| 38     | 1038     | 239        | 1        | 800.00    | 800.00    |
| 39     | 1039     | 240        | 2        | 150.00    | 300.00    |
| 40     | 1040     | 241        | 1        | 25.00     | 25.00     |
| 41     | 1041     | 242        | 1        | 30.00     | 30.00     |
| 42     | 1042     | 243        | 1        | 500.00    | 500.00    |
| 43     | 1043     | 244        | 1        | 400.00    | 400.00    |
| 44     | 1044     | 245        | 1        | 650.00    | 650.00    |
| 45     | 1045     | 246        | 1        | 130.00    | 130.00    |
| 46     | 1046     | 247        | 1        | 200.00    | 200.00    |
| 47     | 1047     | 248        | 2        | 25.00     | 50.00     |
| 48     | 1048     | 249        | 1        | 35.00     | 35.00     |
| 49     | 1049     | 250        | 1        | 45.00     | 45.00     |
| 50     | 1050     | 201        | 1        | 1200.00   | 1200.00   |
+--------+----------+------------+----------+-----------+-----------+
```

```sql
CREATE TABLE order_items (
    item_id INT NOT NULL AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    unit_price DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    total_amt DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    PRIMARY KEY (item_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
) ENGINE=InnoDB;

INSERT INTO order_items (item_id, order_id, product_id, quantity, unit_price, total_amt) VALUES
(1, 1001, 201, 1, 1200.00, 1200.00),
(2, 1002, 202, 1, 2200.00, 2200.00),
(3, 1003, 203, 1, 800.00, 800.00),
(4, 1004, 204, 1, 600.00, 600.00),
(5, 1005, 205, 1, 999.00, 999.00),
(6, 1006, 206, 1, 1200.00, 1200.00),
(7, 1007, 207, 1, 250.00, 250.00),
(8, 1008, 208, 1, 700.00, 700.00),
(9, 1009, 209, 2, 150.00, 300.00),
(10, 1010, 210, 1, 120.00, 120.00),
(11, 1011, 212, 1, 50.00, 50.00),
(12, 1012, 213, 1, 75.00, 75.00),
(13, 1013, 214, 1, 20.00, 20.00),
(14, 1014, 215, 1, 25.00, 25.00),
(15, 1015, 216, 1, 1200.00, 1200.00),
(16, 1016, 217, 2, 35.00, 70.00),
(17, 1017, 218, 1, 150.00, 150.00),
(18, 1018, 219, 1, 1800.00, 1800.00),
(19, 1019, 220, 1, 550.00, 550.00),
(20, 1020, 221, 1, 1500.00, 1500.00),
(21, 1021, 222, 1, 1100.00, 1100.00),
(22, 1022, 223, 1, 1099.00, 1099.00),
(23, 1023, 224, 1, 200.00, 200.00),
(24, 1024, 225, 1, 1300.00, 1300.00),
(25, 1025, 226, 2, 90.00, 180.00),
(26, 1026, 227, 1, 80.00, 80.00),
(27, 1027, 228, 1, 250.00, 250.00),
(28, 1028, 229, 1, 75.00, 75.00),
(29, 1029, 230, 1, 120.00, 120.00),
(30, 1030, 231, 1, 60.00, 60.00),
(31, 1031, 232, 1, 80.00, 80.00),
(32, 1032, 233, 2, 50.00, 100.00),
(33, 1033, 234, 1, 120.00, 120.00),
(34, 1034, 235, 1, 30.00, 30.00),
(35, 1035, 236, 1, 40.00, 40.00),
(36, 1036, 237, 1, 60.00, 60.00),
(37, 1037, 238, 1, 70.00, 70.00),
(38, 1038, 239, 1, 800.00, 800.00),
(39, 1039, 240, 2, 150.00, 300.00),
(40, 1040, 241, 1, 25.00, 25.00),
(41, 1041, 242, 1, 30.00, 30.00),
(42, 1042, 243, 1, 500.00, 500.00),
(43, 1043, 244, 1, 400.00, 400.00),
(44, 1044, 245, 1, 650.00, 650.00),
(45, 1045, 246, 1, 130.00, 130.00),
(46, 1046, 247, 1, 200.00, 200.00),
(47, 1047, 248, 2, 25.00, 50.00),
(48, 1048, 249, 1, 35.00, 35.00),
(49, 1049, 250, 1, 45.00, 45.00),
(50, 1050, 201, 1, 1200.00, 1200.00);
```