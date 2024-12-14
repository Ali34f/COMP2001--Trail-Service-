-- Step 1: Update Foreign Key with ON DELETE CASCADE
ALTER TABLE CW1.trail_point
DROP CONSTRAINT FK__trail_point__TrailID;

ALTER TABLE CW1.trail_point
ADD CONSTRAINT FK__trail_point__TrailID FOREIGN KEY (TrailID)
REFERENCES CW1.trails(TrailID) ON DELETE CASCADE;
GO

-- Step 2: Drop Existing Procedures if They Exist
IF OBJECT_ID('CW1.CreateTrail', 'P') IS NOT NULL
    DROP PROCEDURE CW1.CreateTrail;
IF OBJECT_ID('CW1.ReadTrail', 'P') IS NOT NULL
    DROP PROCEDURE CW1.ReadTrail;
IF OBJECT_ID('CW1.UpdateTrail', 'P') IS NOT NULL
    DROP PROCEDURE CW1.UpdateTrail;
IF OBJECT_ID('CW1.DeleteTrail', 'P') IS NOT NULL
    DROP PROCEDURE CW1.DeleteTrail;
GO

-- Step 3: Define Procedures

-- CreateTrail Procedure
CREATE PROCEDURE CW1.CreateTrail
    @Title VARCHAR(50),
    @Description TEXT,
    @Length SMALLINT,
    @Elevation SMALLINT,
    @RouteType VARCHAR(50),
    @CityID INT,
    @CountyID INT,
    @CountryID INT,
    @UserID INT
AS
BEGIN
    SET NOCOUNT ON;

    -- Validate UserID exists
    IF NOT EXISTS (SELECT 1
    FROM CW1.[user]
    WHERE ID = @UserID)
    BEGIN
        RAISERROR ('Invalid UserID: The user does not exist.', 16, 1);
        RETURN;
    END;

    -- Validate foreign keys for location fields
    IF NOT EXISTS (SELECT 1
    FROM CW1.trail_location
    WHERE LocationID = @CityID)
    BEGIN
        RAISERROR ('Invalid CityID: The city does not exist.', 16, 1);
        RETURN;
    END;

    IF NOT EXISTS (SELECT 1
    FROM CW1.trail_location
    WHERE LocationID = @CountyID)
    BEGIN
        RAISERROR ('Invalid CountyID: The county does not exist.', 16, 1);
        RETURN;
    END;

    IF NOT EXISTS (SELECT 1
    FROM CW1.trail_location
    WHERE LocationID = @CountryID)
    BEGIN
        RAISERROR ('Invalid CountryID: The country does not exist.', 16, 1);
        RETURN;
    END;

    -- Insert the new trail
    INSERT INTO CW1.trails
        (Title, Description, Length, Elevation, RouteType, CityID, CountyID, CountryID, UserID, CreatedAt)
    VALUES
        (@Title, @Description, @Length, @Elevation, @RouteType, @CityID, @CountyID, @CountryID, @UserID, GETDATE());

    PRINT 'Trail created successfully.';
END;
GO

-- ReadTrail Procedure
CREATE PROCEDURE CW1.ReadTrail
    @TrailID INT = NULL,
    @Title VARCHAR(50) = NULL,
    @UserID INT = NULL
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        TrailID,
        Title,
        Description,
        Length,
        Elevation,
        RouteType,
        CityID,
        CountyID,
        CountryID,
        UserID,
        CreatedAt
    FROM CW1.trails
    WHERE
        (@TrailID IS NULL OR TrailID = @TrailID) AND
        (@Title IS NULL OR Title LIKE '%' + @Title + '%') AND
        (@UserID IS NULL OR UserID = @UserID);
END;
GO

-- UpdateTrail Procedure
CREATE PROCEDURE CW1.UpdateTrail
    @TrailID INT,
    @Title VARCHAR(50) = NULL,
    @Description TEXT = NULL,
    @Length SMALLINT = NULL,
    @Elevation SMALLINT = NULL,
    @RouteType VARCHAR(50) = NULL,
    @CityID INT = NULL,
    @CountyID INT = NULL,
    @CountryID INT = NULL,
    @UserID INT = NULL
AS
BEGIN
    SET NOCOUNT ON;

    -- Validate the TrailID exists
    IF NOT EXISTS (SELECT 1
    FROM CW1.trails
    WHERE TrailID = @TrailID)
    BEGIN
        PRINT 'No trail found with the specified TrailID.';
        RETURN;
    END;

    -- Update the trail
    UPDATE CW1.trails
    SET
        Title = COALESCE(@Title, Title),
        Description = COALESCE(@Description, Description),
        Length = COALESCE(@Length, Length),
        Elevation = COALESCE(@Elevation, Elevation),
        RouteType = COALESCE(@RouteType, RouteType),
        CityID = COALESCE(@CityID, CityID),
        CountyID = COALESCE(@CountyID, CountyID),
        CountryID = COALESCE(@CountryID, CountryID),
        UserID = COALESCE(@UserID, UserID)
    WHERE TrailID = @TrailID;

    PRINT 'Trail updated successfully.';
END;
GO

-- DeleteTrail Procedure
CREATE PROCEDURE CW1.DeleteTrail
    @TrailID INT
AS
BEGIN
    SET NOCOUNT ON;

    -- Validate the TrailID exists
    IF NOT EXISTS (SELECT 1
    FROM CW1.trails
    WHERE TrailID = @TrailID)
    BEGIN
        PRINT 'No trail found with the specified TrailID.';
        RETURN;
    END;

    -- Delete the trail
    DELETE FROM CW1.trails
    WHERE TrailID = @TrailID;

    PRINT 'Trail deleted successfully.';
END;
GO

-- Step 4: Testing the Procedures

-- Create a new trail
PRINT 'Executing CreateTrail:';
EXEC CW1.CreateTrail 
    @Title = 'Mountain Trail', 
    @Description = 'A scenic mountain trail.', 
    @Length = 5, 
    @Elevation = 300, 
    @RouteType = 'Loop', 
    @CityID = 1, 
    @CountyID = 2, 
    @CountryID = 3, 
    @UserID = 1;

-- Add points to trail_point
INSERT INTO CW1.trail_point
    (TrailID, Position, Longitude, Latitude)
VALUES
    (1, 1, -118.2437, 34.0522),
    (1, 2, -118.2438, 34.0523),
    (1, 3, -118.2439, 34.0524);

-- Read all trails
PRINT 'Executing ReadTrail:';
EXEC CW1.ReadTrail;

-- Read a specific trail by ID
EXEC CW1.ReadTrail @TrailID = 1;

-- Update the trail details
PRINT 'Executing UpdateTrail:';
EXEC CW1.UpdateTrail 
    @TrailID = 1, 
    @Title = 'Updated Mountain Trail', 
    @Length = 10;

-- Verify the trail was updated
PRINT 'After UpdateTrail:';
SELECT *
FROM CW1.trails;

-- Delete the trail
PRINT 'Executing DeleteTrail:';
EXEC CW1.DeleteTrail @TrailID = 1;

-- Verify deletion
PRINT 'After DeleteTrail:';
SELECT *
FROM CW1.trails;
SELECT *
FROM CW1.trail_point;
GO
