-- Insert into [user] table
INSERT INTO CW2.[user]
    (Email_address, Role)
VALUES
    ('johny28@example.com', 'Hiker'),
    ('shush5@example.com', 'Hiker'),
    ('idris63@example.com', 'Guide'),
    ('sarah99@example.com', 'Hiker'),
    ('rami44a@example.com', 'Guide'),
    ('jerry192d@example.com', 'Admin');

-- Insert into trails table
INSERT INTO CW2.trails
    (Trail_name, Trail_Summary, Trail_Description, Difficulty, Location, Length, Elevation_gain, Route_type, OwnerID, CreatedAt)
VALUES
    ('Plymouth Trail', 'A beautiful hike through the woods', 'Scenic trail with dense forest views', 'Easy', 'Plymouth', 5.00, 120.00, 'Loop', 1, GETDATE()),
    ('Totnes Trail', 'Forest trail ending at a peaceful waterfall', 'Lush green trail with a waterfall at the end', 'Moderate', 'Totnes', 4.50, 150.00, 'Loop', 2, GETDATE()),
    ('Exeter Trail', 'Rocky terrain with desert landscapes', 'Challenging trail with rocky paths', 'Hard', 'Exeter', 6.00, 300.00, 'Out-and-back', 3, GETDATE()),
    ('Paignton Trail', 'Family-friendly walk along a gentle river', 'Gentle trail with picnic spots', 'Easy', 'Paignton', 3.50, 50.00, 'Loop', 4, GETDATE()),
    ('Dawlish Trail', 'Urban trail with city skyline views', 'Urban trail offering views of the city skyline', 'Easy', 'Dawlish', 4.00, 100.00, 'Loop', 5, GETDATE()),
    ('Starcross Trail', 'Mountain trail with wildflower meadows', 'Mountain trail filled with wildflowers', 'Hard', 'Starcross', 7.00, 400.00, 'Out-and-back', 6, GETDATE()),
    ('Teignmouth Trail', 'Historic path with cultural landmarks', 'Trail with historical and cultural landmarks', 'Moderate', 'Teignmouth', 5.00, 200.00, 'Loop', 1, GETDATE());

-- Insert into trail_point table
INSERT INTO CW2.trail_point
    (TrailID, Pt1_Lat, Pt1_Long, Pt1_Desc, Pt2_Lat, Pt2_Long, Pt2_Desc)
VALUES
    (3, 34.052200, -118.243700, 'Starting point at the rocky path', 36.778300, -119.417900, 'Midpoint with desert views'),
    (2, 36.778300, -119.417900, 'Start near the forest entrance', 34.052200, -118.243700, 'Waterfall viewpoint'),
    (1, 50.375500, -4.142700, 'Forest entry point', 50.370000, -4.135000, 'Scenic clearing'),
    (4, 50.435200, -3.567800, 'Gentle riverbank', 50.440000, -3.570000, 'Picnic spot'),
    (5, 51.582500, -2.997800, 'Urban start point', 51.585000, -2.990000, 'City skyline view');

-- Insert into feature table
INSERT INTO CW2.feature
    (Trail_Feature)
VALUES
    ('Waterfall'),
    ('Wildflowers'),
    ('Rocky Path'),
    ('Picnic Spot'),
    ('City View'),
    ('Historical Landmark');

-- Insert into trail_feature table
INSERT INTO CW2.trail_feature
    (TrailID, Trail_FeatureID)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (7, 6);
