
# Sector 5: Airline

### Table 1: airports
```
+---------------+---------------+------+-----+---------+----------------+
| Field         | Type          | Null | Key | Default | Extra          |
+---------------+---------------+------+-----+---------+----------------+
| airport_id    | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| name          | VARCHAR(100)  | NO   |     | NULL    |                |
| city          | VARCHAR(50)   | NO   |     | NULL    |                |
| country       | VARCHAR(50)   | NO   |     | NULL    |                |
| iata_code     | CHAR(3)       | NO   | UNI | NULL    |                |
+---------------+---------------+------+-----+---------+----------------+

+-----------+---------------------+------------+-------------+-----------+
| airport_id| name                | city       | country     | iata_code |
+-----------+---------------------+------------+-------------+-----------+
| 1         | John F. Kennedy Intl| New York   | USA         | JFK       |
| 2         | Los Angeles Intl    | Los Angeles| USA         | LAX       |
| 3         | Chicago O'Hare Intl | Chicago    | USA         | ORD       |
| 4         | Dallas/Fort Worth   | Dallas     | USA         | DFW       |
| 5         | Denver Intl         | Denver     | USA         | DEN       |
| 6         | San Francisco Intl  | San Francisco| USA       | SFO       |
| 7         | Miami Intl          | Miami      | USA         | MIA       |
| 8         | Atlanta Intl        | Atlanta    | USA         | ATL       |
| 9         | Seattle-Tacoma Intl | Seattle    | USA         | SEA       |
| 10        | Orlando Intl        | Orlando    | USA         | MCO       |
| 11        | London Heathrow     | London     | UK          | LHR       |
| 12        | London Gatwick      | London     | UK          | LGW       |
| 13        | Manchester Airport  | Manchester | UK          | MAN       |
| 14        | Paris Charles de Gaulle| Paris   | France      | CDG       |
| 15        | Paris Orly          | Paris      | France      | ORY       |
| 16        | Frankfurt Airport   | Frankfurt  | Germany     | FRA       |
| 17        | Munich Airport      | Munich     | Germany     | MUC       |
| 18        | Amsterdam Schiphol  | Amsterdam  | Netherlands | AMS       |
| 19        | Madrid Barajas      | Madrid     | Spain       | MAD       |
| 20        | Barcelona El Prat   | Barcelona  | Spain       | BCN       |
| 21        | Dubai Intl          | Dubai      | UAE         | DXB       |
| 22        | Abu Dhabi Intl      | Abu Dhabi  | UAE         | AUH       |
| 23        | Tokyo Narita        | Tokyo      | Japan       | NRT       |
| 24        | Tokyo Haneda        | Tokyo      | Japan       | HND       |
| 25        | Osaka Kansai        | Osaka      | Japan       | KIX       |
| 26        | Beijing Capital     | Beijing    | China       | PEK       |
| 27        | Shanghai Pudong     | Shanghai   | China       | PVG       |
| 28        | Hong Kong Intl      | Hong Kong  | China       | HKG       |
| 29        | Singapore Changi    | Singapore  | Singapore   | SIN       |
| 30        | Kuala Lumpur Intl   | Kuala Lumpur| Malaysia   | KUL       |
| 31        | Sydney Kingsford Smith| Sydney  | Australia   | SYD       |
| 32        | Melbourne Airport   | Melbourne  | Australia   | MEL       |
| 33        | Brisbane Airport    | Brisbane   | Australia   | BNE       |
| 34        | Toronto Pearson     | Toronto    | Canada      | YYZ       |
| 35        | Vancouver Intl      | Vancouver  | Canada      | YVR       |
| 36        | Montreal Trudeau    | Montreal   | Canada      | YUL       |
| 37        | Mexico City Intl    | Mexico City| Mexico      | MEX       |
| 38        | Cancun Intl         | Cancun     | Mexico      | CUN       |
| 39        | Sao Paulo Guarulhos | Sao Paulo  | Brazil      | GRU       |
| 40        | Rio de Janeiro Galeao| Rio de Janeiro| Brazil   | GIG       |
| 41        | Johannesburg OR Tambo| Johannesburg| South Africa| JNB      |
| 42        | Cape Town Intl      | Cape Town  | South Africa| CPT       |
| 43        | Cairo Intl          | Cairo      | Egypt       | CAI       |
| 44        | Istanbul Airport    | Istanbul   | Turkey      | IST       |
| 45        | Doha Hamad Intl     | Doha       | Qatar       | DOH       |
| 46        | Muscat Intl         | Muscat     | Oman        | MCT       |
| 47        | Bangkok Suvarnabhumi| Bangkok    | Thailand    | BKK       |
| 48        | Phuket Intl         | Phuket     | Thailand    | HKT       |
| 49        | Delhi Indira Gandhi | Delhi      | India       | DEL       |
| 50        | Mumbai Chhatrapati  | Mumbai     | India       | BOM       |
+-----------+---------------------+------------+-------------+-----------+
```

```sql
CREATE TABLE airports (
    airport_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    iata_code CHAR(3) NOT NULL UNIQUE,
    PRIMARY KEY (airport_id)
) ENGINE=InnoDB;

INSERT INTO airports (name, city, country, iata_code) VALUES
('John F. Kennedy Intl','New York','USA','JFK'),
('Los Angeles Intl','Los Angeles','USA','LAX'),
('Chicago O''Hare Intl','Chicago','USA','ORD'),
('Dallas/Fort Worth','Dallas','USA','DFW'),
('Denver Intl','Denver','USA','DEN'),
('San Francisco Intl','San Francisco','USA','SFO'),
('Miami Intl','Miami','USA','MIA'),
('Atlanta Intl','Atlanta','USA','ATL'),
('Seattle-Tacoma Intl','Seattle','USA','SEA'),
('Orlando Intl','Orlando','USA','MCO'),
('London Heathrow','London','UK','LHR'),
('London Gatwick','London','UK','LGW'),
('Manchester Airport','Manchester','UK','MAN'),
('Paris Charles de Gaulle','Paris','France','CDG'),
('Paris Orly','Paris','France','ORY'),
('Frankfurt Airport','Frankfurt','Germany','FRA'),
('Munich Airport','Munich','Germany','MUC'),
('Amsterdam Schiphol','Amsterdam','Netherlands','AMS'),
('Madrid Barajas','Madrid','Spain','MAD'),
('Barcelona El Prat','Barcelona','Spain','BCN'),
('Dubai Intl','Dubai','UAE','DXB'),
('Abu Dhabi Intl','Abu Dhabi','UAE','AUH'),
('Tokyo Narita','Tokyo','Japan','NRT'),
('Tokyo Haneda','Tokyo','Japan','HND'),
('Osaka Kansai','Osaka','Japan','KIX'),
('Beijing Capital','Beijing','China','PEK'),
('Shanghai Pudong','Shanghai','China','PVG'),
('Hong Kong Intl','Hong Kong','China','HKG'),
('Singapore Changi','Singapore','Singapore','SIN'),
('Kuala Lumpur Intl','Kuala Lumpur','Malaysia','KUL'),
('Sydney Kingsford Smith','Sydney','Australia','SYD'),
('Melbourne Airport','Melbourne','Australia','MEL'),
('Brisbane Airport','Brisbane','Australia','BNE'),
('Toronto Pearson','Toronto','Canada','YYZ'),
('Vancouver Intl','Vancouver','Canada','YVR'),
('Montreal Trudeau','Montreal','Canada','YUL'),
('Mexico City Intl','Mexico City','Mexico','MEX'),
('Cancun Intl','Cancun','Mexico','CUN'),
('Sao Paulo Guarulhos','Sao Paulo','Brazil','GRU'),
('Rio de Janeiro Galeao','Rio de Janeiro','Brazil','GIG'),
('Johannesburg OR Tambo','Johannesburg','South Africa','JNB'),
('Cape Town Intl','Cape Town','South Africa','CPT'),
('Cairo Intl','Cairo','Egypt','CAI'),
('Istanbul Airport','Istanbul','Turkey','IST'),
('Doha Hamad Intl','Doha','Qatar','DOH'),
('Muscat Intl','Muscat','Oman','MCT'),
('Bangkok Suvarnabhumi','Bangkok','Thailand','BKK'),
('Phuket Intl','Phuket','Thailand','HKT'),
('Delhi Indira Gandhi','Delhi','India','DEL'),
('Mumbai Chhatrapati','Mumbai','India','BOM');
```

### Table 2: airlines
```
+-------------+---------------+------+-----+---------+----------------+
| Field       | Type          | Null | Key | Default | Extra          |
+-------------+---------------+------+-----+---------+----------------+
| airline_id  | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| name        | VARCHAR(100)  | NO   |     | NULL    |                |
| country     | VARCHAR(50)   | NO   |     | NULL    |                |
| fleet_size  | INT           | NO   |     | 0       |                |
+-------------+---------------+------+-----+---------+----------------+

+-----------+-------------------------+----------------+-----------+
| airline_id| name                    | country        | fleet_size|
+-----------+-------------------------+----------------+-----------+
| 1         | Delta Air Lines         | USA            | 950       |
| 2         | American Airlines       | USA            | 920       |
| 3         | United Airlines         | USA            | 800       |
| 4         | Southwest Airlines      | USA            | 750       |
| 5         | Alaska Airlines         | USA            | 330       |
| 6         | JetBlue Airways         | USA            | 280       |
| 7         | British Airways         | UK             | 250       |
| 8         | Virgin Atlantic         | UK             | 160       |
| 9         | Air France              | France         | 220       |
| 10        | KLM Royal Dutch         | Netherlands    | 180       |
| 11        | Lufthansa               | Germany        | 300       |
| 12        | Turkish Airlines        | Turkey         | 370       |
| 13        | Emirates                | UAE            | 270       |
| 14        | Qatar Airways           | Qatar          | 250       |
| 15        | Singapore Airlines      | Singapore      | 150       |
| 16        | Cathay Pacific          | Hong Kong      | 160       |
| 17        | Japan Airlines          | Japan          | 180       |
| 18        | All Nippon Airways      | Japan          | 200       |
| 19        | Qantas                  | Australia      | 130       |
| 20        | Air New Zealand         | New Zealand    | 100       |
| 21        | Air Canada              | Canada         | 180       |
| 22        | WestJet                 | Canada         | 120       |
| 23        | Avianca                 | Colombia       | 120       |
| 24        | LATAM Airlines          | Chile          | 140       |
| 25        | Gol Airlines            | Brazil         | 120       |
| 26        | Azul Brazilian Airlines | Brazil         | 110       |
| 27        | Ethiopian Airlines      | Ethiopia       | 110       |
| 28        | EgyptAir                | Egypt          | 90        |
| 29        | Kenya Airways           | Kenya          | 50        |
| 30        | South African Airways   | South Africa   | 40        |
| 31        | IndiGo                  | India          | 300       |
| 32        | Air India               | India          | 150       |
| 33        | SpiceJet                | India          | 120       |
| 34        | GoAir                   | India          | 70        |
| 35        | Vistara                 | India          | 50        |
| 36        | Thai Airways            | Thailand       | 80        |
| 37        | Bangkok Airways         | Thailand       | 30        |
| 38        | Philippine Airlines     | Philippines    | 50        |
| 39        | Cebu Pacific            | Philippines    | 60        |
| 40        | China Southern          | China          | 430       |
| 41        | China Eastern           | China          | 400       |
| 42        | Air China               | China          | 350       |
| 43        | Hainan Airlines         | China          | 200       |
| 44        | Korean Air              | South Korea    | 170       |
| 45        | Asiana Airlines         | South Korea    | 90        |
| 46        | ANA Wings               | Japan          | 60        |
| 47        | Ryanair                 | Ireland        | 470       |
| 48        | easyJet                 | UK             | 350       |
| 49        | Norwegian Air Shuttle   | Norway         | 100       |
| 50        | Finnair                 | Finland        | 80        |
+-----------+-------------------------+----------------+-----------+
```

```sql
CREATE TABLE airlines (
    airline_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50) NOT NULL,
    fleet_size INT NOT NULL DEFAULT 0,
    PRIMARY KEY (airline_id)
) ENGINE=InnoDB;

INSERT INTO airlines (name, country, fleet_size) VALUES
('Delta Air Lines','USA',950),
('American Airlines','USA',920),
('United Airlines','USA',800),
('Southwest Airlines','USA',750),
('Alaska Airlines','USA',330),
('JetBlue Airways','USA',280),
('British Airways','UK',250),
('Virgin Atlantic','UK',160),
('Air France','France',220),
('KLM Royal Dutch','Netherlands',180),
('Lufthansa','Germany',300),
('Turkish Airlines','Turkey',370),
('Emirates','UAE',270),
('Qatar Airways','Qatar',250),
('Singapore Airlines','Singapore',150),
('Cathay Pacific','Hong Kong',160),
('Japan Airlines','Japan',180),
('All Nippon Airways','Japan',200),
('Qantas','Australia',130),
('Air New Zealand','New Zealand',100),
('Air Canada','Canada',180),
('WestJet','Canada',120),
('Avianca','Colombia',120),
('LATAM Airlines','Chile',140),
('Gol Airlines','Brazil',120),
('Azul Brazilian Airlines','Brazil',110),
('Ethiopian Airlines','Ethiopia',110),
('EgyptAir','Egypt',90),
('Kenya Airways','Kenya',50),
('South African Airways','South Africa',40),
('IndiGo','India',300),
('Air India','India',150),
('SpiceJet','India',120),
('GoAir','India',70),
('Vistara','India',50),
('Thai Airways','Thailand',80),
('Bangkok Airways','Thailand',30),
('Philippine Airlines','Philippines',50),
('Cebu Pacific','Philippines',60),
('China Southern','China',430),
('China Eastern','China',400),
('Air China','China',350),
('Hainan Airlines','China',200),
('Korean Air','South Korea',170),
('Asiana Airlines','South Korea',90),
('ANA Wings','Japan',60),
('Ryanair','Ireland',470),
('easyJet','UK',350),
('Norwegian Air Shuttle','Norway',100),
('Finnair','Finland',80);
```

### Table 3: flights
```
+------------------+---------------+------+-----+---------+----------------+
| Field            | Type          | Null | Key | Default | Extra          |
+------------------+---------------+------+-----+---------+----------------+
| flight_id        | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| flight_number    | VARCHAR(10)   | NO   | UNI | NULL    |                |
| airline_id       | INT           | NO   | MUL | NULL    |                |
| origin_airport   | INT           | NO   | MUL | NULL    |                |
| destination_airport| INT         | NO   | MUL | NULL    |                |
| departure_time   | DATETIME      | NO   |     | NULL    |                |
| arrival_time     | DATETIME      | NO   |     | NULL    |                |
| status           | VARCHAR(20)   | NO   |     | 'Scheduled' |           |
+------------------+---------------+------+-----+---------+----------------+

+-----------+--------------+-----------+----------------+------------------+---------------------+---------------------+------------+
| flight_id | flight_number| airline_id| origin_airport | destination_airport| departure_time      | arrival_time        | status     |
+-----------+--------------+-----------+----------------+------------------+---------------------+---------------------+------------+
| 1         | DL101        | 1         | 1              | 2                | 2025-12-07 08:00:00 | 2025-12-07 11:00:00 | Scheduled |
| 2         | AA202        | 2         | 2              | 3                | 2025-12-07 09:00:00 | 2025-12-07 12:00:00 | Scheduled |
| 3         | UA303        | 3         | 3              | 4                | 2025-12-07 10:00:00 | 2025-12-07 13:00:00 | Delayed   |
| 4         | SW404        | 4         | 4              | 5                | 2025-12-07 11:00:00 | 2025-12-07 14:00:00 | Cancelled |
| 5         | DL505        | 1         | 5              | 6                | 2025-12-07 12:00:00 | 2025-12-07 15:00:00 | Scheduled |
| 6         | AA606        | 2         | 6              | 7                | 2025-12-07 13:00:00 | 2025-12-07 16:00:00 | Scheduled |
| 7         | UA707        | 3         | 7              | 8                | 2025-12-07 14:00:00 | 2025-12-07 17:00:00 | Scheduled |
| 8         | SW808        | 4         | 8              | 9                | 2025-12-07 15:00:00 | 2025-12-07 18:00:00 | Delayed   |
| 9         | DL909        | 1         | 9              | 10               | 2025-12-07 16:00:00 | 2025-12-07 19:00:00 | Scheduled |
| 10        | AA010        | 2         | 10             | 1                | 2025-12-07 17:00:00 | 2025-12-07 20:00:00 | Scheduled |
| 11        | BA111        | 7         | 11             | 12               | 2025-12-07 08:00:00 | 2025-12-07 09:30:00 | Scheduled |
| 12        | AF222        | 9         | 14             | 15               | 2025-12-07 09:00:00 | 2025-12-07 10:30:00 | Delayed   |
| 13        | LH333        | 11        | 16             | 17               | 2025-12-07 10:00:00 | 2025-12-07 11:30:00 | Scheduled |
| 14        | TK444        | 12        | 44             | 21               | 2025-12-07 11:00:00 | 2025-12-07 14:00:00 | Scheduled |
| 15        | EK555        | 13        | 21             | 22               | 2025-12-07 12:00:00 | 2025-12-07 15:30:00 | Cancelled |
| 16        | QR666        | 14        | 22             | 29               | 2025-12-07 13:00:00 | 2025-12-07 19:00:00 | Scheduled |
| 17        | SQ777        | 15        | 29             | 30               | 2025-12-07 14:00:00 | 2025-12-07 18:00:00 | Scheduled |
| 18        | CX888        | 16        | 28             | 23               | 2025-12-07 15:00:00 | 2025-12-07 23:00:00 | Delayed   |
| 19        | JL999        | 17        | 23             | 24               | 2025-12-07 16:00:00 | 2025-12-07 18:00:00 | Scheduled |
| 20        | NH010        | 18        | 24             | 25               | 2025-12-07 17:00:00 | 2025-12-07 19:30:00 | Scheduled |
| 21        | QF111        | 19        | 31             | 32               | 2025-12-07 08:00:00 | 2025-12-07 10:00:00 | Scheduled |
| 22        | NZ222        | 20        | 32             | 33               | 2025-12-07 09:00:00 | 2025-12-07 11:00:00 | Scheduled |
| 23        | AC333        | 21        | 34             | 35               | 2025-12-07 10:00:00 | 2025-12-07 12:00:00 | Delayed   |
| 24        | WS444        | 22        | 35             | 36               | 2025-12-07 11:00:00 | 2025-12-07 13:00:00 | Scheduled |
| 25        | AV555        | 23        | 37             | 38               | 2025-12-07 12:00:00 | 2025-12-07 14:30:00 | Scheduled |
| 26        | LA666        | 24        | 38             | 39               | 2025-12-07 13:00:00 | 2025-12-07 15:00:00 | Cancelled |
| 27        | G3123        | 25        | 39             | 40               | 2025-12-07 14:00:00 | 2025-12-07 16:30:00 | Scheduled |
| 28        | AZ444        | 26        | 40             | 41               | 2025-12-07 15:00:00 | 2025-12-07 17:30:00 | Scheduled |
| 29        | ET555        | 27        | 41             | 42               | 2025-12-07 16:00:00 | 2025-12-07 18:30:00 | Delayed   |
| 30        | MS666        | 28        | 43             | 44               | 2025-12-07 17:00:00 | 2025-12-07 19:30:00 | Scheduled |
| 31        | KE777        | 29        | 45             | 49               | 2025-12-07 08:00:00 | 2025-12-07 10:30:00 | Scheduled |
| 32        | SA888        | 30        | 42             | 41               | 2025-12-07 09:00:00 | 2025-12-07 11:30:00 | Scheduled |
| 33        | IG999        | 31        | 49             | 50               | 2025-12-07 10:00:00 | 2025-12-07 12:30:00 | Scheduled |
| 34        | AI010        | 32        | 50             | 49               | 2025-12-07 11:00:00 | 2025-12-07 13:30:00 | Delayed   |
| 35        | SG111        | 33        | 35             | 34               | 2025-12-07 12:00:00 | 2025-12-07 14:00:00 | Scheduled |
| 36        | G0444        | 34        | 34             | 36               | 2025-12-07 13:00:00 | 2025-12-07 15:00:00 | Scheduled |
| 37        | V0555        | 35        | 36             | 35               | 2025-12-07 14:00:00 | 2025-12-07 16:00:00 | Scheduled |
| 38        | TG0666       | 36        | 47             | 48               | 2025-12-07 15:00:00 | 2025-12-07 17:00:00 | Cancelled |
| 39        | PG0777       | 38        | 50             | 49               | 2025-12-07 16:00:00 | 2025-12-07 18:30:00 | Scheduled |
| 40        | CP0888       | 39        | 49             | 50               | 2025-12-07 17:00:00 | 2025-12-07 19:30:00 | Scheduled |
| 41        | CZ0999       | 40        | 26             | 27               | 2025-12-07 08:00:00 | 2025-12-07 10:30:00 | Scheduled |
| 42        | CE0100       | 41        | 27             | 28               | 2025-12-07 09:00:00 | 2025-12-07 11:30:00 | Scheduled |
| 43        | CA0111       | 42        | 26             | 28               | 2025-12-07 10:00:00 | 2025-12-07 12:30:00 | Delayed   |
| 44        | HA0122       | 43        | 28             | 29               | 2025-12-07 11:00:00 | 2025-12-07 13:30:00 | Scheduled |
| 45        | KE0133       | 44        | 23             | 24               | 2025-12-07 12:00:00 | 2025-12-07 14:30:00 | Scheduled |
| 46        | AS0144       | 45        | 24             | 23               | 2025-12-07 13:00:00 | 2025-12-07 15:30:00 | Scheduled |
| 47        | AN0155       | 46        | 24             | 25               | 2025-12-07 14:00:00 | 2025-12-07 16:30:00 | Delayed   |
| 48        | RY0166       | 47        | 11             | 12               | 2025-12-07 15:00:00 | 2025-12-07 16:30:00 | Scheduled |
| 49        | EJ0177       | 48        | 12             | 11               | 2025-12-07 16:00:00 | 2025-12-07 17:30:00 | Scheduled |
| 50        | NO0188       | 49        | 13             | 14               | 2025-12-07 17:00:00 | 2025-12-07 18:30:00 | Cancelled |
+-----------+--------------+-----------+----------------+------------------+---------------------+---------------------+------------+
```

```sql
CREATE TABLE flights (
    flight_id INT NOT NULL AUTO_INCREMENT,
    flight_number VARCHAR(10) NOT NULL UNIQUE,
    airline_id INT NOT NULL,
    origin_airport INT NOT NULL,
    destination_airport INT NOT NULL,
    departure_time DATETIME NOT NULL,
    arrival_time DATETIME NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Scheduled',
    PRIMARY KEY (flight_id),
    FOREIGN KEY (airline_id) REFERENCES airlines(airline_id),
    FOREIGN KEY (origin_airport) REFERENCES airports(airport_id),
    FOREIGN KEY (destination_airport) REFERENCES airports(airport_id)
) ENGINE=InnoDB;

INSERT INTO flights (flight_id, flight_number, airline_id, origin_airport, destination_airport, departure_time, arrival_time, status) VALUES
(1, 'DL101', 1, 1, 2, '2025-12-07 08:00:00', '2025-12-07 11:00:00', 'Scheduled'),
(2, 'AA202', 2, 2, 3, '2025-12-07 09:00:00', '2025-12-07 12:00:00', 'Scheduled'),
(3, 'UA303', 3, 3, 4, '2025-12-07 10:00:00', '2025-12-07 13:00:00', 'Delayed'),
(4, 'SW404', 4, 4, 5, '2025-12-07 11:00:00', '2025-12-07 14:00:00', 'Cancelled'),
(5, 'DL505', 1, 5, 6, '2025-12-07 12:00:00', '2025-12-07 15:00:00', 'Scheduled'),
(6, 'AA606', 2, 6, 7, '2025-12-07 13:00:00', '2025-12-07 16:00:00', 'Scheduled'),
(7, 'UA707', 3, 7, 8, '2025-12-07 14:00:00', '2025-12-07 17:00:00', 'Scheduled'),
(8, 'SW808', 4, 8, 9, '2025-12-07 15:00:00', '2025-12-07 18:00:00', 'Delayed'),
(9, 'DL909', 1, 9, 10, '2025-12-07 16:00:00', '2025-12-07 19:00:00', 'Scheduled'),
(10, 'AA010', 2, 10, 1, '2025-12-07 17:00:00', '2025-12-07 20:00:00', 'Scheduled'),
(11, 'BA111', 7, 11, 12, '2025-12-07 08:00:00', '2025-12-07 09:30:00', 'Scheduled'),
(12, 'AF222', 9, 14, 15, '2025-12-07 09:00:00', '2025-12-07 10:30:00', 'Delayed'),
(13, 'LH333', 11, 16, 17, '2025-12-07 10:00:00', '2025-12-07 11:30:00', 'Scheduled'),
(14, 'TK444', 12, 44, 21, '2025-12-07 11:00:00', '2025-12-07 14:00:00', 'Scheduled'),
(15, 'EK555', 13, 21, 22, '2025-12-07 12:00:00', '2025-12-07 15:30:00', 'Cancelled'),
(16, 'QR666', 14, 22, 29, '2025-12-07 13:00:00', '2025-12-07 19:00:00', 'Scheduled'),
(17, 'SQ777', 15, 29, 30, '2025-12-07 14:00:00', '2025-12-07 18:00:00', 'Scheduled'),
(18, 'CX888', 16, 28, 23, '2025-12-07 15:00:00', '2025-12-07 23:00:00', 'Delayed'),
(19, 'JL999', 17, 23, 24, '2025-12-07 16:00:00', '2025-12-07 18:00:00', 'Scheduled'),
(20, 'NH010', 18, 24, 25, '2025-12-07 17:00:00', '2025-12-07 19:30:00', 'Scheduled'),
(21, 'QF111', 19, 31, 32, '2025-12-07 08:00:00', '2025-12-07 10:00:00', 'Scheduled'),
(22, 'NZ222', 20, 32, 33, '2025-12-07 09:00:00', '2025-12-07 11:00:00', 'Scheduled'),
(23, 'AC333', 21, 34, 35, '2025-12-07 10:00:00', '2025-12-07 12:00:00', 'Delayed'),
(24, 'WS444', 22, 35, 36, '2025-12-07 11:00:00', '2025-12-07 13:00:00', 'Scheduled'),
(25, 'AV555', 23, 37, 38, '2025-12-07 12:00:00', '2025-12-07 14:30:00', 'Scheduled'),
(26, 'LA666', 24, 38, 39, '2025-12-07 13:00:00', '2025-12-07 15:00:00', 'Cancelled'),
(27, 'G3123', 25, 39, 40, '2025-12-07 14:00:00', '2025-12-07 16:30:00', 'Scheduled'),
(28, 'AZ444', 26, 40, 41, '2025-12-07 15:00:00', '2025-12-07 17:30:00', 'Scheduled'),
(29, 'ET555', 27, 41, 42, '2025-12-07 16:00:00', '2025-12-07 18:30:00', 'Delayed'),
(30, 'MS666', 28, 43, 44, '2025-12-07 17:00:00', '2025-12-07 19:30:00', 'Scheduled'),
(31, 'KE777', 29, 45, 49, '2025-12-07 08:00:00', '2025-12-07 10:30:00', 'Scheduled'),
(32, 'SA888', 30, 42, 41, '2025-12-07 09:00:00', '2025-12-07 11:30:00', 'Scheduled'),
(33, 'IG999', 31, 49, 50, '2025-12-07 10:00:00', '2025-12-07 12:30:00', 'Scheduled'),
(34, 'AI010', 32, 50, 49, '2025-12-07 11:00:00', '2025-12-07 13:30:00', 'Delayed'),
(35, 'SG111', 33, 35, 34, '2025-12-07 12:00:00', '2025-12-07 14:00:00', 'Scheduled'),
(36, 'G0444', 34, 34, 36, '2025-12-07 13:00:00', '2025-12-07 15:00:00', 'Scheduled'),
(37, 'V0555', 35, 36, 35, '2025-12-07 14:00:00', '2025-12-07 16:00:00', 'Scheduled'),
(38, 'TG0666', 36, 47, 48, '2025-12-07 15:00:00', '2025-12-07 17:00:00', 'Cancelled'),
(39, 'PG0777', 38, 50, 49, '2025-12-07 16:00:00', '2025-12-07 18:30:00', 'Scheduled'),
(40, 'CP0888', 39, 49, 50, '2025-12-07 17:00:00', '2025-12-07 19:30:00', 'Scheduled'),
(41, 'CZ0999', 40, 26, 27, '2025-12-07 08:00:00', '2025-12-07 10:30:00', 'Scheduled'),
(42, 'CE0100', 41, 27, 28, '2025-12-07 09:00:00', '2025-12-07 11:30:00', 'Scheduled'),
(43, 'CA0111', 42, 26, 28, '2025-12-07 10:00:00', '2025-12-07 12:30:00', 'Delayed'),
(44, 'HA0122', 43, 28, 29, '2025-12-07 11:00:00', '2025-12-07 13:30:00', 'Scheduled'),
(45, 'KE0133', 44, 23, 24, '2025-12-07 12:00:00', '2025-12-07 14:30:00', 'Scheduled'),
(46, 'AS0144', 45, 24, 23, '2025-12-07 13:00:00', '2025-12-07 15:30:00', 'Scheduled'),
(47, 'AN0155', 46, 24, 25, '2025-12-07 14:00:00', '2025-12-07 16:30:00', 'Delayed'),
(48, 'RY0166', 47, 11, 12, '2025-12-07 15:00:00', '2025-12-07 16:30:00', 'Scheduled'),
(49, 'EJ0177', 48, 12, 11, '2025-12-07 16:00:00', '2025-12-07 17:30:00', 'Scheduled'),
(50, 'NO0188', 49, 13, 14, '2025-12-07 17:00:00', '2025-12-07 18:30:00', 'Cancelled');
```

### Table 4: passengers
```
+----------------+---------------+------+-----+---------+----------------+
| Field          | Type          | Null | Key | Default | Extra          |
+----------------+---------------+------+-----+---------+----------------+
| passenger_id   | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| first_name     | VARCHAR(50)   | NO   |     | NULL    |                |
| last_name      | VARCHAR(50)   | NO   |     | NULL    |                |
| email          | VARCHAR(100)  | YES  | UNI | NULL    |                |
| phone          | VARCHAR(20)   | YES  |     | NULL    |                |
| passport_no    | VARCHAR(20)   | NO   | UNI | NULL    |                |
| nationality    | VARCHAR(50)   | NO   |     | NULL    |                |
+----------------+---------------+------+-----+---------+----------------+

+-------------+------------+-----------+-------------------------+----------------+-------------+----------------+
| passenger_id| first_name | last_name | email                   | phone          | passport_no | nationality    |
+-------------+------------+-----------+-------------------------+----------------+-------------+----------------+
| 1           | John       | Smith     | john.smith@example.com  | +1-202-555-0101| P1234567    | USA            |
| 2           | Maria      | Garcia    | maria.garcia@example.com| +34-912-555-010| P2345678    | Spain          |
| 3           | Chen       | Li        | chen.li@example.com     | +86-10-5555-01 | P3456789    | China          |
| 4           | Hiroshi    | Tanaka    | hiro.tanaka@example.jp  | +81-3-5555-01  | P4567890    | Japan          |
| 5           | Emma       | Brown     | emma.brown@example.com  | +44-20-5555-01 | P5678901    | UK             |
| 6           | Ahmed      | Khan      | ahmed.khan@example.ae   | +971-4-555-0101| P6789012    | UAE            |
| 7           | Sarah      | Johnson   | sarah.johnson@example.com| +1-202-555-0202| P7890123   | USA            |
| 8           | Pedro      | Alvarez   | pedro.alvarez@example.com| +34-912-555-020| P8901234   | Spain          |
| 9           | Li         | Wei       | li.wei@example.com      | +86-21-5555-02 | P9012345    | China          |
| 10          | Yuki       | Sato      | yuki.sato@example.jp    | +81-3-5555-02  | P0123456    | Japan          |
| 11          | Olivia     | Williams  | olivia.williams@example.com | +44-20-5555-02 | P1122334 | UK           |
| 12          | Khalid     | Al-Mansoor| khalid.mansoor@example.ae| +971-4-555-0202| P2233445 | UAE           |
| 13          | David      | Miller    | david.miller@example.com| +1-202-555-0303| P3344556    | USA            |
| 14          | Sofia      | Fernandez | sofia.fernandez@example.com| +34-912-555-030| P4455667 | Spain         |
| 15          | Wang       | Mei       | wang.mei@example.com    | +86-10-5555-03 | P5566778    | China          |
| 16          | Takashi    | Yamamoto  | takashi.yamamoto@example.jp| +81-3-5555-03| P6677889 | Japan          |
| 17          | Isabella   | Taylor    | isabella.taylor@example.com| +44-20-5555-03| P7788990 | UK             |
| 18          | Fatima     | Al-Hadid  | fatima.alhadid@example.ae| +971-4-555-0303| P8899001 | UAE           |
| 19          | Michael    | Davis     | michael.davis@example.com| +1-202-555-0404| P9900112  | USA            |
| 20          | Lucia      | Martinez  | lucia.martinez@example.com| +34-912-555-040| P1011123 | Spain         |
| 21          | Zhou       | Fang      | zhou.fang@example.com   | +86-21-5555-04 | P1213141    | China          |
| 22          | Kenji      | Kobayashi | kenji.kobayashi@example.jp| +81-3-5555-04| P1314151 | Japan          |
| 23          | Emily      | Wilson    | emily.wilson@example.com| +44-20-5555-04 | P1415161    | UK             |
| 24          | Omar       | Al-Farsi  | omar.alfarsi@example.ae | +971-4-555-0404| P1516171    | UAE           |
| 25          | Daniel     | Anderson  | daniel.anderson@example.com| +1-202-555-0505| P1617181 | USA           |
| 26          | Carmen     | Lopez     | carmen.lopez@example.com| +34-912-555-050| P1718191    | Spain          |
| 27          | Li         | Jie       | li.jie@example.com      | +86-10-5555-05 | P1819202    | China          |
| 28          | Haruto     | Nakamura  | haruto.nakamura@example.jp| +81-3-5555-05| P1920212 | Japan          |
| 29          | Grace      | Hall      | grace.hall@example.com  | +44-20-5555-05 | P2021222    | UK             |
| 30          | Aisha      | Al-Khalid | aisha.alkhalid@example.ae| +971-4-555-0505| P2122232 | UAE           |
| 31          | James      | Scott     | james.scott@example.com | +1-202-555-0606 | P2223242   | USA            |
| 32          | Elena      | Sanchez   | elena.sanchez@example.com| +34-912-555-060| P2324252  | Spain          |
| 33          | Zhang      | Lei       | zhang.lei@example.com   | +86-21-5555-06 | P2425262    | China          |
| 34          | Yui        | Nakamoto  | yui.nakamoto@example.jp | +81-3-5555-06 | P2526272    | Japan          |
| 35          | Chloe      | Moore     | chloe.moore@example.com | +44-20-5555-06 | P2627282    | UK             |
| 36          | Hamad      | Al-Saidi  | hamad.alsaidi@example.ae| +971-4-555-0606| P2728292 | UAE           |
| 37          | Matthew    | Thompson  | matthew.thompson@example.com| +1-202-555-0707| P2829302 | USA           |
| 38          | Ana        | Ruiz      | ana.ruiz@example.com    | +34-912-555-070| P2930313   | Spain          |
| 39          | Liu        | Xin       | liu.xin@example.com     | +86-10-5555-07 | P3031323    | China          |
| 40          | Riku       | Matsumoto | riku.matsumoto@example.jp| +81-3-5555-07| P3132333   | Japan          |
| 41          | Sophie     | Clark     | sophie.clark@example.com| +44-20-5555-07 | P3233343   | UK             |
| 42          | Zayed      | Al-Mansouri| zayed.almansouri@example.ae| +971-4-555-0707| P3334353| UAE           |
| 43          | Ryan       | Lewis     | ryan.lewis@example.com  | +1-202-555-0808 | P3435363   | USA            |
| 44          | Marta      | Gonzalez  | marta.gonzalez@example.com| +34-912-555-080| P3536373  | Spain         |
| 45          | Wu         | Hao       | wu.hao@example.com      | +86-21-5555-08 | P3637383    | China          |
| 46          | Sora       | Fujimoto  | sora.fujimoto@example.jp| +81-3-5555-08 | P3738393   | Japan          |
| 47          | Lily       | Adams     | lily.adams@example.com  | +44-20-5555-08 | P3839403   | UK             |
| 48          | Noura      | Al-Zahra  | noura.alzahra@example.ae| +971-4-555-0808| P3940414  | UAE           |
| 49          | Ethan      | Baker     | ethan.baker@example.com | +1-202-555-0909 | P4041424   | USA            |
| 50          | Sofia      | Romero    | sofia.romero@example.com| +34-912-555-090| P4142434   | Spain         |
+-------------+------------+-----------+-------------------------+----------------+-------------+----------------+
```

```sql
CREATE TABLE passengers (
    passenger_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    passport_no VARCHAR(20) NOT NULL UNIQUE,
    nationality VARCHAR(50) NOT NULL,
    PRIMARY KEY (passenger_id)
) ENGINE=InnoDB;

INSERT INTO passengers (passenger_id, first_name, last_name, email, phone, passport_no, nationality) VALUES
(1, 'John', 'Smith', 'john.smith@example.com', '+1-202-555-0101', 'P1234567', 'USA'),
(2, 'Maria', 'Garcia', 'maria.garcia@example.com', '+34-912-555-010', 'P2345678', 'Spain'),
(3, 'Chen', 'Li', 'chen.li@example.com', '+86-10-5555-01', 'P3456789', 'China'),
(4, 'Hiroshi', 'Tanaka', 'hiro.tanaka@example.jp', '+81-3-5555-01', 'P4567890', 'Japan'),
(5, 'Emma', 'Brown', 'emma.brown@example.com', '+44-20-5555-01', 'P5678901', 'UK'),
(6, 'Ahmed', 'Khan', 'ahmed.khan@example.ae', '+971-4-555-0101', 'P6789012', 'UAE'),
(7, 'Sarah', 'Johnson', 'sarah.johnson@example.com', '+1-202-555-0202', 'P7890123', 'USA'),
(8, 'Pedro', 'Alvarez', 'pedro.alvarez@example.com', '+34-912-555-020', 'P8901234', 'Spain'),
(9, 'Li', 'Wei', 'li.wei@example.com', '+86-21-5555-02', 'P9012345', 'China'),
(10, 'Yuki', 'Sato', 'yuki.sato@example.jp', '+81-3-5555-02', 'P0123456', 'Japan'),
(11, 'Olivia', 'Williams', 'olivia.williams@example.com', '+44-20-5555-02', 'P1122334', 'UK'),
(12, 'Khalid', 'Al-Mansoor', 'khalid.mansoor@example.ae', '+971-4-555-0202', 'P2233445', 'UAE'),
(13, 'David', 'Miller', 'david.miller@example.com', '+1-202-555-0303', 'P3344556', 'USA'),
(14, 'Sofia', 'Fernandez', 'sofia.fernandez@example.com', '+34-912-555-030', 'P4455667', 'Spain'),
(15, 'Wang', 'Mei', 'wang.mei@example.com', '+86-10-5555-03', 'P5566778', 'China'),
(16, 'Takashi', 'Yamamoto', 'takashi.yamamoto@example.jp', '+81-3-5555-03', 'P6677889', 'Japan'),
(17, 'Isabella', 'Taylor', 'isabella.taylor@example.com', '+44-20-5555-03', 'P7788990', 'UK'),
(18, 'Fatima', 'Al-Hadid', 'fatima.alhadid@example.ae', '+971-4-555-0303', 'P8899001', 'UAE'),
(19, 'Michael', 'Davis', 'michael.davis@example.com', '+1-202-555-0404', 'P9900112', 'USA'),
(20, 'Lucia', 'Martinez', 'lucia.martinez@example.com', '+34-912-555-040', 'P1011123', 'Spain'),
(21, 'Zhou', 'Fang', 'zhou.fang@example.com', '+86-21-5555-04', 'P1213141', 'China'),
(22, 'Kenji', 'Kobayashi', 'kenji.kobayashi@example.jp', '+81-3-5555-04', 'P1314151', 'Japan'),
(23, 'Emily', 'Wilson', 'emily.wilson@example.com', '+44-20-5555-04', 'P1415161', 'UK'),
(24, 'Omar', 'Al-Farsi', 'omar.alfarsi@example.ae', '+971-4-555-0404', 'P1516171', 'UAE'),
(25, 'Daniel', 'Anderson', 'daniel.anderson@example.com', '+1-202-555-0505', 'P1617181', 'USA'),
(26, 'Carmen', 'Lopez', 'carmen.lopez@example.com', '+34-912-555-050', 'P1718191', 'Spain'),
(27, 'Li', 'Jie', 'li.jie@example.com', '+86-10-5555-05', 'P1819202', 'China'),
(28, 'Haruto', 'Nakamura', 'haruto.nakamura@example.jp', '+81-3-5555-05', 'P1920212', 'Japan'),
(29, 'Grace', 'Hall', 'grace.hall@example.com', '+44-20-5555-05', 'P2021222', 'UK'),
(30, 'Aisha', 'Al-Khalid', 'aisha.alkhalid@example.ae', '+971-4-555-0505', 'P2122232', 'UAE'),
(31, 'James', 'Scott', 'james.scott@example.com', '+1-202-555-0606', 'P2223242', 'USA'),
(32, 'Elena', 'Sanchez', 'elena.sanchez@example.com', '+34-912-555-060', 'P2324252', 'Spain'),
(33, 'Zhang', 'Lei', 'zhang.lei@example.com', '+86-21-5555-06', 'P2425262', 'China'),
(34, 'Yui', 'Nakamoto', 'yui.nakamoto@example.jp', '+81-3-5555-06', 'P2526272', 'Japan'),
(35, 'Chloe', 'Moore', 'chloe.moore@example.com', '+44-20-5555-06', 'P2627282', 'UK'),
(36, 'Hamad', 'Al-Saidi', 'hamad.alsaidi@example.ae', '+971-4-555-0606', 'P2728292', 'UAE'),
(37, 'Matthew', 'Thompson', 'matthew.thompson@example.com', '+1-202-555-0707', 'P2829302', 'USA'),
(38, 'Ana', 'Ruiz', 'ana.ruiz@example.com', '+34-912-555-070', 'P2930313', 'Spain'),
(39, 'Liu', 'Xin', 'liu.xin@example.com', '+86-10-5555-07', 'P3031323', 'China'),
(40, 'Riku', 'Matsumoto', 'riku.matsumoto@example.jp', '+81-3-5555-07', 'P3132333', 'Japan'),
(41, 'Sophie', 'Clark', 'sophie.clark@example.com', '+44-20-5555-07', 'P3233343', 'UK'),
(42, 'Zayed', 'Al-Mansouri', 'zayed.almansouri@example.ae', '+971-4-555-0707', 'P3334353', 'UAE'),
(43, 'Ryan', 'Lewis', 'ryan.lewis@example.com', '+1-202-555-0808', 'P3435363', 'USA'),
(44, 'Marta', 'Gonzalez', 'marta.gonzalez@example.com', '+34-912-555-080', 'P3536373', 'Spain'),
(45, 'Wu', 'Hao', 'wu.hao@example.com', '+86-21-5555-08', 'P3637383', 'China'),
(46, 'Sora', 'Fujimoto', 'sora.fujimoto@example.jp', '+81-3-5555-08', 'P3738393', 'Japan'),
(47, 'Lily', 'Adams', 'lily.adams@example.com', '+44-20-5555-08', 'P3839403', 'UK'),
(48, 'Noura', 'Al-Zahra', 'noura.alzahra@example.ae', '+971-4-555-0808', 'P3940414', 'UAE'),
(49, 'Ethan', 'Baker', 'ethan.baker@example.com', '+1-202-555-0909', 'P4041424', 'USA'),
(50, 'Sofia', 'Romero', 'sofia.romero@example.com', '+34-912-555-090', 'P4142434', 'Spain');
```

### Table 5: tickets
```
+----------------+---------------+------+-----+---------+----------------+
| Field          | Type          | Null | Key | Default | Extra          |
+----------------+---------------+------+-----+---------+----------------+
| ticket_id      | INT           | NO   | PRI | NULL    | AUTO_INCREMENT |
| flight_id      | INT           | NO   | MUL | NULL    |                |
| passenger_id   | INT           | NO   | MUL | NULL    |                |
| seat_no        | VARCHAR(5)    | NO   |     | NULL    |                |
| price          | DECIMAL(8,2)  | NO   |     | 0.00    |                |
| booking_date   | DATE          | NO   |     | NULL    |                |
| status         | VARCHAR(20)   | NO   |     | 'Booked'|                |
+----------------+---------------+------+-----+---------+----------------+

+-----------+-----------+--------------+--------+--------+-------------+--------+
| ticket_id | flight_id | passenger_id | seat_no| price  | booking_date| status |
+-----------+-----------+--------------+--------+--------+-------------+--------+
| 1         | 1         | 1            | 1A     | 350.00 | 2025-11-20  | Booked |
| 2         | 1         | 2            | 1B     | 350.00 | 2025-11-21  | Booked |
| 3         | 2         | 3            | 2A     | 400.00 | 2025-11-22  | Booked |
| 4         | 2         | 4            | 2B     | 400.00 | 2025-11-23  | Cancelled |
| 5         | 3         | 5            | 3A     | 500.00 | 2025-11-24  | Booked |
| 6         | 3         | 6            | 3B     | 500.00 | 2025-11-25  | Booked |
| 7         | 4         | 7            | 4A     | 300.00 | 2025-11-26  | Booked |
| 8         | 4         | 8            | 4B     | 300.00 | 2025-11-27  | Booked |
| 9         | 5         | 9            | 5A     | 450.00 | 2025-11-28  | Booked |
| 10        | 5         | 10           | 5B     | 450.00 | 2025-11-29  | Booked |
| 11        | 6         | 11           | 6A     | 320.00 | 2025-11-30  | Booked |
| 12        | 6         | 12           | 6B     | 320.00 | 2025-12-01  | Booked |
| 13        | 7         | 13           | 7A     | 380.00 | 2025-12-02  | Booked |
| 14        | 7         | 14           | 7B     | 380.00 | 2025-12-03  | Booked |
| 15        | 8         | 15           | 8A     | 420.00 | 2025-12-04  | Cancelled |
| 16        | 8         | 16           | 8B     | 420.00 | 2025-12-05  | Booked |
| 17        | 9         | 17           | 9A     | 500.00 | 2025-12-06  | Booked |
| 18        | 9         | 18           | 9B     | 500.00 | 2025-12-07  | Booked |
| 19        | 10        | 19           | 10A    | 360.00 | 2025-12-07  | Booked |
| 20        | 10        | 20           | 10B    | 360.00 | 2025-12-07  | Booked |
| 21        | 11        | 21           | 11A    | 400.00 | 2025-12-07  | Booked |
| 22        | 11        | 22           | 11B    | 400.00 | 2025-12-07  | Booked |
| 23        | 12        | 23           | 12A    | 420.00 | 2025-12-07  | Booked |
| 24        | 12        | 24           | 12B    | 420.00 | 2025-12-07  | Cancelled |
| 25        | 13        | 25           | 13A    | 450.00 | 2025-12-07  | Booked |
| 26        | 13        | 26           | 13B    | 450.00 | 2025-12-07  | Booked |
| 27        | 14        | 27           | 14A    | 470.00 | 2025-12-07  | Booked |
| 28        | 14        | 28           | 14B    | 470.00 | 2025-12-07  | Booked |
| 29        | 15        | 29           | 15A    | 500.00 | 2025-12-07  | Booked |
| 30        | 15        | 30           | 15B    | 500.00 | 2025-12-07  | Booked |
| 31        | 16        | 31           | 16A    | 350.00 | 2025-12-07  | Booked |
| 32        | 16        | 32           | 16B    | 350.00 | 2025-12-07  | Booked |
| 33        | 17        | 33           | 17A    | 400.00 | 2025-12-07  | Cancelled |
| 34        | 17        | 34           | 17B    | 400.00 | 2025-12-07  | Booked |
| 35        | 18        | 35           | 18A    | 420.00 | 2025-12-07  | Booked |
| 36        | 18        | 36           | 18B    | 420.00 | 2025-12-07  | Booked |
| 37        | 19        | 37           | 19A    | 450.00 | 2025-12-07  | Booked |
| 38        | 19        | 38           | 19B    | 450.00 | 2025-12-07  | Booked |
| 39        | 20        | 39           | 20A    | 500.00 | 2025-12-07  | Booked |
| 40        | 20        | 40           | 20B    | 500.00 | 2025-12-07  | Cancelled |
| 41        | 21        | 41           | 21A    | 360.00 | 2025-12-07  | Booked |
| 42        | 21        | 42           | 21B    | 360.00 | 2025-12-07  | Booked |
| 43        | 22        | 43           | 22A    | 400.00 | 2025-12-07  | Booked |
| 44        | 22        | 44           | 22B    | 400.00 | 2025-12-07  | Booked |
| 45        | 23        | 45           | 23A    | 420.00 | 2025-12-07  | Cancelled |
| 46        | 23        | 46           | 23B    | 420.00 | 2025-12-07  | Booked |
| 47        | 24        | 47           | 24A    | 450.00 | 2025-12-07  | Booked |
| 48        | 24        | 48           | 24B    | 450.00 | 2025-12-07  | Booked |
| 49        | 25        | 49           | 25A    | 500.00 | 2025-12-07  | Booked |
| 50        | 25        | 50           | 25B    | 500.00 | 2025-12-07  | Booked |
+-----------+-----------+--------------+--------+--------+-------------+--------+
```

```sql
CREATE TABLE tickets (
    ticket_id INT NOT NULL AUTO_INCREMENT,
    flight_id INT NOT NULL,
    passenger_id INT NOT NULL,
    seat_no VARCHAR(5) NOT NULL,
    price DECIMAL(8,2) NOT NULL DEFAULT 0.00,
    booking_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Booked',
    PRIMARY KEY (ticket_id),
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id),
    FOREIGN KEY (passenger_id) REFERENCES passengers(passenger_id)
) ENGINE=InnoDB;

INSERT INTO tickets (ticket_id, flight_id, passenger_id, seat_no, price, booking_date, status) VALUES
(1, 1, 1, '1A', 350.00, '2025-11-20', 'Booked'),
(2, 1, 2, '1B', 350.00, '2025-11-21', 'Booked'),
(3, 2, 3, '2A', 400.00, '2025-11-22', 'Booked'),
(4, 2, 4, '2B', 400.00, '2025-11-23', 'Cancelled'),
(5, 3, 5, '3A', 500.00, '2025-11-24', 'Booked'),
(6, 3, 6, '3B', 500.00, '2025-11-25', 'Booked'),
(7, 4, 7, '4A', 300.00, '2025-11-26', 'Booked'),
(8, 4, 8, '4B', 300.00, '2025-11-27', 'Booked'),
(9, 5, 9, '5A', 450.00, '2025-11-28', 'Booked'),
(10, 5, 10, '5B', 450.00, '2025-11-29', 'Booked'),
(11, 6, 11, '6A', 320.00, '2025-11-30', 'Booked'),
(12, 6, 12, '6B', 320.00, '2025-12-01', 'Booked'),
(13, 7, 13, '7A', 380.00, '2025-12-02', 'Booked'),
(14, 7, 14, '7B', 380.00, '2025-12-03', 'Booked'),
(15, 8, 15, '8A', 420.00, '2025-12-04', 'Cancelled'),
(16, 8, 16, '8B', 420.00, '2025-12-05', 'Booked'),
(17, 9, 17, '9A', 500.00, '2025-12-06', 'Booked'),
(18, 9, 18, '9B', 500.00, '2025-12-07', 'Booked'),
(19, 10, 19, '10A', 360.00, '2025-12-07', 'Booked'),
(20, 10, 20, '10B', 360.00, '2025-12-07', 'Booked'),
(21, 11, 21, '11A', 400.00, '2025-12-07', 'Booked'),
(22, 11, 22, '11B', 400.00, '2025-12-07', 'Booked'),
(23, 12, 23, '12A', 420.00, '2025-12-07', 'Booked'),
(24, 12, 24, '12B', 420.00, '2025-12-07', 'Cancelled'),
(25, 13, 25, '13A', 450.00, '2025-12-07', 'Booked'),
(26, 13, 26, '13B', 450.00, '2025-12-07', 'Booked'),
(27, 14, 27, '14A', 470.00, '2025-12-07', 'Booked'),
(28, 14, 28, '14B', 470.00, '2025-12-07', 'Booked'),
(29, 15, 29, '15A', 500.00, '2025-12-07', 'Booked'),
(30, 15, 30, '15B', 500.00, '2025-12-07', 'Booked'),
(31, 16, 31, '16A', 350.00, '2025-12-07', 'Booked'),
(32, 16, 32, '16B', 350.00, '2025-12-07', 'Booked'),
(33, 17, 33, '17A', 400.00, '2025-12-07', 'Cancelled'),
(34, 17, 34, '17B', 400.00, '2025-12-07', 'Booked'),
(35, 18, 35, '18A', 420.00, '2025-12-07', 'Booked'),
(36, 18, 36, '18B', 420.00, '2025-12-07', 'Booked'),
(37, 19, 37, '19A', 450.00, '2025-12-07', 'Booked'),
(38, 19, 38, '19B', 450.00, '2025-12-07', 'Booked'),
(39, 20, 39, '20A', 500.00, '2025-12-07', 'Booked'),
(40, 20, 40, '20B', 500.00, '2025-12-07', 'Cancelled'),
(41, 21, 41, '21A', 360.00, '2025-12-07', 'Booked'),
(42, 21, 42, '21B', 360.00, '2025-12-07', 'Booked'),
(43, 22, 43, '22A', 400.00, '2025-12-07', 'Booked'),
(44, 22, 44, '22B', 400.00, '2025-12-07', 'Booked'),
(45, 23, 45, '23A', 420.00, '2025-12-07', 'Cancelled'),
(46, 23, 46, '23B', 420.00, '2025-12-07', 'Booked'),
(47, 24, 47, '24A', 450.00, '2025-12-07', 'Booked'),
(48, 24, 48, '24B', 450.00, '2025-12-07', 'Booked'),
(49, 25, 49, '25A', 500.00, '2025-12-07', 'Booked'),
(50, 25, 50, '25B', 500.00, '2025-12-07', 'Booked');
```