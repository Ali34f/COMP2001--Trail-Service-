DROP VIEW IF EXISTS CW2.UserTrailSummary;
GO

CREATE VIEW CW2.UserTrailSummary
AS
    SELECT
        u.Email_address AS UserEmail,
        u.Role AS UserRole,
        COUNT(t.TrailID) AS TotalTrails,
        AVG(t.Length) AS AverageTrailLength,
        AVG(t.Elevation_gain) AS AverageElevationGain,
        t.Location AS TrailLocation
    FROM
        CW2.[user] u
        JOIN CW2.trails t ON u.UserID = t.OwnerID
    GROUP BY 
        u.Email_address, u.Role, t.Location;
GO

SELECT *
FROM CW2.UserTrailSummary;