# Sector 3: Library

### Table 1: authors
```
+------------+---------------+------+-----+---------+----------------+
| Field      | Type          | Null | Key | Default | Extra          |
+------------+---------------+------+-----+---------+----------------+
| author_id  | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| first_name | VARCHAR(50)   | NO   |     | NULL    |                |
| last_name  | VARCHAR(50)   | NO   |     | NULL    |                |
| birth_date | DATE          | YES  |     | NULL    |                |
| country    | VARCHAR(50)   | YES  |     | NULL    |                |
+------------+---------------+------+-----+---------+----------------+

+-----------+------------+-----------+------------+-------------+
| author_id | first_name | last_name | birth_date | country     |
+-----------+------------+-----------+------------+-------------+
| 101       | J.K.       | Rowling   | 1965-07-31 | UK          |
| 102       | George     | Orwell    | 1903-06-25 | UK          |
| 103       | Jane       | Austen    | 1775-12-16 | UK          |
| 104       | Mark       | Twain     | 1835-11-30 | USA         |
| 105       | Charles    | Dickens   | 1812-02-07 | UK          |
| 106       | Agatha     | Christie  | 1890-09-15 | UK          |
| 107       | Leo        | Tolstoy   | 1828-09-09 | Russia      |
| 108       | Fyodor     | Dostoevsky| 1821-11-11 | Russia      |
| 109       | Ernest     | Hemingway | 1899-07-21 | USA         |
| 110       | F. Scott   | Fitzgerald| 1896-09-24 | USA         |
| 111       | Virginia   | Woolf     | 1882-01-25 | UK          |
| 112       | William    | Shakespeare| 1564-04-23 | UK         |
| 113       | Homer      |           | NULL       | Greece      |
| 114       | H.G.       | Wells     | 1866-09-21 | UK          |
| 115       | Jules      | Verne     | 1828-02-08 | France      |
| 116       | Harper     | Lee       | 1926-04-28 | USA         |
| 117       | C.S.       | Lewis     | 1898-11-29 | UK          |
| 118       | J.R.R.     | Tolkien   | 1892-01-03 | UK          |
| 119       | Suzanne    | Collins   | 1962-08-10 | USA         |
| 120       | Dan        | Brown     | 1964-06-22 | USA         |
| 121       | Stephen    | King      | 1947-09-21 | USA         |
| 122       | George     | R.R. Martin | 1948-09-20 | USA       |
| 123       | Isaac      | Asimov    | 1920-01-02 | Russia/USA  |
| 124       | Arthur     | Clarke    | 1917-12-16 | UK          |
| 125       | Philip     | Dick      | 1928-12-16 | USA         |
| 126       | Neil       | Gaiman    | 1960-11-10 | UK          |
| 127       | Terry      | Pratchett | 1948-04-28 | UK          |
| 128       | Douglas    | Adams     | 1952-03-11 | UK          |
| 129       | Mary       | Shelley   | 1797-08-30 | UK          |
| 130       | Bram       | Stoker    | 1847-11-08 | Ireland     |
| 131       | Alexandre  | Dumas     | 1802-07-24 | France      |
| 132       | Victor     | Hugo      | 1802-02-26 | France      |
| 133       | Miguel     | Cervantes | 1547-09-29 | Spain       |
| 134       | Dante      | Alighieri | 1265-05-21 | Italy       |
| 135       | Homer      | Simpson   | 1956-05-12 | USA         |
| 136       | Roald      | Dahl      | 1916-09-13 | UK          |
| 137       | Louisa     | May Alcott| 1832-11-29 | USA         |
| 138       | Antoine    | de Saint-Exupéry | 1900-06-29 | France |
| 139       | E.B.       | White     | 1899-07-11 | USA         |
| 140       | L.M.       | Montgomery| 1874-11-30 | Canada      |
| 141       | Beatrix    | Potter    | 1866-07-28 | UK          |
| 142       | H.P.       | Lovecraft | 1890-08-20 | USA         |
| 143       | John       | Steinbeck | 1902-02-27 | USA         |
| 144       | Oscar      | Wilde     | 1854-10-16 | Ireland     |
| 145       | Khaled     | Hosseini | 1965-03-04 | Afghanistan |
| 146       | Paulo      | Coelho    | 1947-08-24 | Brazil      |
| 147       | Gabriel    | Garcia Marquez | 1927-03-06 | Colombia |
| 148       | Haruki     | Murakami  | 1949-01-12 | Japan       |
| 149       | Orhan      | Pamuk     | 1952-06-07 | Turkey      |
| 150       | Chimamanda | Ngozi Adichie | 1977-09-15 | Nigeria  |
+-----------+------------+-----------+------------+-------------+
```

```sql
CREATE TABLE authors (
    author_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE,
    country VARCHAR(50),
    PRIMARY KEY (author_id)
) ENGINE=InnoDB;

INSERT INTO authors (author_id, first_name, last_name, birth_date, country)
VALUES
(101, 'J.K.', 'Rowling', '1965-07-31', 'UK'),
(102, 'George', 'Orwell', '1903-06-25', 'UK'),
(103, 'Jane', 'Austen', '1775-12-16', 'UK'),
(104, 'Mark', 'Twain', '1835-11-30', 'USA'),
(105, 'Charles', 'Dickens', '1812-02-07', 'UK'),
(106, 'Agatha', 'Christie', '1890-09-15', 'UK'),
(107, 'Leo', 'Tolstoy', '1828-09-09', 'Russia'),
(108, 'Fyodor', 'Dostoevsky', '1821-11-11', 'Russia'),
(109, 'Ernest', 'Hemingway', '1899-07-21', 'USA'),
(110, 'F. Scott', 'Fitzgerald', '1896-09-24', 'USA'),
(111, 'Virginia', 'Woolf', '1882-01-25', 'UK'),
(112, 'William', 'Shakespeare', '1564-04-23', 'UK'),
(113, 'Homer', NULL, NULL, 'Greece'),
(114, 'H.G.', 'Wells', '1866-09-21', 'UK'),
(115, 'Jules', 'Verne', '1828-02-08', 'France'),
(116, 'Harper', 'Lee', '1926-04-28', 'USA'),
(117, 'C.S.', 'Lewis', '1898-11-29', 'UK'),
(118, 'J.R.R.', 'Tolkien', '1892-01-03', 'UK'),
(119, 'Suzanne', 'Collins', '1962-08-10', 'USA'),
(120, 'Dan', 'Brown', '1964-06-22', 'USA'),
(121, 'Stephen', 'King', '1947-09-21', 'USA'),
(122, 'George', 'R.R. Martin', '1948-09-20', 'USA'),
(123, 'Isaac', 'Asimov', '1920-01-02', 'Russia/USA'),
(124, 'Arthur', 'Clarke', '1917-12-16', 'UK'),
(125, 'Philip', 'Dick', '1928-12-16', 'USA'),
(126, 'Neil', 'Gaiman', '1960-11-10', 'UK'),
(127, 'Terry', 'Pratchett', '1948-04-28', 'UK'),
(128, 'Douglas', 'Adams', '1952-03-11', 'UK'),
(129, 'Mary', 'Shelley', '1797-08-30', 'UK'),
(130, 'Bram', 'Stoker', '1847-11-08', 'Ireland'),
(131, 'Alexandre', 'Dumas', '1802-07-24', 'France'),
(132, 'Victor', 'Hugo', '1802-02-26', 'France'),
(133, 'Miguel', 'Cervantes', '1547-09-29', 'Spain'),
(134, 'Dante', 'Alighieri', '1265-05-21', 'Italy'),
(135, 'Homer', 'Simpson', '1956-05-12', 'USA'),
(136, 'Roald', 'Dahl', '1916-09-13', 'UK'),
(137, 'Louisa', 'May Alcott', '1832-11-29', 'USA'),
(138, 'Antoine', 'de Saint-Exupéry', '1900-06-29', 'France'),
(139, 'E.B.', 'White', '1899-07-11', 'USA'),
(140, 'L.M.', 'Montgomery', '1874-11-30', 'Canada'),
(141, 'Beatrix', 'Potter', '1866-07-28', 'UK'),
(142, 'H.P.', 'Lovecraft', '1890-08-20', 'USA'),
(143, 'John', 'Steinbeck', '1902-02-27', 'USA'),
(144, 'Oscar', 'Wilde', '1854-10-16', 'Ireland'),
(145, 'Khaled', 'Hosseini', '1965-03-04', 'Afghanistan'),
(146, 'Paulo', 'Coelho', '1947-08-24', 'Brazil'),
(147, 'Gabriel', 'Garcia Marquez', '1927-03-06', 'Colombia'),
(148, 'Haruki', 'Murakami', '1949-01-12', 'Japan'),
(149, 'Orhan', 'Pamuk', '1952-06-07', 'Turkey'),
(150, 'Chimamanda', 'Ngozi Adichie', '1977-09-15', 'Nigeria');
```

### Table 2: genres
```
+-----------+---------------+------+-----+---------+-------+
| Field     | Type          | Null | Key | Default | Extra |
+-----------+---------------+------+-----+---------+-------+
| genre_id  | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| genre_name| VARCHAR(50)   | NO   |     | NULL    |                |
+-----------+---------------+------+-----+---------+-------+

+---------+---------------------+
| genre_id| genre_name          |
+---------+---------------------+
| 201     | Fiction             |
| 202     | Non-Fiction         |
| 203     | Mystery             |
| 204     | Science Fiction     |
| 205     | Fantasy             |
| 206     | Romance             |
| 207     | Thriller            |
| 208     | Horror              |
| 209     | Biography           |
| 210     | History             |
| 211     | Self-Help           |
| 212     | Poetry              |
| 213     | Adventure           |
| 214     | Graphic Novel       |
| 215     | Classic Literature  |
| 216     | Young Adult         |
| 217     | Children            |
| 218     | Philosophy          |
| 219     | Science             |
| 220     | Travel              |
| 221     | Religion            |
| 222     | Art                 |
| 223     | Cookbooks           |
| 224     | Education           |
| 225     | Drama               |
+---------+---------------------+
```

```sql
CREATE TABLE genres (
    genre_id INT NOT NULL AUTO_INCREMENT,
    genre_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (genre_id)
) ENGINE=InnoDB;

INSERT INTO genres (genre_id, genre_name) VALUES
(201, 'Fiction'),
(202, 'Non-Fiction'),
(203, 'Mystery'),
(204, 'Science Fiction'),
(205, 'Fantasy'),
(206, 'Romance'),
(207, 'Thriller'),
(208, 'Horror'),
(209, 'Biography'),
(210, 'History'),
(211, 'Self-Help'),
(212, 'Poetry'),
(213, 'Adventure'),
(214, 'Graphic Novel'),
(215, 'Classic Literature'),
(216, 'Young Adult'),
(217, 'Children'),
(218, 'Philosophy'),
(219, 'Science'),
(220, 'Travel'),
(221, 'Religion'),
(222, 'Art'),
(223, 'Cookbooks'),
(224, 'Education'),
(225, 'Drama');
```

### Table 3: books
```
+----------------+---------------+------+-----+---------+----------------+
| Field          | Type          | Null | Key | Default | Extra          |
+----------------+---------------+------+-----+---------+----------------+
| book_id        | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| title          | VARCHAR(100)  | NO   |     | NULL    |                |
| author_id      | INT           | NO   | MUL | NULL    |                |
| genre_id       | INT           | NO   | MUL | NULL    |                |
| published_date | DATE          | YES  |     | NULL    |                |
| isbn           | VARCHAR(20)   | YES  |     | NULL    |                |
| copies_total   | INT           | NO   |     | 1       |                |
| copies_available| INT          | NO   |     | 1       |                |
+----------------+---------------+------+-----+---------+----------------+

+---------+----------------------------+-----------+---------+---------------+-------------+-------------+------------------+
| book_id | title                      | author_id | genre_id| published_date| isbn        | copies_total| copies_available |
+---------+----------------------------+-----------+---------+---------------+-------------+-------------+------------------+
| 301     | Harry Potter 1             | 101       | 205     | 1997-06-26    | 9780747532699| 10         | 10               |
| 302     | 1984                       | 102       | 204     | 1949-06-08    | 9780451524935| 8          | 8                |
| 303     | Pride and Prejudice        | 103       | 215     | 1813-01-28    | 9780141439518| 5          | 5                |
| 304     | Adventures of Huckleberry Finn | 104    | 213     | 1884-12-10    | 9780486280615| 6          | 6                |
| 305     | Great Expectations         | 105       | 215     | 1861-08-01    | 9780141439563| 7          | 7                |
| 306     | Murder on the Orient Express| 106      | 203     | 1934-01-01    | 9780062693662| 5          | 5                |
| 307     | War and Peace              | 107       | 215     | 1869-01-01    | 9780199232765| 6          | 6                |
| 308     | Crime and Punishment       | 108       | 215     | 1866-01-01    | 9780143058144| 4          | 4                |
| 309     | The Old Man and the Sea    | 109       | 201     | 1952-09-01    | 9780684801223| 6          | 6                |
| 310     | The Great Gatsby           | 110       | 201     | 1925-04-10    | 9780743273565| 7          | 7                |
| 311     | To the Lighthouse          | 111       | 201     | 1927-05-05    | 9780156907392| 5          | 5                |
| 312     | Hamlet                     | 112       | 215     | 1603-01-01    | 9780141396507| 6          | 6                |
| 313     | The Time Machine           | 114       | 204     | 1895-05-07    | 9780553213515| 4          | 4                |
| 314     | Journey to the Center of the Earth | 115 | 204   | 1864-11-25    | 9780486440880| 5          | 5                |
| 315     | To Kill a Mockingbird      | 116       | 201     | 1960-07-11    | 9780061120084| 7          | 7                |
| 316     | The Chronicles of Narnia   | 117       | 205     | 1950-10-16    | 9780064471190| 6          | 6                |
| 317     | The Hobbit                 | 118       | 205     | 1937-09-21    | 9780547928227| 8          | 8                |
| 318     | The Hunger Games           | 119       | 216     | 2008-09-14    | 9780439023481| 10         | 10               |
| 319     | The Da Vinci Code          | 120       | 207     | 2003-03-18    | 9780307474278| 9          | 9                |
| 320     | It                         | 121       | 208     | 1986-09-15    | 9780450411434| 8          | 8                |
| 321     | A Game of Thrones          | 122       | 204     | 1996-08-06    | 9780553103540| 10         | 10               |
| 322     | Foundation                 | 123       | 204     | 1951-06-01    | 9780553293357| 6          | 6                |
| 323     | 2001: A Space Odyssey      | 124       | 204     | 1968-07-01    | 9780451457998| 5          | 5                |
| 324     | Do Androids Dream of Electric Sheep | 125 | 204  | 1968-01-01    | 9780345404473| 5          | 5                |
| 325     | American Gods              | 126       | 205     | 2001-06-19    | 9780062572233| 6          | 6                |
| 326     | Good Omens                 | 127       | 205     | 1990-05-01    | 9780060853983| 5          | 5                |
| 327     | Hitchhiker's Guide to the Galaxy | 128 | 205     | 1979-10-12    | 9780345391803| 6          | 6                |
| 328     | Frankenstein               | 129       | 208     | 1818-01-01    | 9780141439471| 4          | 4                |
| 329     | Dracula                    | 130       | 208     | 1897-05-26    | 9780141439846| 5          | 5                |
| 330     | The Count of Monte Cristo  | 131       | 215     | 1844-08-28    | 9780140449266| 6          | 6                |
| 331     | Les Misérables             | 132       | 215     | 1862-01-01    | 9780451419439| 7          | 7                |
| 332     | Don Quixote                | 133       | 215     | 1605-01-16    | 9780060934347| 5          | 5                |
| 333     | The Divine Comedy          | 134       | 215     | 1320-01-01    | 9780142437223| 4          | 4                |
| 334     | Charlie and the Chocolate Factory | 136 | 216     | 1964-01-01    | 9780142410318| 6          | 6                |
| 335     | Little Women               | 137       | 215     | 1868-09-30    | 9780147514011| 5          | 5                |
| 336     | The Little Prince          | 138       | 216     | 1943-04-06    | 9780156012195| 6          | 6                |
| 337     | Charlotte's Web            | 139       | 216     | 1952-10-15    | 9780064400558| 7          | 7                |
| 338     | Anne of Green Gables       | 140       | 216     | 1908-06-01    | 9780553213136| 6          | 6                |
| 339     | The Tale of Peter Rabbit   | 141       | 217     | 1902-10-01    | 9780723247703| 8          | 8                |
| 340     | The Call of Cthulhu        | 142       | 208     | 1928-02-01    | 9780486262114| 5          | 5                |
| 341     | Of Mice and Men            | 143       | 215     | 1937-02-06    | 9780140177398| 6          | 6                |
| 342     | The Picture of Dorian Gray | 144       | 215     | 1890-06-20    | 9780141439570| 5          | 5                |
| 343     | The Kite Runner            | 145       | 201     | 2003-05-29    | 9781594631931| 6          | 6                |
| 344     | The Alchemist              | 146       | 201     | 1988-04-01    | 9780061122415| 7          | 7                |
| 345     | One Hundred Years of Solitude | 147    | 201     | 1967-05-30    | 9780060883287| 6          | 6                |
| 346     | Norwegian Wood             | 148       | 201     | 1987-09-04    | 9780375704024| 6          | 6                |
| 347     | My Name Is Red             | 149       | 201     | 1998-05-01    | 9780375722433| 5          | 5                |
| 348     | Half of a Yellow Sun       | 150       | 201     | 2006-09-01    | 9780345804303| 6          | 6                |
+---------+----------------------------+-----------+---------+---------------+-------------+-------------+------------------+
```

```sql
CREATE TABLE books (
    book_id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    author_id INT NOT NULL,
    genre_id INT NOT NULL,
    published_date DATE,
    isbn VARCHAR(20),
    copies_total INT NOT NULL DEFAULT 1,
    copies_available INT NOT NULL DEFAULT 1,
    PRIMARY KEY (book_id),
    FOREIGN KEY (author_id) REFERENCES authors(author_id),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
) ENGINE=InnoDB;

INSERT INTO books (book_id, title, author_id, genre_id, published_date, isbn, copies_total, copies_available)VALUES
(301, 'Harry Potter 1', 101, 205, '1997-06-26', '9780747532699', 10, 10),
(302, '1984', 102, 204, '1949-06-08', '9780451524935', 8, 8),
(303, 'Pride and Prejudice', 103, 215, '1813-01-28', '9780141439518', 5, 5),
(304, 'Adventures of Huckleberry Finn', 104, 213, '1884-12-10', '9780486280615', 6, 6),
(305, 'Great Expectations', 105, 215, '1861-08-01', '9780141439563', 7, 7),
(306, 'Murder on the Orient Express', 106, 203, '1934-01-01', '9780062693662', 5, 5),
(307, 'War and Peace', 107, 215, '1869-01-01', '9780199232765', 6, 6),
(308, 'Crime and Punishment', 108, 215, '1866-01-01', '9780143058144', 4, 4),
(309, 'The Old Man and the Sea', 109, 201, '1952-09-01', '9780684801223', 6, 6),
(310, 'The Great Gatsby', 110, 201, '1925-04-10', '9780743273565', 7, 7),
(311, 'To the Lighthouse', 111, 201, '1927-05-05', '9780156907392', 5, 5),
(312, 'Hamlet', 112, 215, '1603-01-01', '9780141396507', 6, 6),
(313, 'The Time Machine', 114, 204, '1895-05-07', '9780553213515', 4, 4),
(314, 'Journey to the Center of the Earth', 115, 204, '1864-11-25', '9780486440880', 5, 5),
(315, 'To Kill a Mockingbird', 116, 201, '1960-07-11', '9780061120084', 7, 7),
(316, 'The Chronicles of Narnia', 117, 205, '1950-10-16', '9780064471190', 6, 6),
(317, 'The Hobbit', 118, 205, '1937-09-21', '9780547928227', 8, 8),
(318, 'The Hunger Games', 119, 216, '2008-09-14', '9780439023481', 10, 10),
(319, 'The Da Vinci Code', 120, 207, '2003-03-18', '9780307474278', 9, 9),
(320, 'It', 121, 208, '1986-09-15', '9780450411434', 8, 8),
(321, 'A Game of Thrones', 122, 204, '1996-08-06', '9780553103540', 10, 10),
(322, 'Foundation', 123, 204, '1951-06-01', '9780553293357', 6, 6),
(323, '2001: A Space Odyssey', 124, 204, '1968-07-01', '9780451457998', 5, 5),
(324, 'Do Androids Dream of Electric Sheep', 125, 204, '1968-01-01', '9780345404473', 5, 5),
(325, 'American Gods', 126, 205, '2001-06-19', '9780062572233', 6, 6),
(326, 'Good Omens', 127, 205, '1990-05-01', '9780060853983', 5, 5),
(327, 'Hitchhiker''s Guide to the Galaxy', 128, 205, '1979-10-12', '9780345391803', 6, 6),
(328, 'Frankenstein', 129, 208, '1818-01-01', '9780141439471', 4, 4),
(329, 'Dracula', 130, 208, '1897-05-26', '9780141439846', 5, 5),
(330, 'The Count of Monte Cristo', 131, 215, '1844-08-28', '9780140449266', 6, 6),
(331, 'Les Misérables', 132, 215, '1862-01-01', '9780451419439', 7, 7),
(332, 'Don Quixote', 133, 215, '1605-01-16', '9780060934347', 5, 5),
(333, 'The Divine Comedy', 134, 215, '1320-01-01', '9780142437223', 4, 4),
(334, 'Charlie and the Chocolate Factory', 136, 216, '1964-01-01', '9780142410318', 6, 6),
(335, 'Little Women', 137, 215, '1868-09-30', '9780147514011', 5, 5),
(336, 'The Little Prince', 138, 216, '1943-04-06', '9780156012195', 6, 6),
(337, 'Charlotte''s Web', 139, 216, '1952-10-15', '9780064400558', 7, 7),
(338, 'Anne of Green Gables', 140, 216, '1908-06-01', '9780553213136', 6, 6),
(339, 'The Tale of Peter Rabbit', 141, 217, '1902-10-01', '9780723247703', 8, 8),
(340, 'The Call of Cthulhu', 142, 208, '1928-02-01', '9780486262114', 5, 5),
(341, 'Of Mice and Men', 143, 215, '1937-02-06', '9780140177398', 6, 6),
(342, 'The Picture of Dorian Gray', 144, 215, '1890-06-20', '9780141439570', 5, 5),
(343, 'The Kite Runner', 145, 201, '2003-05-29', '9781594631931', 6, 6),
(344, 'The Alchemist', 146, 201, '1988-04-01', '9780061122415', 7, 7),
(345, 'One Hundred Years of Solitude', 147, 201, '1967-05-30', '9780060883287', 6, 6),
(346, 'Norwegian Wood', 148, 201, '1987-09-04', '9780375704024', 6, 6),
(347, 'My Name Is Red', 149, 201, '1998-05-01', '9780375722433', 5, 5),
(348, 'Half of a Yellow Sun', 150, 201, '2006-09-01', '9780345804303', 6, 6);
```

### Table 4: members
```
+------------+---------------+------+-----+---------+-------+
| Field      | Type          | Null | Key | Default | Extra |
+------------+---------------+------+-----+---------+-------+
| member_id  | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| first_name | VARCHAR(50)   | NO   |     | NULL    |                |
| last_name  | VARCHAR(50)   | NO   |     | NULL    |                |
| join_date  | DATE          | NO   |     | NULL    |                |
| email      | VARCHAR(100)  | NO   | UNI | NULL    |                |
| phone      | VARCHAR(15)   | YES  |     | NULL    |                |
+------------+---------------+------+-----+---------+-------+

+-----------+------------+-----------+------------+-------------------------+-------------+
| member_id | first_name | last_name | join_date  | email                   | phone       |
+-----------+------------+-----------+------------+-------------------------+-------------+
| 401       | Alice      | Smith     | 2023-01-10 | alice.smith@example.com | 9876543210  |
| 402       | Bob        | Johnson   | 2023-01-15 | bob.johnson@example.com | 9876543211  |
| 403       | Charlie    | Brown     | 2023-02-01 | charlie.brown@example.com | 9876543212|
| 404       | David      | Wilson    | 2023-02-05 | david.wilson@example.com | 9876543213|
| 405       | Emma       | Taylor    | 2023-02-10 | emma.taylor@example.com  | 9876543214|
| 406       | Frank      | Anderson  | 2023-02-12 | frank.anderson@example.com | 9876543215|
| 407       | Grace      | Thomas    | 2023-03-01 | grace.thomas@example.com  | 9876543216|
| 408       | Henry      | Jackson   | 2023-03-05 | henry.jackson@example.com | 9876543217|
| 409       | Isabella   | White     | 2023-03-10 | isabella.white@example.com | 9876543218|
| 410       | Jack       | Harris    | 2023-03-12 | jack.harris@example.com | 9876543219|
| 411       | Karen      | Martin    | 2023-03-15 | karen.martin@example.com | 9876543220|
| 412       | Liam       | Thompson  | 2023-03-20 | liam.thompson@example.com | 9876543221|
| 413       | Mia        | Garcia    | 2023-03-25 | mia.garcia@example.com | 9876543222|
| 414       | Noah       | Martinez  | 2023-03-28 | noah.martinez@example.com | 9876543223|
| 415       | Olivia     | Robinson  | 2023-04-01 | olivia.robinson@example.com | 9876543224|
| 416       | Paul       | Clark     | 2023-04-05 | paul.clark@example.com | 9876543225|
| 417       | Quinn      | Rodriguez | 2023-04-10 | quinn.rodriguez@example.com | 9876543226|
| 418       | Rachel     | Lewis     | 2023-04-15 | rachel.lewis@example.com | 9876543227|
| 419       | Samuel     | Lee       | 2023-04-20 | samuel.lee@example.com | 9876543228|
| 420       | Tina       | Walker    | 2023-04-25 | tina.walker@example.com | 9876543229|
| 421       | Ursula     | Hall      | 2023-05-01 | ursula.hall@example.com | 9876543230|
| 422       | Victor     | Allen     | 2023-05-05 | victor.allen@example.com | 9876543231|
| 423       | Wendy      | Young     | 2023-05-10 | wendy.young@example.com | 9876543232|
| 424       | Xavier     | Hernandez | 2023-05-15 | xavier.hernandez@example.com | 9876543233|
| 425       | Yvonne     | King      | 2023-05-20 | yvonne.king@example.com | 9876543234|
| 426       | Zachary    | Wright    | 2023-05-25 | zachary.wright@example.com | 9876543235|
| 427       | Abigail    | Lopez     | 2023-06-01 | abigail.lopez@example.com | 9876543236|
| 428       | Brandon    | Hill      | 2023-06-05 | brandon.hill@example.com | 9876543237|
| 429       | Chloe      | Scott     | 2023-06-10 | chloe.scott@example.com | 9876543238|
| 430       | Daniel     | Green     | 2023-06-15 | daniel.green@example.com | 9876543239|
| 431       | Ella       | Adams     | 2023-06-20 | ella.adams@example.com | 9876543240|
| 432       | Felix      | Baker     | 2023-06-25 | felix.baker@example.com | 9876543241|
| 433       | Gabriella  | Nelson    | 2023-07-01 | gabriella.nelson@example.com | 9876543242|
| 434       | Harrison   | Carter    | 2023-07-05 | harrison.carter@example.com | 9876543243|
| 435       | Isabelle   | Mitchell  | 2023-07-10 | isabelle.mitchell@example.com | 9876543244|
| 436       | Jason      | Perez     | 2023-07-15 | jason.perez@example.com | 9876543245|
| 437       | Kaitlyn    | Roberts   | 2023-07-20 | kaitlyn.roberts@example.com | 9876543246|
| 438       | Leo        | Turner    | 2023-07-25 | leo.turner@example.com | 9876543247|
| 439       | Madison    | Phillips  | 2023-08-01 | madison.phillips@example.com | 9876543248|
| 440       | Nathan     | Campbell  | 2023-08-05 | nathan.campbell@example.com | 9876543249|
| 441       | Olivia     | Parker    | 2023-08-10 | olivia.parker@example.com | 9876543250|
| 442       | Patrick    | Evans     | 2023-08-15 | patrick.evans@example.com | 9876543251|
| 443       | Quinn      | Edwards   | 2023-08-20 | quinn.edwards@example.com | 9876543252|
| 444       | Riley      | Collins   | 2023-08-25 | riley.collins@example.com | 9876543253|
| 445       | Sophia     | Stewart   | 2023-09-01 | sophia.stewart@example.com | 9876543254|
| 446       | Thomas     | Sanchez   | 2023-09-05 | thomas.sanchez@example.com | 9876543255|
| 447       | Uma        | Morris    | 2023-09-10 | uma.morris@example.com | 9876543256|
| 448       | Vincent    | Rogers    | 2023-09-15 | vincent.rogers@example.com | 9876543257|
| 449       | Willow     | Reed      | 2023-09-20 | willow.reed@example.com | 9876543258|
| 450       | Xavier     | Cook      | 2023-09-25 | xavier.cook@example.com | 9876543259|
+-----------+------------+-----------+------------+-------------------------+-------------+
```

```sql
CREATE TABLE members (
    member_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    join_date DATE NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15),
    PRIMARY KEY (member_id)
) ENGINE=InnoDB;

INSERT INTO members (member_id, first_name, last_name, join_date, email, phone) VALUES
(401, 'Alice', 'Smith', '2023-01-10', 'alice.smith@example.com', '9876543210'),
(402, 'Bob', 'Johnson', '2023-01-15', 'bob.johnson@example.com', '9876543211'),
(403, 'Charlie', 'Brown', '2023-02-01', 'charlie.brown@example.com', '9876543212'),
(404, 'David', 'Wilson', '2023-02-05', 'david.wilson@example.com', '9876543213'),
(405, 'Emma', 'Taylor', '2023-02-10', 'emma.taylor@example.com', '9876543214'),
(406, 'Frank', 'Anderson', '2023-02-12', 'frank.anderson@example.com', '9876543215'),
(407, 'Grace', 'Thomas', '2023-03-01', 'grace.thomas@example.com', '9876543216'),
(408, 'Henry', 'Jackson', '2023-03-05', 'henry.jackson@example.com', '9876543217'),
(409, 'Isabella', 'White', '2023-03-10', 'isabella.white@example.com', '9876543218'),
(410, 'Jack', 'Harris', '2023-03-12', 'jack.harris@example.com', '9876543219'),
(411, 'Karen', 'Martin', '2023-03-15', 'karen.martin@example.com', '9876543220'),
(412, 'Liam', 'Thompson', '2023-03-20', 'liam.thompson@example.com', '9876543221'),
(413, 'Mia', 'Garcia', '2023-03-25', 'mia.garcia@example.com', '9876543222'),
(414, 'Noah', 'Martinez', '2023-03-28', 'noah.martinez@example.com', '9876543223'),
(415, 'Olivia', 'Robinson', '2023-04-01', 'olivia.robinson@example.com', '9876543224'),
(416, 'Paul', 'Clark', '2023-04-05', 'paul.clark@example.com', '9876543225'),
(417, 'Quinn', 'Rodriguez', '2023-04-10', 'quinn.rodriguez@example.com', '9876543226'),
(418, 'Rachel', 'Lewis', '2023-04-15', 'rachel.lewis@example.com', '9876543227'),
(419, 'Samuel', 'Lee', '2023-04-20', 'samuel.lee@example.com', '9876543228'),
(420, 'Tina', 'Walker', '2023-04-25', 'tina.walker@example.com', '9876543229'),
(421, 'Ursula', 'Hall', '2023-05-01', 'ursula.hall@example.com', '9876543230'),
(422, 'Victor', 'Allen', '2023-05-05', 'victor.allen@example.com', '9876543231'),
(423, 'Wendy', 'Young', '2023-05-10', 'wendy.young@example.com', '9876543232'),
(424, 'Xavier', 'Hernandez', '2023-05-15', 'xavier.hernandez@example.com', '9876543233'),
(425, 'Yvonne', 'King', '2023-05-20', 'yvonne.king@example.com', '9876543234'),
(426, 'Zachary', 'Wright', '2023-05-25', 'zachary.wright@example.com', '9876543235'),
(427, 'Abigail', 'Lopez', '2023-06-01', 'abigail.lopez@example.com', '9876543236'),
(428, 'Brandon', 'Hill', '2023-06-05', 'brandon.hill@example.com', '9876543237'),
(429, 'Chloe', 'Scott', '2023-06-10', 'chloe.scott@example.com', '9876543238'),
(430, 'Daniel', 'Green', '2023-06-15', 'daniel.green@example.com', '9876543239'),
(431, 'Ella', 'Adams', '2023-06-20', 'ella.adams@example.com', '9876543240'),
(432, 'Felix', 'Baker', '2023-06-25', 'felix.baker@example.com', '9876543241'),
(433, 'Gabriella', 'Nelson', '2023-07-01', 'gabriella.nelson@example.com', '9876543242'),
(434, 'Harrison', 'Carter', '2023-07-05', 'harrison.carter@example.com', '9876543243'),
(435, 'Isabelle', 'Mitchell', '2023-07-10', 'isabelle.mitchell@example.com', '9876543244'),
(436, 'Jason', 'Perez', '2023-07-15', 'jason.perez@example.com', '9876543245'),
(437, 'Kaitlyn', 'Roberts', '2023-07-20', 'kaitlyn.roberts@example.com', '9876543246'),
(438, 'Leo', 'Turner', '2023-07-25', 'leo.turner@example.com', '9876543247'),
(439, 'Madison', 'Phillips', '2023-08-01', 'madison.phillips@example.com', '9876543248'),
(440, 'Nathan', 'Campbell', '2023-08-05', 'nathan.campbell@example.com', '9876543249'),
(441, 'Olivia', 'Parker', '2023-08-10', 'olivia.parker@example.com', '9876543250'),
(442, 'Patrick', 'Evans', '2023-08-15', 'patrick.evans@example.com', '9876543251'),
(443, 'Quinn', 'Edwards', '2023-08-20', 'quinn.edwards@example.com', '9876543252'),
(444, 'Riley', 'Collins', '2023-08-25', 'riley.collins@example.com', '9876543253'),
(445, 'Sophia', 'Stewart', '2023-09-01', 'sophia.stewart@example.com', '9876543254'),
(446, 'Thomas', 'Sanchez', '2023-09-05', 'thomas.sanchez@example.com', '9876543255'),
(447, 'Uma', 'Morris', '2023-09-10', 'uma.morris@example.com', '9876543256'),
(448, 'Vincent', 'Rogers', '2023-09-15', 'vincent.rogers@example.com', '9876543257'),
(449, 'Willow', 'Reed', '2023-09-20', 'willow.reed@example.com', '9876543258'),
(450, 'Xavier', 'Cook', '2023-09-25', 'xavier.cook@example.com', '9876543259');
```

### Table 5: loans
```
+------------+---------------+------+-----+---------+----------------+
| Field      | Type          | Null | Key | Default | Extra          |
+------------+---------------+------+-----+---------+----------------+
| loan_id    | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| member_id  | INT           | NO   | MUL | NULL    |                |
| book_id    | INT           | NO   | MUL | NULL    |                |
| loan_date  | DATE          | NO   |     | NULL    |                |
| due_date   | DATE          | NO   |     | NULL    |                |
| return_date| DATE          | YES  |     | NULL    |                |
| fine_amount| DECIMAL(6,2) | YES  |     | 0.00    |                |
+------------+---------------+------+-----+---------+----------------+

+---------+-----------+---------+------------+------------+------------+------------+
| loan_id | member_id | book_id | loan_date  | due_date   | return_date| fine_amount|
+---------+-----------+---------+------------+------------+------------+------------+
| 501     | 401       | 301     | 2023-06-01 | 2023-06-15 | 2023-06-16 | 1.00       |
| 502     | 402       | 302     | 2023-06-02 | 2023-06-16 | 2023-06-18 | 2.00       |
| 503     | 403       | 303     | 2023-06-03 | 2023-06-17 | 2023-06-14 | 0.00       |
| 504     | 404       | 304     | 2023-06-04 | 2023-06-18 | 2023-06-15 | 0.00       |
| 505     | 405       | 305     | 2023-06-05 | 2023-06-19 | NULL       | 0.00       |
| 506     | 406       | 306     | 2023-06-06 | 2023-06-20 | 2023-06-18 | 0.00       |
| 507     | 407       | 307     | 2023-06-07 | 2023-06-21 | 2023-06-20 | 0.00       |
| 508     | 408       | 308     | 2023-06-08 | 2023-06-22 | 2023-06-19 | 0.00       |
| 509     | 409       | 309     | 2023-06-09 | 2023-06-23 | 2023-06-25 | 2.00       |
| 510     | 410       | 310     | 2023-06-10 | 2023-06-24 | 2023-06-28 | 4.00       |
| 511     | 411       | 311     | 2023-06-11 | 2023-06-25 | 2023-06-22 | 0.00       |
| 512     | 412       | 312     | 2023-06-12 | 2023-06-26 | 2023-06-25 | 0.00       |
| 513     | 413       | 313     | 2023-06-13 | 2023-06-27 | 2023-06-29 | 2.00       |
| 514     | 414       | 314     | 2023-06-14 | 2023-06-28 | 2023-07-01 | 3.00       |
| 515     | 415       | 315     | 2023-06-15 | 2023-06-29 | 2023-06-28 | 0.00       |
| 516     | 416       | 316     | 2023-06-16 | 2023-06-30 | NULL       | 0.00       |
| 517     | 417       | 317     | 2023-06-17 | 2023-07-01 | 2023-07-01 | 0.00       |
| 518     | 418       | 318     | 2023-06-18 | 2023-07-02 | 2023-07-01 | 0.00       |
| 519     | 419       | 319     | 2023-06-19 | 2023-07-03 | 2023-07-03 | 0.00       |
| 520     | 420       | 320     | 2023-06-20 | 2023-07-04 | 2023-07-04 | 0.00       |
| 521     | 421       | 321     | 2023-06-21 | 2023-07-05 | 2023-07-04 | 0.00       |
| 522     | 422       | 322     | 2023-06-22 | 2023-07-06 | 2023-07-07 | 1.00       |
| 523     | 423       | 323     | 2023-06-23 | 2023-07-07 | NULL       | 0.00       |
| 524     | 424       | 324     | 2023-06-24 | 2023-07-08 | 2023-07-08 | 0.00       |
| 525     | 425       | 325     | 2023-06-25 | 2023-07-09 | 2023-07-09 | 0.00       |
| 526     | 426       | 326     | 2023-06-26 | 2023-07-10 | NULL       | 0.00       |
| 527     | 427       | 327     | 2023-06-27 | 2023-07-11 | 2023-07-14 | 3.00       |
| 528     | 428       | 328     | 2023-06-28 | 2023-07-12 | 2023-07-12 | 0.00       |
| 529     | 429       | 329     | 2023-06-29 | 2023-07-13 | 2023-07-14 | 1.00       |
| 530     | 430       | 330     | 2023-06-30 | 2023-07-14 | 2023-07-17 | 3.00       |
| 531     | 431       | 331     | 2023-07-01 | 2023-07-15 | NULL       | 0.00       |
| 532     | 432       | 332     | 2023-07-02 | 2023-07-16 | NULL       | 0.00       |
| 533     | 433       | 333     | 2023-07-03 | 2023-07-17 | NULL       | 0.00       |
| 534     | 434       | 334     | 2023-07-04 | 2023-07-18 | 2023-07-18 | 0.00       |
| 535     | 435       | 335     | 2023-07-05 | 2023-07-19 | 2023-07-19 | 0.00       |
| 536     | 436       | 336     | 2023-07-06 | 2023-07-20 | NULL       | 0.00       |
| 537     | 437       | 337     | 2023-07-07 | 2023-07-21 | 2023-07-19 | 0.00       |
| 538     | 438       | 338     | 2023-07-08 | 2023-07-22 | 2023-07-20 | 0.00       |
| 539     | 439       | 339     | 2023-07-09 | 2023-07-23 | 2023-07-24 | 1.00       |
| 540     | 440       | 340     | 2023-07-10 | 2023-07-24 | 2023-07-26 | 2.00       |
| 541     | 441       | 341     | 2023-07-11 | 2023-07-25 | 2023-07-25 | 0.00       |
| 542     | 442       | 342     | 2023-07-12 | 2023-07-26 | 2023-07-24 | 0.00       |
| 543     | 443       | 343     | 2023-07-13 | 2023-07-27 | 2023-07-27 | 0.00       |
| 544     | 444       | 344     | 2023-07-14 | 2023-07-28 | NULL       | 0.00       |
| 545     | 445       | 345     | 2023-07-15 | 2023-07-29 | 2023-07-31 | 2.00       |
| 546     | 446       | 346     | 2023-07-16 | 2023-07-30 | 2023-07-31 | 1.00       |
| 547     | 447       | 347     | 2023-07-17 | 2023-07-31 | 2023-07-30 | 0.00       |
| 548     | 448       | 348     | 2023-07-18 | 2023-08-01 | NULL       | 0.00       |
| 549     | 449       | 301     | 2023-07-19 | 2023-08-02 | 2023-08-02 | 0.00       |
| 550     | 450       | 302     | 2023-07-20 | 2023-08-03 | 2023-07-31 | 0.00       |
| 551     | 401       | 303     | 2023-07-21 | 2023-08-04 | NULL       | 0.00       |
| 552     | 402       | 304     | 2023-07-22 | 2023-08-05 | 2023-08-05 | 0.00       |
| 553     | 403       | 305     | 2023-07-23 | 2023-08-06 | 2023-08-10 | 4.00       |
| 554     | 404       | 306     | 2023-07-24 | 2023-08-07 | NULL       | 0.00       |
| 555     | 405       | 307     | 2023-07-25 | 2023-08-08 | 2023-08-10 | 2.00       |
| 556     | 406       | 308     | 2023-07-26 | 2023-08-09 | 2023-08-08 | 0.00       |
| 557     | 407       | 309     | 2023-07-27 | 2023-08-10 | 2023-08-13 | 3.00       |
| 558     | 408       | 310     | 2023-07-28 | 2023-08-11 | 2023-08-15 | 4.00       |
| 559     | 409       | 311     | 2023-07-29 | 2023-08-12 | NULL       | 0.00       |
| 560     | 410       | 312     | 2023-07-30 | 2023-08-13 | 2023-08-13 | 0.00       |
| 561     | 411       | 313     | 2023-07-31 | 2023-08-14 | 2023-08-13 | 0.00       |
| 562     | 412       | 314     | 2023-08-01 | 2023-08-15 | 2023-08-15 | 0.00       |
| 563     | 413       | 315     | 2023-08-02 | 2023-08-16 | 2023-08-15 | 0.00       |
| 564     | 414       | 316     | 2023-08-03 | 2023-08-17 | NULL       | 0.00       |
| 565     | 415       | 317     | 2023-08-04 | 2023-08-18 | 2023-08-17 | 0.00       |
| 566     | 416       | 318     | 2023-08-05 | 2023-08-19 | 2023-08-23 | 4.00       |
| 567     | 417       | 319     | 2023-08-06 | 2023-08-20 | 2023-08-20 | 0.00       |
| 568     | 418       | 320     | 2023-08-07 | 2023-08-21 | 2023-08-21 | 0.00       |
| 569     | 419       | 321     | 2023-08-08 | 2023-08-22 | 2023-08-22 | 0.00       |
| 570     | 420       | 322     | 2023-08-09 | 2023-08-23 | 2023-08-23 | 0.00       |
| 571     | 421       | 323     | 2023-08-10 | 2023-08-24 | 2023-08-21 | 0.00       |
| 572     | 422       | 324     | 2023-08-11 | 2023-08-25 | NULL       | 0.00       |
| 573     | 423       | 325     | 2023-08-12 | 2023-08-26 | 2023-08-23 | 0.00       |
| 574     | 424       | 326     | 2023-08-13 | 2023-08-27 | 2023-08-24 | 0.00       |
| 575     | 425       | 327     | 2023-08-14 | 2023-08-28 | 2023-08-31 | 3.00       |
| 576     | 426       | 328     | 2023-08-15 | 2023-08-29 | 2023-08-27 | 0.00       |
| 577     | 427       | 329     | 2023-08-16 | 2023-08-30 | 2023-08-29 | 0.00       |
| 578     | 428       | 330     | 2023-08-17 | 2023-08-31 | NULL       | 0.00       |
| 579     | 429       | 331     | 2023-08-18 | 2023-09-01 | NULL       | 0.00       |
| 580     | 430       | 332     | 2023-08-19 | 2023-09-02 | 2023-08-30 | 0.00       |
| 581     | 431       | 333     | 2023-08-20 | 2023-09-03 | 2023-09-04 | 1.00       |
| 582     | 432       | 334     | 2023-08-21 | 2023-09-04 | NULL       | 0.00       |
| 583     | 433       | 335     | 2023-08-22 | 2023-09-05 | 2023-09-02 | 0.00       |
| 584     | 434       | 336     | 2023-08-23 | 2023-09-06 | 2023-09-06 | 0.00       |
| 585     | 435       | 337     | 2023-08-24 | 2023-09-07 | 2023-09-05 | 0.00       |
| 586     | 436       | 338     | 2023-08-25 | 2023-09-08 | 2023-09-09 | 1.00       |
| 587     | 437       | 339     | 2023-08-26 | 2023-09-09 | 2023-09-09 | 0.00       |
| 588     | 438       | 340     | 2023-08-27 | 2023-09-10 | 2023-09-10 | 0.00       |
| 589     | 439       | 341     | 2023-08-28 | 2023-09-11 | 2023-09-09 | 0.00       |
| 590     | 440       | 342     | 2023-08-29 | 2023-09-12 | NULL       | 0.00       |
| 591     | 441       | 343     | 2023-08-30 | 2023-09-13 | NULL       | 0.00       |
| 592     | 442       | 344     | 2023-08-31 | 2023-09-14 | 2023-09-14 | 0.00       |
| 593     | 443       | 345     | 2023-09-01 | 2023-09-15 | 2023-09-12 | 0.00       |
| 594     | 444       | 346     | 2023-09-02 | 2023-09-16 | NULL       | 0.00       |
| 595     | 445       | 347     | 2023-09-03 | 2023-09-17 | 2023-09-15 | 0.00       |
| 596     | 446       | 348     | 2023-09-04 | 2023-09-18 | NULL       | 0.00       |
| 597     | 447       | 301     | 2023-09-05 | 2023-09-19 | NULL       | 0.00       |
| 598     | 448       | 302     | 2023-09-06 | 2023-09-20 | 2023-09-20 | 0.00       |
| 599     | 449       | 303     | 2023-09-07 | 2023-09-21 | 2023-09-18 | 0.00       |
| 600     | 450       | 304     | 2023-09-08 | 2023-09-22 | 2023-09-22 | 0.00       |
+---------+-----------+---------+------------+------------+------------+------------+

```

```sql
CREATE TABLE loans (
    loan_id INT NOT NULL AUTO_INCREMENT,
    member_id INT NOT NULL,
    book_id INT NOT NULL,
    loan_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    fine_amount DECIMAL(6,2) DEFAULT 0.00,
    PRIMARY KEY (loan_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
) ENGINE=InnoDB;

INSERT INTO loan (loan_id, member_id, book_id, loan_date, due_date, return_date, fine_amount)VALUES
(501, 401, 301, '2023-06-01', '2023-06-15', '2023-06-16', 1.00),
(502, 402, 302, '2023-06-02', '2023-06-16', '2023-06-18', 2.00),
(503, 403, 303, '2023-06-03', '2023-06-17', '2023-06-14', 0.00),
(504, 404, 304, '2023-06-04', '2023-06-18', '2023-06-15', 0.00),
(505, 405, 305, '2023-06-05', '2023-06-19', NULL, 0.00),
(506, 406, 306, '2023-06-06', '2023-06-20', '2023-06-18', 0.00),
(507, 407, 307, '2023-06-07', '2023-06-21', '2023-06-20', 0.00),
(508, 408, 308, '2023-06-08', '2023-06-22', '2023-06-19', 0.00),
(509, 409, 309, '2023-06-09', '2023-06-23', '2023-06-25', 2.00),
(510, 410, 310, '2023-06-10', '2023-06-24', '2023-06-28', 4.00),
(511, 411, 311, '2023-06-11', '2023-06-25', '2023-06-22', 0.00),
(512, 412, 312, '2023-06-12', '2023-06-26', '2023-06-25', 0.00),
(513, 413, 313, '2023-06-13', '2023-06-27', '2023-06-29', 2.00),
(514, 414, 314, '2023-06-14', '2023-06-28', '2023-07-01', 3.00),
(515, 415, 315, '2023-06-15', '2023-06-29', '2023-06-28', 0.00),
(516, 416, 316, '2023-06-16', '2023-06-30', NULL, 0.00),
(517, 417, 317, '2023-06-17', '2023-07-01', '2023-07-01', 0.00),
(518, 418, 318, '2023-06-18', '2023-07-02', '2023-07-01', 0.00),
(519, 419, 319, '2023-06-19', '2023-07-03', '2023-07-03', 0.00),
(520, 420, 320, '2023-06-20', '2023-07-04', '2023-07-04', 0.00),
(521, 421, 321, '2023-06-21', '2023-07-05', '2023-07-04', 0.00),
(522, 422, 322, '2023-06-22', '2023-07-06', '2023-07-07', 1.00),
(523, 423, 323, '2023-06-23', '2023-07-07', NULL, 0.00),
(524, 424, 324, '2023-06-24', '2023-07-08', '2023-07-08', 0.00),
(525, 425, 325, '2023-06-25', '2023-07-09', '2023-07-09', 0.00),
(526, 426, 326, '2023-06-26', '2023-07-10', NULL, 0.00),
(527, 427, 327, '2023-06-27', '2023-07-11', '2023-07-14', 3.00),
(528, 428, 328, '2023-06-28', '2023-07-12', '2023-07-12', 0.00),
(529, 429, 329, '2023-06-29', '2023-07-13', '2023-07-14', 1.00),
(530, 430, 330, '2023-06-30', '2023-07-14', '2023-07-17', 3.00),
(531, 431, 331, '2023-07-01', '2023-07-15', NULL, 0.00),
(532, 432, 332, '2023-07-02', '2023-07-16', NULL, 0.00),
(533, 433, 333, '2023-07-03', '2023-07-17', NULL, 0.00),
(534, 434, 334, '2023-07-04', '2023-07-18', '2023-07-18', 0.00),
(535, 435, 335, '2023-07-05', '2023-07-19', '2023-07-19', 0.00),
(536, 436, 336, '2023-07-06', '2023-07-20', NULL, 0.00),
(537, 437, 337, '2023-07-07', '2023-07-21', '2023-07-19', 0.00),
(538, 438, 338, '2023-07-08', '2023-07-22', '2023-07-20', 0.00),
(539, 439, 339, '2023-07-09', '2023-07-23', '2023-07-24', 1.00),
(540, 440, 340, '2023-07-10', '2023-07-24', '2023-07-26', 2.00),
(541, 441, 341, '2023-07-11', '2023-07-25', '2023-07-25', 0.00),
(542, 442, 342, '2023-07-12', '2023-07-26', '2023-07-24', 0.00),
(543, 443, 343, '2023-07-13', '2023-07-27', '2023-07-27', 0.00),
(544, 444, 344, '2023-07-14', '2023-07-28', NULL, 0.00),
(545, 445, 345, '2023-07-15', '2023-07-29', '2023-07-31', 2.00),
(546, 446, 346, '2023-07-16', '2023-07-30', '2023-07-31', 1.00),
(547, 447, 347, '2023-07-17', '2023-07-31', '2023-07-30', 0.00),
(548, 448, 348, '2023-07-18', '2023-08-01', NULL, 0.00),
(549, 449, 301, '2023-07-19', '2023-08-02', '2023-08-02', 0.00),
(550, 450, 302, '2023-07-20', '2023-08-03', '2023-07-31', 0.00),
(551, 401, 303, '2023-07-21', '2023-08-04', NULL, 0.00),
(552, 402, 304, '2023-07-22', '2023-08-05', '2023-08-05', 0.00),
(553, 403, 305, '2023-07-23', '2023-08-06', '2023-08-10', 4.00),
(554, 404, 306, '2023-07-24', '2023-08-07', NULL, 0.00),
(555, 405, 307, '2023-07-25', '2023-08-08', '2023-08-10', 2.00),
(556, 406, 308, '2023-07-26', '2023-08-09', '2023-08-08', 0.00),
(557, 407, 309, '2023-07-27', '2023-08-10', '2023-08-13', 3.00),
(558, 408, 310, '2023-07-28', '2023-08-11', '2023-08-15', 4.00),
(559, 409, 311, '2023-07-29', '2023-08-12', NULL, 0.00),
(560, 410, 312, '2023-07-30', '2023-08-13', '2023-08-13', 0.00),
(561, 411, 313, '2023-07-31', '2023-08-14', '2023-08-13', 0.00),
(562, 412, 314, '2023-08-01', '2023-08-15', '2023-08-15', 0.00),
(563, 413, 315, '2023-08-02', '2023-08-16', '2023-08-15', 0.00),
(564, 414, 316, '2023-08-03', '2023-08-17', NULL, 0.00),
(565, 415, 317, '2023-08-04', '2023-08-18', '2023-08-17', 0.00),
(566, 416, 318, '2023-08-05', '2023-08-19', '2023-08-23', 4.00),
(567, 417, 319, '2023-08-06', '2023-08-20', '2023-08-20', 0.00),
(568, 418, 320, '2023-08-07', '2023-08-21', '2023-08-21', 0.00),
(569, 419, 321, '2023-08-08', '2023-08-22', '2023-08-22', 0.00),
(570, 420, 322, '2023-08-09', '2023-08-23', '2023-08-23', 0.00),
(571, 421, 323, '2023-08-10', '2023-08-24', '2023-08-21', 0.00),
(572, 422, 324, '2023-08-11', '2023-08-25', NULL, 0.00),
(573, 423, 325, '2023-08-12', '2023-08-26', '2023-08-23', 0.00),
(574, 424, 326, '2023-08-13', '2023-08-27', '2023-08-24', 0.00),
(575, 425, 327, '2023-08-14', '2023-08-28', '2023-08-31', 3.00),
(576, 426, 328, '2023-08-15', '2023-08-29', '2023-08-27', 0.00),
(577, 427, 329, '2023-08-16', '2023-08-30', '2023-08-29', 0.00),
(578, 428, 330, '2023-08-17', '2023-08-31', NULL, 0.00),
(579, 429, 331, '2023-08-18', '2023-09-01', NULL, 0.00),
(580, 430, 332, '2023-08-19', '2023-09-02', '2023-08-30', 0.00),
(581, 431, 333, '2023-08-20', '2023-09-03', '2023-09-04', 1.00),
(582, 432, 334, '2023-08-21', '2023-09-04', NULL, 0.00),
(583, 433, 335, '2023-08-22', '2023-09-05', '2023-09-02', 0.00),
(584, 434, 336, '2023-08-23', '2023-09-06', '2023-09-06', 0.00),
(585, 435, 337, '2023-08-24', '2023-09-07', '2023-09-05', 0.00),
(586, 436, 338, '2023-08-25', '2023-09-08', '2023-09-09', 1.00),
(587, 437, 339, '2023-08-26', '2023-09-09', '2023-09-09', 0.00),
(588, 438, 340, '2023-08-27', '2023-09-10', '2023-09-10', 0.00),
(589, 439, 341, '2023-08-28', '2023-09-11', '2023-09-09', 0.00),
(590, 440, 342, '2023-08-29', '2023-09-12', NULL, 0.00),
(591, 441, 343, '2023-08-30', '2023-09-13', NULL, 0.00),
(592, 442, 344, '2023-08-31', '2023-09-14', '2023-09-14', 0.00),
(593, 443, 345, '2023-09-01', '2023-09-15', '2023-09-12', 0.00),
(594, 444, 346, '2023-09-02', '2023-09-16', NULL, 0.00),
(595, 445, 347, '2023-09-03', '2023-09-17', '2023-09-15', 0.00),
(596, 446, 348, '2023-09-04', '2023-09-18', NULL, 0.00),
(597, 447, 301, '2023-09-05', '2023-09-19', NULL, 0.00),
(598, 448, 302, '2023-09-06', '2023-09-20', '2023-09-20', 0.00),
(599, 449, 303, '2023-09-07', '2023-09-21', '2023-09-18', 0.00),
(600, 450, 304, '2023-09-08', '2023-09-22', '2023-09-22', 0.00);
```