DROP TRIGGER IF EXISTS CW2.AfterCommentInsert;
GO

CREATE TABLE CW2.comment_log
(
    CommentID INT,
    UserID INT,
    TrailID INT,
    CommentText VARCHAR(MAX),
    Timestamp DATETIME
);

CREATE TRIGGER CW2.AfterCommentInsert
ON CW2.comment
AFTER INSERT
AS
BEGIN
    INSERT INTO CW2.comment_log
        (CommentID, UserID, TrailID, CommentText, Timestamp)
    SELECT
        CommentID,
        UserID,
        TrailID,
        CommentText,
        GETDATE()
    FROM inserted;
END;
GO
