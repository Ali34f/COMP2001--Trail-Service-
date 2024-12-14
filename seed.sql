-- Insert into [user] table
INSERT INTO CW2.[user]
    (Username, FirstName, LastName, [Password])
VALUES
    ('johny28', 'John', 'Smith', 'password'),
    ('Shush5', 'Shush', 'Wallah', 'Popcorn890'),
    ('Idris63', 'Idris', 'Ali', 'Genz2024'),
    ('Sarah99', 'Sarah', 'Carrington', 'Central888'),
    ('Rami44a', 'Rami', 'Khan', 'bookybee156'),
    ('Jerry192d', 'Bob', 'Baker', 'password');

-- Insert into trail_location table
INSERT INTO CW2.trail_location
    (Title)
VALUES
    ('Plymouth'),
    ('Exeter'),
    ('Paignton'),
    ('Torquay'),
    ('Teignmouth'),
    ('Dawlish'),
    ('Starcross'),
    ('Totnes');

-- Insert into trails table
INSERT INTO CW2.trails
    (Title, Description, Length, Elevation, RouteType, CityID, CountyID, CountryID, UserID)
VALUES
    ('Plymouth Trail', 'A beautiful hike through the woods', 5, 1200, 'Loop out-and-back', 1, 6, 3, 1),
    ('Totnes Trail', 'Forest trail ending at a peaceful waterfall.', 5, 1200, 'Loop out-and-back', 2, 2, 3, 2),
    ('Exeter Trail', 'Rocky terrain with desert landscapes', 5, 1200, 'Loop out-and-back', 3, 5, 3, 3),
    ('Paignton Trail', 'Family-friendly walk along a gentle river with picnic spots', 5, 1200, 'Loop out-and-back', 4, 2, 3, 4),
    ('Dawlish Trail', 'Urban trail with city skyline views', 5, 1200, 'Loop out-and-back', 5, 2, 4, 5),
    ('Starcross Trail', 'Mountain trail with wildflower meadows', 5, 1200, 'Loop out-and-back', 6, 2, 3, 6),
    ('Teignmouth Trail', 'Historic path with cultural landmarks', 5, 1200, 'Loop out-and-back', 7, 2, 3, 1);

-- Insert into trail_point table
INSERT INTO CW2.trail_point
    (Position, Latitude, Longitude, TrailID)
VALUES
    (1, 34.0522, -118.2437, 3),
    (2, 36.7783, -119.4179, 3),
    (3, 34.0522, -118.2437, 3),
    (1, 36.7783, -119.4179, 2),
    (2, 34.0522, -118.2437, 2),
    (3, 36.7783, -119.4179, 2),
    (4, 34.0522, -118.2437, 2);

-- Insert into comment table
INSERT INTO CW2.comment
    (UserID, TrailID, CommentText)
VALUES
    (1, 2, 'Nice trail! The views were amazing'),
    (1, 2, 'Nice trail! The views were stunning'),
    (1, 2, 'Nice trail! The views were outstanding'),
    (1, 2, 'Nice trail! The views were mindblowing'),
    (1, 2, 'Nice trail! The views were very bright'),
    (1, 2, 'Nice trail! The views were spectacular');
