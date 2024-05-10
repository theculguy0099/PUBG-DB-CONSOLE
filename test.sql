drop database if exists pubg;

create database pubg;

use pubg;

create table Player(
    Player_ID INT(10) PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Date_of_Birth DATE NOT NULL,
    Region VARCHAR(255) NOT NULL,
    Age INT(10) NOT NULL,
    Total_Matches_Played INT(10) DEFAULT 0,
    Rank_Rating INT(10) DEFAULT 0,
    Total_Wins INT(10) DEFAULT 0,
    Win_Rate FLOAT(10) DEFAULT 0,
    Tier VARCHAR(255) DEFAULT "Bronze-III"

);
create table Clans(
    Clan_ID INT(10) PRIMARY KEY,
    Clan_Name VARCHAR(255) NOT NULL,
    ClanLeader_ID INT(10) NOT NULL,
    FOREIGN KEY (ClanLeader_ID) REFERENCES Player(Player_ID) ON UPDATE CASCADE 
);

create table Maps(
    Map_ID INT(10) PRIMARY KEY,
    Map_Name VARCHAR(255) NOT NULL,
    Map_Dimension VARCHAR(255) NOT NULL,
    Terrain VARCHAR(255) NOT NULL
);

create table Matches(
    Match_ID INT(10) PRIMARY KEY,
    Date VARCHAR(255) NOT NULL,
    Number_Of_Teams INT(10) NOT NULL,
    Number_Of_Kills INT(10) DEFAULT 0,
    Winnner_Team_ID INT(10) DEFAULT 0,
    Duration INT(10) DEFAULT 0,
    -- Type VARCHAR(10) NOT NULL,
    Map_ID INT(10) NOT NULL,
    FOREIGN KEY (Map_ID) REFERENCES Maps(Map_ID) ON UPDATE CASCADE 
);

create table Team(

    Team_ID INT(10) PRIMARY KEY,
    Player_ID1 INT(10) NOT NULL,
    Player_ID2 INT(10) NOT NULL,
    Player_ID3 INT(10) NOT NULL,
    Player_ID4 INT(10) NOT NULL,
    Wins INT(10) DEFAULT 0,
    Number_Of_Matches_Played INT(10) DEFAULT 0,
    Win_Rate FLOAT(10) DEFAULT 0,
    Average_Rating INT(10) DEFAULT 0,
    FOREIGN KEY (Player_ID1) REFERENCES Player(Player_ID) ON UPDATE CASCADE ,
    FOREIGN KEY (Player_ID2) REFERENCES Player(Player_ID) ON UPDATE CASCADE ,
    FOREIGN KEY (Player_ID3) REFERENCES Player(Player_ID) ON UPDATE CASCADE ,
    FOREIGN KEY (Player_ID4) REFERENCES Player(Player_ID) ON UPDATE CASCADE 

);

create table MemberOf(

    Player_ID INT(10) PRIMARY KEY,
    Clan_ID INT(10) NOT NULL,
    FOREIGN KEY (Player_ID) REFERENCES Player(Player_ID) ON UPDATE CASCADE ,
    FOREIGN KEY (Clan_ID) REFERENCES Clans(Clan_ID) ON UPDATE CASCADE 
);

create table Kills(
    Player_ID_killer INT(10) NOT NULL,
    Player_ID_killed INT(10) NOT NULL,
    Weapon_ID VARCHAR(10) NOT NULL,
    Match_ID INT(10) NOT NULL,
    PRIMARY KEY(Player_ID_killer,Player_ID_killed,Match_ID),
    FOREIGN KEY (Player_ID_killer) REFERENCES Player(Player_ID) ON UPDATE CASCADE ,
    FOREIGN KEY (Player_ID_killed) REFERENCES Player(Player_ID) ON UPDATE CASCADE ,
    FOREIGN KEY (Match_ID) REFERENCES Matches(Match_ID) ON UPDATE CASCADE 
);

create table Extension(
    Extension_ID INT(10) PRIMARY KEY,
    SCOPE VARCHAR(255) NOT NULL,
    MAG VARCHAR(255) NOT NULL,
    GRIP VARCHAR(255) NOT NULL

);

create table InventoryItem(
    Player_ID INT(10) PRIMARY KEY,
    GunSkin VARCHAR(255),
    VechileSkin VARCHAR(255),
    BackpackSkin VARCHAR(255),
    ClothesSkin VARCHAR(255),
    FOREIGN KEY (Player_ID) REFERENCES Player(Player_ID) ON UPDATE CASCADE 
);


create table MatchDescription(

    Match_ID INT(10) NOT NULL,
    Team_ID INT(10) NOT NULL,
    PRIMARY KEY(Match_ID,Team_ID),
    
    FOREIGN KEY (Match_ID) REFERENCES Matches(Match_ID) ON UPDATE CASCADE ,
    FOREIGN KEY (Team_ID) REFERENCES Team(Team_ID) ON UPDATE CASCADE 
);


create table Weapons(
    Weapon_ID VARCHAR(255) PRIMARY KEY,
    Weapon_Name VARCHAR(255) NOT NULL,
    Ammo FLOAT(10) NOT NULL,
    Fire_Rate INT(10) NOT NULL,
    Damage INT(10) NOT NULL,
    Extension_ID INT(10) NOT NULL,
    FOREIGN KEY (Extension_ID) REFERENCES Extension(Extension_ID) ON UPDATE CASCADE 
);  


create table Plays(
    Match_ID INT(10) NOT NULL,
    Player_ID INT(10) NOT NULL,
    Win_Lose INT(10) NOT NULL,
    Score INT(10) NOT NULL,
    FOREIGN KEY (Player_ID) REFERENCES Player(Player_ID) ON UPDATE CASCADE ,
    FOREIGN KEY (Match_ID) REFERENCES Matches(Match_ID) ON UPDATE CASCADE 
);



-- Insert Players
INSERT INTO Player (Player_ID, Name, Date_of_Birth, Region, Age, Total_Matches_Played, Rank_Rating, Total_Wins, Win_Rate, Tier)
VALUES
(1, 'John Doe', '1990-05-15', 'North America', 31, 20, 1400, 8, 0.40, 'Silver-II'),
(2, 'Jane Smith', '1985-08-22', 'Europe', 36, 25, 1600, 12, 0.48, 'Gold-I'),
(3, 'Alice Johnson', '1995-02-10', 'Asia', 27, 18, 1200, 5, 0.30, 'Bronze-II'),
(4, 'Robert Brown', '1993-07-18', 'South America', 28, 30, 1500, 10, 0.55, 'Gold-III'),
(5, 'Emily White', '1998-03-25', 'Europe', 23, 15, 1100, 4, 0.27, 'Bronze-III'),
(6, 'Michael Turner', '1987-11-02', 'Asia', 36, 22, 1300, 7, 0.35, 'Silver-I'),
(7, 'Sophia Martinez', '1995-09-12', 'North America', 28, 19, 1450, 9, 0.50, 'Gold-II'),
(8, 'Daniel Taylor', '1990-01-30', 'Europe', 32, 27, 1550, 11, 0.52, 'Gold-III'),
(9, 'Olivia Harris', '1999-05-08', 'South America', 24, 14, 1200, 5, 0.29, 'Bronze-II'),
(10, 'William Garcia', '1985-12-15', 'Asia', 38, 33, 1600, 12, 0.48, 'Gold-I'),
(11, 'Ethan Miller', '1996-08-20', 'North America', 27, 29, 1500, 10, 0.55, 'Gold-III'),
(12, 'Ava Anderson', '1991-04-05', 'Europe', 32, 24, 1400, 8, 0.40, 'Silver-II'),
(13, 'Noah Wilson', '1994-02-28', 'Asia', 29, 20, 1300, 7, 0.35, 'Silver-I'),
(14, 'Isabella Moore', '1997-11-15', 'South America', 26, 18, 1200, 5, 0.30, 'Bronze-III'),
(15, 'Liam Jackson', '1989-06-10', 'Europe', 33, 22, 1500, 10, 0.55, 'Gold-II'),
(16, 'Mia Harris', '2000-09-25', 'North America', 21, 15, 1100, 4, 0.27, 'Bronze-III'),
(17, 'James Martinez', '1988-07-02', 'Asia', 34, 28, 1700, 14, 0.60, 'Platinum-I'),
(18, 'Emma Garcia', '1993-01-18', 'South America', 28, 25, 1600, 12, 0.48, 'Gold-I'),
(19, 'Alexander Taylor', '1995-05-03', 'North America', 26, 20, 1450, 9, 0.50, 'Gold-II'),
(20, 'Sophie Johnson', '1992-03-12', 'Asia', 29, 26, 1550, 11, 0.52, 'Gold-III'),
(21, 'Henry Clark', '1997-12-05', 'Europe', 24, 18, 1200, 5, 0.30, 'Bronze-III'),
(22, 'Grace Turner', '1994-09-08', 'South America', 29, 23, 1300, 7, 0.35, 'Silver-I'),
(23, 'Logan Davis', '1991-06-23', 'North America', 32, 19, 1450, 9, 0.50, 'Gold-II'),
(24, 'Chloe White', '1998-04-17', 'Asia', 23, 27, 1550, 11, 0.52, 'Gold-III'),
(25, 'Benjamin Scott', '1986-02-28', 'Europe', 37, 30, 1500, 10, 0.55, 'Gold-II');
-- Add more players as needed...

-- Insert Clans
INSERT INTO Clans (Clan_ID, Clan_Name, ClanLeader_ID)
VALUES
(1, 'Alpha Clan', 1),
(2, 'Bravo Clan', 5),
(3, 'Gamma Clan', 10),
(4, 'Delta Clan', 15),
(5, 'Echo Clan', 20);
-- Add more clans as needed...

INSERT INTO MemberOf (Player_ID, Clan_ID)
VALUES
(1,1),
(5,2),
(10,3),
(15,4),
(20,5);
-- Add more clans as needed...


-- Insert Maps
INSERT INTO Maps (Map_ID, Map_Name, Map_Dimension, Terrain)
VALUES
(1, 'Erangel', '8x8', 'Island'),
(2, 'Miramar', '8x8', 'Desert'),
(3, 'Sanhok', '6x6', 'Forest'),
(4, 'Vikendi', '6x6', 'Snow'),
(5, 'Livik', '2x2', 'Tropical');
-- Add more maps as needed...

-- Insert Extensions
INSERT INTO Extension (Extension_ID, SCOPE, MAG, GRIP)
VALUES
(1, 'Red Dot Sight', 'Extended Mag', 'Angled Grip'),
(2, '4x Scope', 'Quickdraw Mag', 'Vertical Grip'),
(3, 'Holographic Sight', 'Standard Mag', 'Foregrip'),
(4, '8x Scope', 'Extended Mag', 'Bipod Grip'),
(5, '2x Scope', 'Quickdraw Mag', 'Vertical Grip');
-- Add more extensions as needed...

-- Insert Weapons
INSERT INTO Weapons (Weapon_ID, Weapon_Name, Ammo, Fire_Rate, Damage, Extension_ID)
VALUES
('1', 'AKM Rifle', 7.62, 600, 49, 1),
('2', 'M416 Rifle', 5.56, 750, 43, 2),
('3', 'UMP45 Submachine Gun', 9.0, 650, 30, 3),
('4', 'AWM Sniper Rifle', 7.62, 40, 120, 4),
('5', 'P92 Pistol', 9.0, 490, 35, 5);
-- Add more weapons as needed...


-- Insert Teams
INSERT INTO Team (Team_ID, Player_ID1, Player_ID2, Player_ID3, Player_ID4, Wins, Number_Of_Matches_Played, Win_Rate, Average_Rating)
VALUES
(1, 1, 2, 3, 4, 5, 10, 0.50, 1550),
(2, 5, 8, 12, 15, 8, 15, 0.53, 1600),
(3, 3, 6, 9, 11, 12, 20, 0.60, 1450),
(4, 7, 10, 13, 18, 10, 18, 0.55, 1500),
(5, 2, 4, 6, 8, 7, 12, 0.58, 1580);
-- Add more teams as needed...






