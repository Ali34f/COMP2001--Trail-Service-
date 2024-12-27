-- Test Script for Procedures: testing_procedures.sql
-- This script tests the Create, Read, Update, and Delete procedures

-- Step 1: Test CreateTrail Procedure
PRINT 'Testing CreateTrail Procedure...';
EXEC CW2.CreateTrail
    @Trail_name = 'Test Trail',
    @Trail_Summary = 'Summary for Test Trail',
    @Trail_Description = 'Description for Test Trail',
    @Difficulty = 'Moderate',
    @Location = 'Test Location',
    @Length = 3.5,
    @Elevation_gain = 200,
    @Route_type = 'Loop',
    @OwnerID = 1; -- Ensure this OwnerID exists in your database
GO

-- Step 2: Declare, Set, and Use @TestTrailID in the Same Batch
BEGIN
    PRINT 'Fetching TrailID for created Test Trail...';
    DECLARE @TestTrailID INT;
    SELECT @TestTrailID = MAX(TrailID)
    FROM CW2.trails
    WHERE Trail_name = 'Test Trail';
    PRINT 'Test TrailID fetched: ' + CAST(@TestTrailID AS VARCHAR);

    -- Step 3: Test ReadTrail Procedure
    PRINT 'Testing ReadTrail Procedure...';
    EXEC CW2.ReadTrail @TrailID = @TestTrailID;
    -- Fetch the specific trail
    EXEC CW2.ReadTrail @Trail_name = 'Test';
    -- Fetch trails containing 'Test' in the name
    EXEC CW2.ReadTrail @OwnerID = 1;
    -- Fetch trails owned by user with ID = 1

    -- Step 4: Test UpdateTrail Procedure
    PRINT 'Testing UpdateTrail Procedure...';
    EXEC CW2.UpdateTrail 
        @TrailID = @TestTrailID,
        @Trail_name = 'Updated Test Trail Name';

    -- Step 5: Verify UpdateTrail
    PRINT 'Verifying UpdateTrail...';
    SELECT *
    FROM CW2.trails
    WHERE TrailID = @TestTrailID;

    -- Step 6: Test DeleteTrail Procedure
    PRINT 'Testing DeleteTrail Procedure...';
    EXEC CW2.DeleteTrail @TrailID = @TestTrailID;

    -- Step 7: Verify DeleteTrail
    PRINT 'Verifying DeleteTrail...';
    SELECT *
    FROM CW2.trails
    WHERE TrailID = @TestTrailID;
END;
GO