-- Step 1: Update Foreign Key with ON DELETE CASCADE
IF EXISTS (
    SELECT 1
FROM sys.foreign_keys
WHERE name = 'FK__trail_point__TrailID'
)
BEGIN
    ALTER TABLE CW2.trail_point
    DROP CONSTRAINT FK__trail_point__TrailID;
END;
GO

ALTER TABLE CW2.trail_point
ADD CONSTRAINT FK__trail_point__TrailID FOREIGN KEY (TrailID)
REFERENCES CW2.trails(TrailID) ON DELETE CASCADE;
GO

-- Step 2: Drop Existing Procedures if They Exist
IF OBJECT_ID('CW2.CreateTrail', 'P') IS NOT NULL
    DROP PROCEDURE CW2.CreateTrail;
IF OBJECT_ID('CW2.ReadTrail', 'P') IS NOT NULL
    DROP PROCEDURE CW2.ReadTrail;
IF OBJECT_ID('CW2.UpdateTrail', 'P') IS NOT NULL
    DROP PROCEDURE CW2.UpdateTrail;
IF OBJECT_ID('CW2.DeleteTrail', 'P') IS NOT NULL
    DROP PROCEDURE CW2.DeleteTrail;
GO

-- Step 3: Define Procedures

-- CreateTrail Procedure
CREATE PROCEDURE CW2.CreateTrail
    @Trail_name VARCHAR(100),
    @Trail_Summary VARCHAR(500),
    @Trail_Description TEXT,
    @Difficulty VARCHAR(20),
    @Location VARCHAR(150),
    @Length DECIMAL(6,2),
    @Elevation_gain DECIMAL(6,2),
    @Route_type VARCHAR(50),
    @OwnerID INT
AS
BEGIN
    SET NOCOUNT ON;

    -- Validate OwnerID exists
    IF NOT EXISTS (
        SELECT 1
    FROM CW2.[user]
    WHERE UserID = @OwnerID
    )
    BEGIN
        RAISERROR ('Invalid OwnerID: The user does not exist.', 16, 1);
        RETURN;
    END;

    -- Insert the new trail
    INSERT INTO CW2.trails
        (Trail_name, Trail_Summary, Trail_Description, Difficulty, Location, Length, Elevation_gain, Route_type, OwnerID, CreatedAt)
    VALUES
        (@Trail_name, @Trail_Summary, @Trail_Description, @Difficulty, @Location, @Length, @Elevation_gain, @Route_type, @OwnerID, GETDATE());

    PRINT 'Trail created successfully.';
END;
GO

-- ReadTrail Procedure
CREATE PROCEDURE CW2.ReadTrail
    @TrailID INT = NULL,
    @Trail_name VARCHAR(100) = NULL,
    @OwnerID INT = NULL
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        TrailID,
        Trail_name,
        Trail_Summary,
        Trail_Description,
        Difficulty,
        Location,
        Length,
        Elevation_gain,
        Route_type,
        OwnerID,
        CreatedAt
    FROM CW2.trails
    WHERE
        (@TrailID IS NULL OR TrailID = @TrailID) AND
        (@Trail_name IS NULL OR Trail_name LIKE '%' + @Trail_name + '%') AND
        (@OwnerID IS NULL OR OwnerID = @OwnerID);
END;
GO

-- UpdateTrail Procedure
CREATE PROCEDURE CW2.UpdateTrail
    @TrailID INT,
    @Trail_name VARCHAR(100) = NULL,
    @Trail_Summary VARCHAR(500) = NULL,
    @Trail_Description TEXT = NULL,
    @Difficulty VARCHAR(20) = NULL,
    @Location VARCHAR(150) = NULL,
    @Length DECIMAL(6,2) = NULL,
    @Elevation_gain DECIMAL(6,2) = NULL,
    @Route_type VARCHAR(50) = NULL,
    @OwnerID INT = NULL
AS
BEGIN
    SET NOCOUNT ON;

    -- Validate the TrailID exists
    IF NOT EXISTS (
        SELECT 1
    FROM CW2.trails
    WHERE TrailID = @TrailID
    )
    BEGIN
        RAISERROR ('No trail found with the specified TrailID.', 16, 1);
        RETURN;
    END;

    -- Update the trail
    UPDATE CW2.trails
    SET
        Trail_name = COALESCE(@Trail_name, Trail_name),
        Trail_Summary = COALESCE(@Trail_Summary, Trail_Summary),
        Trail_Description = COALESCE(@Trail_Description, Trail_Description),
        Difficulty = COALESCE(@Difficulty, Difficulty),
        Location = COALESCE(@Location, Location),
        Length = COALESCE(@Length, Length),
        Elevation_gain = COALESCE(@Elevation_gain, Elevation_gain),
        Route_type = COALESCE(@Route_type, Route_type),
        OwnerID = COALESCE(@OwnerID, OwnerID)
    WHERE TrailID = @TrailID;

    PRINT 'Trail updated successfully.';
END;
GO

CREATE PROCEDURE CW2.DeleteTrail
    @TrailID INT
AS
BEGIN
    SET NOCOUNT ON;

    -- Validate the TrailID exists
    IF NOT EXISTS (
        SELECT 1
    FROM CW2.trails
    WHERE TrailID = @TrailID
    )
    BEGIN
        RAISERROR ('No trail found with the specified TrailID.', 16, 1);
        RETURN;
    END;

    -- Delete the trail
    DELETE FROM CW2.trails WHERE TrailID = @TrailID;

    PRINT 'Trail deleted successfully.';
END;
GO
