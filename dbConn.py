import pyodbc
from datetime import datetime

def connection():
    # Connection details
    server = 'LAPTOP-G46LLVV6\JARVIS'
    database = 'demodb1'
    username = 'jarvis'
    password = 'jarvis@17'
    
    # Create connection string
    connStr = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password};'
    )
    
    return connStr

def generateUID():
    currDT = datetime.now()
    uid = currDT.strftime(r"%Y%m%d%H%M%S%f")[:-2]
    return uid

def executeProcedure(procedureName, *params):
    try:
        conn = pyodbc.connect(connection())
        cursor = conn.cursor()
        cursor.execute(f"EXEC {procedureName} " + ", ".join(["?"] * len(params)), params)
        conn.commit()
        conn.close()
        print("Done")
        return 
    except pyodbc.Error as e:
        print(e)
        return f'Error executing query: {e}'

def extractData(filename, wavFilePath, filesize, chunkPath, nchannels, sampwidth, framerate, nframes, duration, jsonData):
    try:
        uid = generateUID()
        # Insert data into DB
        result = executeProcedure('InsertAudioDetails', uid, filename, wavFilePath, filesize, chunkPath, nchannels, sampwidth, framerate, nframes, duration, jsonData)
        return result
    except Exception as e:
        return f"Error: {e}"