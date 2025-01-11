-- Drop existing DeleteTrail procedure if it exists
IF OBJECT_ID('CW2.DeleteTrail', 'P') IS NOT NULL
    DROP PROCEDURE CW2.DeleteTrail;
GO

-- DeleteTrail Procedure
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