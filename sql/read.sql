-- Drop existing ReadTrail procedure if it exists
IF OBJECT_ID('CW2.ReadTrail', 'P') IS NOT NULL
    DROP PROCEDURE CW2.ReadTrail;
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