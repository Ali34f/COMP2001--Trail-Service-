DROP TRIGGER IF EXISTS CW2.AfterTrailInsert;
GO

CREATE TRIGGER CW2.AfterTrailInsert
ON CW2.trails
AFTER INSERT
AS
BEGIN
    INSERT INTO CW2.trail_log
        (TrailID, Trail_name, Trail_Summary, Trail_Description, Difficulty, Location, Length, Elevation_gain, Route_type, OwnerID, CreatedAt, LogTimestamp)
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
        CreatedAt,
        GETDATE()
    -- Log timestamp
    FROM inserted;
END;
GO