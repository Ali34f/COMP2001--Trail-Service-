
CREATE SCHEMA CW2;
GO

DROP TABLE IF EXISTS CW2.[user];
DROP TABLE IF EXISTS CW2.trail_location;
DROP TABLE IF EXISTS CW2.trails;
DROP TABLE IF EXISTS CW2.trail_point;
DROP TABLE IF EXISTS CW2.comment;

CREATE TABLE CW2.[user]
(
    Username VARCHAR(10) NOT NULL CHECK(LEN(Username) >= 3),
    FirstName VARCHAR(40),
    LastName VARCHAR(40),
    Password TEXT NOT NULL,
    CreatedAt DATETIME NOT NULL DEFAULT GETDATE(),
    ID INT PRIMARY KEY IDENTITY (1,1)
);




CREATE TABLE CW2.trail_location
(
    LocationID INT PRIMARY KEY IDENTITY,
    Title VARCHAR(50) NOT NULL
);

CREATE TABLE CW2.trails
(
    TrailID INT PRIMARY KEY IDENTITY (1,1),
    Title VARCHAR(50) NOT NULL,
    Description TEXT NOT NULL,
    Length SMALLINT NOT NULL,
    Elevation SMALLINT NOT NULL,
    RouteType VARCHAR(50) NOT NULL,
    CityID INT NOT NULL REFERENCES CW2.trail_location(LocationID),
    CountyID INT NOT NULL REFERENCES CW2.trail_location(LocationID),
    CountryID INT NOT NULL REFERENCES CW2.trail_location(LocationID),
    UserID INT NOT NULL REFERENCES CW2.[user](ID),
    -- Corrected to reference CW2.[user]
    CreatedAt DATETIME NOT NULL DEFAULT GETDATE()
);

CREATE TABLE CW2.trail_point
(
    TrailID INT REFERENCES CW2.trails(TrailID),
    Position SMALLINT NOT NULL CHECK(Position > 0),
    Longitude REAL NOT NULL CHECK(Longitude >= -180.0 AND Longitude <= 180),
    Latitude REAL NOT NULL CHECK(Latitude >= -90.0 AND Latitude <= 90),
    PRIMARY KEY (TrailID, Position)
);

CREATE TABLE CW2.comment
(
    CommentID INT PRIMARY KEY IDENTITY (1,1),
    UserID INT NOT NULL REFERENCES CW2.[user](ID),
    -- Corrected to reference CW2.[user]
    TrailID INT NOT NULL REFERENCES CW2.trails(TrailID),
    CommentText TEXT NOT NULL
);
