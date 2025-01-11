-- Drop existing UpdateTrail procedure if it exists
IF OBJECT_ID('CW2.UpdateTrail', 'P') IS NOT NULL
    DROP PROCEDURE CW2.UpdateTrail;
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