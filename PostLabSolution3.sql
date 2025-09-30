-- ───────────────────────────────────────────────────────────
-- Full Database Setup — Merged from Six Tabs
-- ───────────────────────────────────────────────────────────

-- ========== Section 1: Guide / Customer / Trip ==========

DROP TABLE IF EXISTS TRIP_GUIDES;
DROP TABLE IF EXISTS RESERVATION;
DROP TABLE IF EXISTS TRIP;
DROP TABLE IF EXISTS GUIDE;
DROP TABLE IF EXISTS CUSTOMER;

CREATE TABLE GUIDE (
  GUIDE_NUM   TEXT PRIMARY KEY,
  LAST_NAME   TEXT,
  FIRST_NAME  TEXT,
  ADDRESS     TEXT,
  CITY        TEXT,
  STATE       TEXT,
  POSTAL_CODE TEXT,
  PHONE_NUM   TEXT,
  HIRE_DATE   TEXT
);

CREATE TABLE CUSTOMER (
  CUSTOMER_NUM TEXT PRIMARY KEY,
  LAST_NAME    TEXT NOT NULL,
  FIRST_NAME   TEXT,
  ADDRESS      TEXT,
  CITY         TEXT,
  STATE        TEXT,
  POSTAL_CODE  TEXT,
  PHONE        TEXT
);

CREATE TABLE TRIP (
  TRIP_ID        INTEGER PRIMARY KEY,
  TRIP_NAME      TEXT,
  START_LOCATION TEXT,
  STATE          TEXT,
  DISTANCE       INTEGER,
  MAX_GRP_SIZE   INTEGER,
  TYPE           TEXT,
  SEASON         TEXT
);

INSERT INTO GUIDE VALUES
  ('AM01','Abrams','Miles','54 Quest Ave.','Williamsburg','MA','01096','617-555-6032','2012-06-03'),
  ('BR01','Boyers','Rita','140 Oakton Rd.','Jaffrey','NH','03452','603-555-2134','2012-03-04'),
  ('DH01','Devon','Harley','25 Old Ranch Rd.','Sunderland','MA','01375','781-555-7767','2012-01-08'),
  ('GZ01','Gregory','Zach','7 Moose Head Rd.','Dummer','NH','03588','603-555-8765','2012-11-04'),
  ('KS01','Kiley','Susan','943 Oakton Rd.','Jaffrey','NH','03452','603-555-1230','2013-04-08'),
  ('KS02','Kelly','Sam','9 Congaree Ave.','Fraconia','NH','03580','603-555-0003','2013-06-10'),
  ('MR01','Marston','Ray','24 Shenandoah Rd.','Springfield','MA','01101','781-555-2323','2015-09-14'),
  ('RH01','Rowan','Hal','12 Heather Rd.','Mount Desert','ME','04660','207-555-9009','2014-06-02'),
  ('SL01','Stevens','Lori','15 Riverton Rd.','Coventry','VT','05825','802-555-3339','2014-09-05'),
  ('UG01','Unser','Glory','342 Pineview St.','Danbury','CT','06810','203-555-8534','2015-02-02');

INSERT INTO CUSTOMER VALUES
  ('101','Northfold','Liam','9 Old Mill Rd.','Londonderry','NH','03053','603-555-7563'),
  ('102','Ocean','Arnold','2332 South St. Apt 3','Springfield','MA','01101','413-555-3212'),
  ('103','Kasuma','Sujata','132 Main St. #1','East Hartford','CT','06108','860-555-0703'),
  ('104','Goff','Ryan','164A South Bend Rd.','Lowell','MA','01854','781-555-8423'),
  ('105','McLean','Kyle','345 Lower Ave.','Wolcott','NY','14590','585-555-5321'),
  ('106','Morontoia','Joseph','156 Scholar St.','Johnston','RI','02919','401-555-4848'),
  ('107','Marchand','Quinn','76 Cross Rd.','Bath','NH','03740','603-555-0456'),
  ('108','Rulf','Uschi','32 Sheep Stop St.','Edinboro','PA','16412','814-555-5521'),
  ('109','Caron','Jean Luc','10 Greenfield St.','Rome','ME','04963','207-555-9643'),
  ('110','Bers','Martha','65 Granite St.','York','NY','14592','585-555-0111'),
  ('112','Jones','Laura','373 Highland Ave.','Somerville','MA','02143','857-555-6258'),
  ('115','Vaccari','Adam','1282 Ocean Walk','Ocean CITY','NJ','08226','609-555-5231'),
  ('116','Murakami','Iris','7 Cherry Blossom St.','Weymouth','MA','02188','617-555-6665'),
  ('119','Chau','Clement','18 Ark Ledge Ln.','Londonderry','VT','05148','802-555-3096'),
  ('120','Gernowski','Sadie','24 Stump Rd.','Athens','ME','04912','207-555-4507'),
  ('121','Bretton-Borak','Siam','10 Old Main St.','Cambridge','VT','05444','802-555-3443'),
  ('122','Hefferson','Orlagh','132 South St. Apt 27','Manchester','NH','03101','603-555-3476'),
  ('123','Barnett','Larry','25 Stag Rd.','Fairfield','CT','06824','860-555-9876'),
  ('124','Busa','Karen','12 Foster St.','South Windsor','CT','06074','857-555-5532'),
  ('125','Peterson','Becca','51 Fredrick St.','Albion','NY','14411','585-555-0900'),
  ('126','Brown','Brianne','154 Central St.','Vernon','CT','06066','860-555-3234');

INSERT INTO TRIP VALUES
  (1, 'Arethusa Falls ', 'Harts Location', 'NH', 5, 10, 'Hiking', 'Summer'),
  (2, 'Mt Ascutney - North Peak', 'Weathersfield', 'VT', 5, 6, 'Hiking', 'Late Spring'),
  (3, 'Mt Ascutney - West Peak', 'Weathersfield', 'VT', 6, 10, 'Hiking', 'Early Fall'),
  (4, 'Bradbury Mountain Ride', 'Lewiston-Auburn', 'ME', 25, 8, 'Biking', 'Early Fall'),
  (5, 'Baldpate Mountain ', 'North Newry', 'ME', 6, 10, 'Hiking', 'Late Spring'),
  (6, 'Blueberry Mountain', 'Batchelders Grant', 'ME', 8, 8, 'Hiking', 'Early Fall'),
  (7, 'Bloomfield - Maidstone', 'Bloomfield', 'CT', 10, 6, 'Paddling', 'Late Spring'),
  (8, 'Black Pond', 'Lincoln', 'NH', 8, 12, 'Hiking', 'Summer'),
  (9, 'Big Rock Cave', 'Tamworth', 'NH', 6, 10, 'Hiking', 'Summer'),
  (10, 'Mt. Cardigan - Firescrew', 'Orange', 'NH', 7, 8, 'Hiking', 'Summer'),
  (11, 'Chocorua Lake Tour', 'Tamworth', 'NH', 12, 15, 'Paddling', 'Summer'),
  (12, 'Cadillac Mountain Ride', 'Bar Harbor', 'ME', 8, 16, 'Biking', 'Early Fall'),
  (13, 'Cadillac Mountain', 'Bar Harbor', 'ME', 7, 8, 'Hiking', 'Late Spring'),
  (14, 'Cannon Mtn', 'Franconia', 'NH', 6, 6, 'Hiking', 'Early Fall'),
  (15, 'Crawford Path Presidentials Hike', 'Crawford Notch', 'NH', 16, 4, 'Hiking', 'Summer'),
  (16, 'Cherry Pond', 'Whitefield', 'NH', 6, 16, 'Hiking', 'Spring'),
  (17, 'Huguenot Head Hike', 'Bar Harbor', 'ME', 5, 10, 'Hiking', 'Early Fall'),
  (18, 'Low Bald Spot Hike', 'Pinkam Notch', 'NH', 8, 6, 'Hiking', 'Early Fall'),
  (19, 'Mason''s Farm ', 'North Stratford', 'CT', 12, 7, 'Paddling', 'Late Spring'),
  (20, 'Lake Mephremagog Tour', 'Newport', 'VT', 8, 15, 'Paddling', 'Late Spring'),
  (21, 'Long Pond', 'Rutland', 'MA', 8, 12, 'Hiking', 'Summer'),
  (22, 'Long Pond Tour', 'Greenville', 'ME', 12, 10, 'Paddling', 'Summer'),
  (23, 'Lower Pond Tour', 'Poland', 'ME', 8, 15, 'Paddling', 'Late Spring'),
  (24, 'Mt Adams ', 'Randolph', 'NH', 9, 6, 'Hiking', 'Summer'),
  (25, 'Mount Battie Ride', 'Camden', 'ME', 20, 8, 'Biking', 'Early Fall'),
  (26, 'Mount Cardigan Hike', 'Cardigan', 'NH', 4, 16, 'Hiking', 'Late Fall'),
  (27, 'Mt. Chocorua', 'Albany', 'NH', 6, 10, 'Hiking', 'Spring'),
  (28, 'Mount Garfield Hike', 'Woodstock', 'NH', 5, 10, 'Hiking', 'Early Fall'),
  (29, 'Metacomet-Monadnock Trail Hike', 'Pelham', 'MA', 10, 12, 'Hiking', 'Late Spring'),
  (30, 'McLennan Reservation Hike', 'Tyringham', 'MA', 6, 16, 'Hiking', 'Summer'),
  (31, 'Missisquoi River - VT', 'Lowell', 'VT', 12, 10, 'Paddling', 'Summer'),
  (32, 'Northern Forest Canoe Trail', 'Stark', 'NH', 15, 10, 'Paddling', 'Summer'),
  (33, 'Park Loop Ride', 'Mount Desert Island', 'ME', 27, 8, 'Biking', 'Late Spring'),
  (34, 'Pontook Reservoir Tour', 'Dummer', 'NH', 15, 14, 'Paddling', 'Late Spring'),
  (35, 'Pisgah STATE Park Ride', 'Northborough', 'NH', 12, 10, 'Biking', 'Summer'),
  (36, 'Pondicherry Trail Ride', 'White Mountains', 'NH', 15, 16, 'Biking', 'Late Spring'),
  (37, 'Seal Beach Harbor', 'Bar Harbor', 'ME', 5, 16, 'Hiking', 'Early Spring'),
  (38, 'Sawyer River Ride', 'Mount Carrigain', 'NH', 10, 18, 'Biking', 'Early Fall'),
  (39, 'Welch and Dickey Mountains Hike', 'Thorton', 'NH', 5, 10, 'Hiking', 'Summer'),
  (40, 'Wachusett Mountain', 'Princeton', 'MA', 8, 8, 'Hiking', 'Early Spring'),
  (41, 'Westfield River Loop', 'Fort Fairfield', 'ME', 20, 10, 'Biking', 'Late Spring');

SELECT * FROM GUIDE;
SELECT * FROM CUSTOMER;
SELECT * FROM TRIP;


-- ========== Section 2: Trip_Guides & Reservation ==========

DROP TABLE IF EXISTS TRIP_GUIDES;
DROP TABLE IF EXISTS RESERVATION;

CREATE TABLE TRIP_GUIDES (
  TRIP_ID   INTEGER,
  GUIDE_NUM TEXT,
  PRIMARY KEY (TRIP_ID, GUIDE_NUM)
);

CREATE TABLE RESERVATION (
  RESERVATION_ID TEXT PRIMARY KEY,
  TRIP_ID        INTEGER,
  TRIP_DATE      TEXT,
  NUM_PERSONS    INTEGER,
  TRIP_PRICE     NUMERIC,
  OTHER_FEES     NUMERIC,
  CUSTOMER_NUM   TEXT
);

INSERT INTO TRIP_GUIDES VALUES
  (1,'GZ01'), (1,'RH01'),
  (2,'AM01'), (2,'SL01'),
  (3,'SL01'),
  (4,'BR01'), (4,'GZ01'),
  (5,'KS01'), (5,'UG01'),
  (6,'RH01'),
  (7,'SL01'),
  (8,'BR01'),
  (9,'BR01'),
  (10,'GZ01'),
  (11,'DH01'), (11,'KS01'), (11,'UG01'),
  (12,'BR01'),
  (13,'RH01'),
  (14,'KS02'),
  (15,'GZ01'),
  (16,'KS02'),
  (17,'RH01'),
  (18,'KS02'),
  (19,'DH01'),
  (20,'SL01'),
  (21,'AM01'),
  (22,'UG01'),
  (23,'DH01'), (23,'SL01'),
  (24,'BR01'),
  (25,'BR01'),
  (26,'GZ01'),
  (27,'GZ01'),
  (28,'BR01'),
  (29,'DH01'),
  (30,'AM01'),
  (31,'SL01'),
  (32,'KS01'),
  (33,'UG01'),
  (34,'KS01'),
  (35,'GZ01'),
  (36,'KS02'),
  (37,'RH01'),
  (38,'KS02'),
  (39,'BR01'),
  (40,'DH01'),
  (41,'BR01');

INSERT INTO RESERVATION VALUES
  ('1600001', 40, '2016-03-26', 2,  55.00, 0.00, '101'),
  ('1600002', 21, '2016-06-08', 2,  95.00, 0.00, '101'),
  ('1600003', 28, '2016-09-12', 1,  35.00, 0.00, '103'),
  ('1600004', 26, '2016-10-16', 4,  45.00, 15.00, '104'),
  ('1600005', 39, '2016-06-25', 5,  55.00, 0.00, '105'),
  ('1600006', 32, '2016-06-18', 1,  80.00, 20.00, '106'),
  ('1600007', 22, '2016-07-09', 8,  75.00, 10.00, '107'),
  ('1600008', 28, '2016-09-12', 2,  35.00, 0.00, '108'),
  ('1600009', 38, '2016-09-11', 2,  90.00, 40.00, '109'),
  ('1600010', 2,  '2016-05-14', 3,  25.00, 0.00, '102'),
  ('1600011', 3,  '2016-09-15', 3,  25.00, 0.00, '102'),
  ('1600012', 1,  '2016-06-12', 4,  15.00, 0.00, '115'),
  ('1600013', 8,  '2016-07-09', 1,  20.00, 5.00, '116'),
  ('1600014', 12, '2016-10-01', 2,  40.00, 5.00, '119'),
  ('1600015', 10, '2016-07-23', 1,  20.00, 0.00, '120'),
  ('1600016', 11, '2016-07-23', 6,  75.00, 15.00, '121'),
  ('1600017', 39, '2016-06-18', 3,  20.00, 5.00, '122'),
  ('1600018', 38, '2016-09-18', 4,  85.00, 15.00, '126'),
  ('1600019', 25, '2016-08-29', 2, 110.00, 25.00, '124'),
  ('1600020', 28, '2016-08-27', 2, 35.00, 10.00, '124'),
  ('1600021', 32, '2016-06-11', 3, 90.00, 20.00, '112'),
  ('1600022', 21, '2016-06-08', 1, 95.00, 25.00, '119'),
  ('1600024', 38, '2016-09-11', 1, 70.00, 30.00, '121'),
  ('1600025', 38, '2016-09-11', 2, 70.00, 45.00, '125'),
  ('1600026', 12, '2016-10-01', 2, 40.00, 0.00, '126'),
  ('1600029', 4,  '2016-09-19', 4, 105.00, 25.00, '120'),
  ('1600030', 15, '2016-07-25', 6,  60.00, 15.00, '104');

SELECT * FROM TRIP_GUIDES;
SELECT * FROM RESERVATION;


-- ========== Section 3: Condo / Service ==========

DROP TABLE IF EXISTS SERVICE_REQUEST;
DROP TABLE IF EXISTS SERVICE_CATEGORY;
DROP TABLE IF EXISTS CONDO_UNIT;
DROP TABLE IF EXISTS OWNER;
DROP TABLE IF EXISTS LOCATION;

CREATE TABLE LOCATION (
  LOCATION_NUM INTEGER PRIMARY KEY,
  LOCATION_NAME TEXT,
  ADDRESS       TEXT,
  CITY          TEXT,
  STATE         TEXT,
  POSTAL_CODE   TEXT
);

CREATE TABLE OWNER (
  OWNER_NUM    TEXT PRIMARY KEY,
  LAST_NAME    TEXT,
  FIRST_NAME   TEXT,
  ADDRESS      TEXT,
  CITY         TEXT,
  STATE        TEXT,
  POSTAL_CODE  TEXT
);

CREATE TABLE CONDO_UNIT (
  CONDO_ID     INTEGER PRIMARY KEY,
  LOCATION_NUM INTEGER,
  UNIT_NUM     TEXT,
  SQR_FT       INTEGER,
  BDRMS        INTEGER,
  BATHS        INTEGER,
  CONDO_FEE    NUMERIC,
  OWNER_NUM    TEXT
);

CREATE TABLE SERVICE_CATEGORY (
  CATEGORY_NUM INTEGER PRIMARY KEY,
  CATEGORY_DESCRIPTION TEXT
);

CREATE TABLE SERVICE_REQUEST (
  SERVICE_ID       INTEGER PRIMARY KEY,
  CONDO_ID         INTEGER,
  CATEGORY_NUM     INTEGER,
  DESCRIPTION      TEXT,
  STATUS           TEXT,
  EST_HOURS        NUMERIC,
  SPENT_HOURS      NUMERIC,
  NEXT_SERVICE_DATE TEXT
);

INSERT INTO LOCATION VALUES
  (1, 'Solmaris Ocean', '100 Ocean Ave.', 'Bowton', 'FL', '31313'),
  (2, 'Solmaris Bayside', '405 Bayside Blvd.', 'Glander Bay', 'FL', '31044');

INSERT INTO OWNER VALUES
  ('AD057','Adney','Bruce and Jean','100 Ocean Ave.','Bowton','FL','31313'),
  ('AN175','Anderson','Bill','18 Wilcox St.','Brunswick','GA','31522'),
  ('BL720','Blake','Jack','2672 Condor St.','Mills','SC','29707'),
  ('EL025','Elend','Bill and Sandy','100 Ocean Ave.','Bowton','FL','31313'),
  ('FE182','Feenstra','Daniel','7822 Coventry Dr.','Rivard','FL','31062'),
  ('JU092','Juarez','Maria','892 Oak St.','Kaleva','FL','31521'),
  ('KE122','Kelly','Alyssa','527 Waters St.','Norton','MI','49441'),
  ('NO225','Norton','Peter and Caitlin','281 Lakewood Ave.','Lawndale','PA','19111'),
  ('RO123','Robinson','Mike and Jane','900 Spring Lake Dr.','Springs','MI','49456'),
  ('SM072','Smeltz','Jim and Cathy','922 Garland Dr.','Lewiston','FL','32765'),
  ('TR222','Trent','Michael','405 Bayside Blvd.','Glander Bay','FL','31044'),
  ('WS032','Wilson','Henry and Karen','25 Nichols St.','Lewiston','FL','32765');

INSERT INTO CONDO_UNIT VALUES
  (1,  1, '102',  675, 1, 1, 475.00, 'AD057'),
  (2,  1, '201', 1030, 2, 1, 550.00, 'EL025'),
  (3,  1, '306', 1575, 3, 2, 625.00, 'AN175'),
  (4,  1, '204', 1164, 2, 2, 575.00, 'BL720'),
  (5,  1, '405', 1575, 3, 2, 625.00, 'FE182'),
  (6,  1, '401', 1030, 2, 2, 550.00, 'KE122'),
  (7,  1, '502',  745, 1, 1, 490.00, 'JU092'),
  (8,  1, '503', 1680, 3, 3, 670.00, 'RO123'),
  (9,  2, 'A03',  725, 1, 1, 190.00, 'TR222'),
  (10, 2, 'A01', 1084, 2, 1, 235.00, 'NO225'),
  (11, 2, 'B01', 1084, 2, 2, 250.00, 'SM072'),
  (12, 2, 'C01',  750, 1, 1, 190.00, 'AN175'),
  (13, 2, 'C02', 1245, 2, 2, 250.00, 'WS032'),
  (14, 2, 'C06', 1540, 3, 2, 300.00, 'RO123');

INSERT INTO SERVICE_CATEGORY VALUES
  (1, 'Plumbing'),
  (2, 'Heating/Air Conditioning'),
  (3, 'Painting'),
  (4, 'Electrical Systems'),
  (5, 'Carpentry'),
  (6, 'Janitorial');

INSERT INTO SERVICE_REQUEST VALUES
  (1, 2, 1, 'Back wall in pantry has mold indicating water seepage. Diagnose and repair.',
     'Service rep has verified the problem. Plumbing contractor has been called.', 4, 2, '2015-10-12'),
  (2, 5, 2, 'Air conditioning doesn’t cool.',
     'Service rep has verified problem. Air conditioning contractor has been called.', 3, 1, '2015-10-12'),
  (3, 4, 6, 'Hardwood floors must be refinished.',
     'Service call has been scheduled.', 8, 0, '2015-10-16'),
  (4, 1, 4, 'Switches in kitchen and adjoining dining room are reversed.',
     'Open', 1, 0, '2015-10-13'),
  (5, 2, 5, 'Molding in pantry must be replaced.',
     'Cannot schedule until water leak is corrected.', 2, 0, ''),
  (6,14, 3, 'Unit needs to be repainted due to previous tenant damage.',
     'Scheduled', 7, 0, '2015-10-19'),
  (7,11, 4, 'Tenant complained that using microwave caused short circuits on two occasions.',
     'Service rep unable to duplicate problem. Tenant to notify condo management if problem recurs.', 1, 1, ''),
  (8, 9, 3, 'Kitchen must be repainted. Walls discolored due to kitchen fire.',
     'Scheduled', 5, 0, '2015-10-16'),
  (9, 7, 6, 'Shampoo all carpets.',
     'Open', 5, 0, '2015-10-19'),
  (10,9, 5, 'Repair window sills.',
     'Scheduled', 4, 0, '2015-10-20');

SELECT * FROM LOCATION;
SELECT * FROM OWNER;
SELECT * FROM CONDO_UNIT;
SELECT * FROM SERVICE_CATEGORY;
SELECT * FROM SERVICE_REQUEST;


-- ========== Section 4: Sales – REP / CUSTOMER_TAL ==========

DROP TABLE IF EXISTS ORDER_LINE;
DROP TABLE IF EXISTS ORDERS;
DROP TABLE IF EXISTS ITEM;
DROP TABLE IF EXISTS CUSTOMER_TAL;
DROP TABLE IF EXISTS REP;

CREATE TABLE REP (
  REP_NUM     TEXT PRIMARY KEY,
  LAST_NAME   TEXT,
  FIRST_NAME  TEXT,
  STREET      TEXT,
  CITY        TEXT,
  STATE       TEXT,
  POSTAL_CODE TEXT,
  COMMISSION  NUMERIC,
  RATE        NUMERIC
);

CREATE TABLE CUSTOMER_TAL (
  CUSTOMER_NUM   TEXT PRIMARY KEY,
  CUSTOMER_NAME  TEXT NOT NULL,
  STREET         TEXT,
  CITY           TEXT,
  STATE          TEXT,
  POSTAL_CODE    TEXT,
  BALANCE        NUMERIC,
  CREDIT_LIMIT   NUMERIC,
  REP_NUM        TEXT
);

INSERT INTO REP VALUES
  ('15', 'Campos', 'Rafael', '724 Vinca Dr.', 'Grove', 'CA', '90092', 23457.50, 0.06),
  ('30', 'Gradey', 'Megan', '632 Liatris St.', 'Fullton', 'CA', '90085', 41317.00, 0.08),
  ('45', 'Tian', 'Hui', '1785 Tyler Ave.', 'Northfield', 'CA', '90098', 27789.25, 0.06),
  ('60', 'Sefton','Janet','267 Oakley St.','Congree','CA','90097', 0.00, 0.06);

INSERT INTO CUSTOMER_TAL VALUES
  ('126','Toys Galore','28 Laketon St.','Fullton','CA','90085',1210.25, 7500.00, '15'),
  ('260','Brookings Direct','452 Columbus Dr.','Grove','CA','90092',575.00, 10000.00, '30'),
  ('334','The Everything Shop','342 Magee St.','Congree','CA','90097',2345.75, 7500.00, '45'),
  ('386','Johnson''s Department Store','124 Main St.','Northfield','CA','90098',879.25, 7500.00, '30'),
  ('440','Grove Historical Museum Store','3456 Central Ave.','Fullton','CA','90085',345.00, 5000.00, '45'),
  ('502','Cards and More','167 Hale St.','Mesa','CA','90104',5025.75, 5000.00, '15'),
  ('586','Almondton General Store','3345 Devon Ave.','Almondton','CA','90125',3456.75,15000.00, '45'),
  ('665','Cricket Gift Shop','372 Oxford St.','Grove','CA','90092',678.90, 7500.00, '30'),
  ('713','Cress Store','12 Rising Sun Ave.','Congree','CA','90097',4234.60,10000.00, '15'),
  ('796','Unique Gifts','786 Passmore St.','Northfield','CA','90098',124.75, 7500.00, '45'),
  ('824','Kline''s','945 Gilham St.','Mesa','CA','90104',2475.99,15000.00, '30'),
  ('893','All Season Gifts','382 Wildwood Ave.','Fullton','CA','90085',935.75, 7500.00, '15');

SELECT * FROM REP;
SELECT * FROM CUSTOMER_TAL;


-- ========== Section 5: Sales – ITEM / ORDERS / ORDER_LINE ==========

DROP TABLE IF EXISTS ORDER_LINE;
DROP TABLE IF EXISTS ORDERS;
DROP TABLE IF EXISTS ITEM;

CREATE TABLE ITEM (
  ITEM_NUM    TEXT PRIMARY KEY,
  DESCRIPTION TEXT,
  ON_HAND     INTEGER,
  CATEGORY    TEXT,
  STOREHOUSE  TEXT,
  PRICE       NUMERIC
);

CREATE TABLE ORDERS (
  ORDER_NUM    TEXT PRIMARY KEY,
  ORDER_DATE   TEXT,
  CUSTOMER_NUM TEXT
);

INSERT INTO ITEM VALUES
  ('AH74','Patience',9,'GME','3',22.99),
  ('BR23','Skittles',21,'GME','2',29.99),
  ('CD33','Wood Block Set (48 piece)',36,'TOY','1',89.49),
  ('DL51','Classic Railway Set',12,'TOY','3',107.95),
  ('DR67','Giant Star Brain Teaser',24,'PZL','2',31.95),
  ('DW23','Mancala',40,'GME','3',50.00),
  ('FD11','Rocking Horse',8,'TOY','3',124.95),
  ('FH24','Puzzle Gift Set',65,'PZL','1',38.95),
  ('KA12','Cribbage Set',56,'GME','3',75.00),
  ('KD34','Pentominoes Brain Teaser',60,'PZL','2',14.95),
  ('KL78','Pick Up Sticks',110,'GME','1',10.95),
  ('MT03','Zauberkasten Brain Teaser',45,'PZL','1',45.79),
  ('NL89','Wood Block Set (62 piece)',32,'TOY','3',119.75),
  ('TR40','Tic Tac Toe',75,'GME','2',13.99),
  ('TW35','Fire Engine',30,'TOY','2',118.95);

INSERT INTO ORDERS VALUES
  ('51608','2015-10-12','126'),
  ('51610','2015-10-12','334'),
  ('51613','2015-10-13','386'),
  ('51614','2015-10-13','260'),
  ('51617','2015-10-15','586'),
  ('51619','2015-10-15','126'),
  ('51623','2015-10-15','586'),
  ('51625','2015-10-16','796');

-- Verification selects
SELECT * FROM ITEM;
SELECT * FROM ORDERS;

-- Create and populate ORDER_LINE
DROP TABLE IF EXISTS ORDER_LINE;

CREATE TABLE ORDER_LINE (
  ORDER_NUM    TEXT,
  ITEM_NUM     TEXT,
  NUM_ORDERED  INTEGER,
  QUOTED_PRICE NUMERIC,
  PRIMARY KEY (ORDER_NUM, ITEM_NUM)
);

INSERT INTO ORDER_LINE VALUES
  ('51608','CD33',5,86.99),
  ('51610','KL78',25,10.95),
  ('51610','TR40',10,13.99),
  ('51613','DL51',5,104.95),
  ('51614','FD11',1,124.95),
  ('51617','NL89',4,115.99),
  ('51617','TW35',3,116.95),
  ('51619','FD11',2,121.95),
  ('51623','DR67',5,29.95),
  ('51623','FH24',12,36.95),
  ('51623','KD34',10,13.10),
  ('51625','MT03',8,45.79);

SELECT * FROM ORDER_LINE;

-- ───────────────────────────────────────────────────────────
-- End of Script
-- ───────────────────────────────────────────────────────────
