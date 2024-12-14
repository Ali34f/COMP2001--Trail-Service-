DROP VIEW IF EXISTS CW2.UserTrailSummary;
GO

CREATE VIEW CW2.UserTrailSummary
AS
    SELECT
        u.Username,
        u.FirstName,
        u.LastName,
        COUNT(t.TrailID) AS TotalTrails,
        AVG(t.Length) AS AverageTrailLength,
        AVG(t.Elevation) AS AverageElevation,
        l.Title AS LocationTitle
    FROM
        CW2.[user] u
        JOIN CW2.trails t ON u.ID = t.UserID
        JOIN CW2.trail_location l ON t.CityID = l.LocationID
    GROUP BY 
        u.Username, u.FirstName, u.LastName, l.Title;
GO

SELECT *
FROM CW2.UserTrailSummary;
