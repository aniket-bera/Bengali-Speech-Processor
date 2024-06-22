# Bengali-Speech-Processor

Bengali-Speech-Processor is a Python-based project designed to process audio files in Bengali. It splits the audio into chunks based on silence, transcribes the chunks using Google Speech Recognition for Indian Bengali, and saves the transcriptions along with audio metadata into a database. The transcription data is also saved in a JSON file.

## Features

- Splits audio files based on silence.
- Transcribes audio chunks using Google Speech Recognition.
- Saves transcription data and audio metadata to a database.
- Saves transcription data to a JSON file.

## Getting Started

### Prerequisites

- Python 3.x
- pydub library
- speech_recognition library
- pyodbc library
- Microsoft ODBC Driver 17 for SQL Server

### Installation

1. Install the required Python packages:
    ```bash
    pip install pydub speechrecognition pyodbc
    ```

2. Ensure you have FFmpeg installed (required by pydub):
    - For Windows: Download and install FFmpeg from [FFmpeg Download](https://ffmpeg.org/download.html).

### Usage

1. Prepare your audio file and place it in the project directory.

2. Update the database connection details in `dbConn.py` to match your SQL Server setup.

3. Run the script with your audio file as an argument:
    ```bash
    python main.py path/to/your/audiofile.wav
    ```

### File Descriptions

- `getAudioData.py`: Contains functions to process the audio file, split it into chunks, transcribe the chunks, and push the data to the database.
- `dbConn.py`: Handles the database connection and operations.
- `main.py`: Entry point of the application which invokes the processing on the given audio file.
- `AudioDetails.sql`: SQL script to create the `AudioDetails` table and `InsertAudioDetails` stored procedure.

### Database

The project uses a SQL Server database. Execute the SQL script in `AudioDetails.sql` to create the required table and stored procedure.

#### Example Table and Procedure Creation Script

```sql
-- Table Creation for 'AudioDetails'
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
);

-- Procedure Creation for 'InsertAudioDetails'
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
```

### Contact

For any questions or suggestions, please reach out to [aniketbera.ab@gmail.com](mailto:aniketbera.ab@gmail.com).

---

Thank you for using Bengali-Speech-Processor! We hope it helps you process and transcribe your Bengali audio data effectively.
