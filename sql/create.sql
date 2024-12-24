-- Drop existing CreateTrail procedure if it exists
IF OBJECT_ID('CW2.CreateTrail', 'P') IS NOT NULL
    DROP PROCEDURE CW2.CreateTrail;
GO

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
