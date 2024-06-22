/*
CREATE TABLE AudioDetails (
    job_id NVARCHAR(255) PRIMARY KEY,
    fileName NVARCHAR(max),
	wavFilePath NVARCHAR(max),
	fileSize BIGINT,
	chunkPath NVARCHAR(max),
    nChannels INT,
    sampWidth INT,
    framerate INT,
    nFrames INT,
    duration FLOAT,
    jsonData NVARCHAR(max)
)
*/

/*
CREATE PROCEDURE InsertAudioDetails
    @job_id NVARCHAR(255),
    @fileName NVARCHAR(max),
    @wavFilePath NVARCHAR(max),
    @fileSize BIGINT,
    @chunkPath NVARCHAR(max),
    @nChannels INT,
    @sampWidth INT,
    @framerate INT,
    @nFrames INT,
    @duration FLOAT,
    @jsonData NVARCHAR(max)
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO AudioDetails (job_id, fileName, wavFilePath, fileSize, chunkPath, nChannels, sampWidth, framerate, nFrames, duration, jsonData)
    VALUES (@job_id, @fileName, @wavFilePath, @fileSize, @chunkPath, @nChannels, @sampWidth, @framerate, @nFrames, @duration, @jsonData);
END;
*/

/*
drop procedure InsertAudioDetails;
*/

/*
drop table AudioDetails;
*/


select * from demodb1.dbo.AudioDetails;
