import wave
import os
import json
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
import dbConn

def pushDBData(filename,wavFilePath,filesize,chunkPath,wav,transcriptData):
    # get all parameter of audio
    data=wav.getparams()
    
    duration=(round((wav.getnframes()/wav.getframerate()),3))
    #print(duration[0])

    # ensure_ascii=False is added to ensure that non-ASCII characters are not escaped
    jsonData = json.dumps(transcriptData, indent=4, ensure_ascii=False)
    
    details = {
        "filename": filename,
        "wavFilePath": wavFilePath,
        "filesize": filesize,
        "chunkPath": chunkPath,
        "nchannels": data[0],
        "sampwidth": data[1],
        "framerate": data[2],
        "nframes": data[3],
        "duration": duration,
        "jsonData": jsonData
    }
    
    # push data in DB
    dbConn.extractData(**details)
    
    # Save JSON data to a file
    json_filename = f"{os.path.splitext(filename)[0]}.json"
    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json_file.write(jsonData)
    
    return True

def getTranscript(path):
    os.chdir(path)
    
    # Store chunk audio transcript data
    transcriptData={'wavFile':os.path.abspath(path)+'.wav',
              'chunks':[]}

    # Initialize a recognizer object
    recognizer = sr.Recognizer()

    for file in os.listdir(path):
        # Check if the file is a WAV file
        if file.endswith(".wav"):
            # Open the audio file
            with sr.AudioFile(file) as source:
                # Record the audio
                audio = recognizer.record(source)
                try:
                    # Recognize the audio using Google Speech Recognition for Indian Bengali language
                    transcript = recognizer.recognize_google(audio, language="bn-in")
                    # Append the transcript to the chunks list
                    transcriptData['chunks'].append({'chunkFile': os.path.abspath(file), 'text': transcript})
                except sr.UnknownValueError:
                    # If the recognizer couldn't understand the audio
                    pass
                except sr.RequestError:
                    # If there was an error in the request to Google Speech Recognition service
                    pass
    
    # return main directory
    os.chdir('..')
    
    return transcriptData

def splitAudio(audio, filename):
    # Split audio on silence
    chunks = split_on_silence(audio, min_silence_len=1000, silence_thresh=-40)
    
    # Create directory to save chunks if not exists
    os.makedirs(filename.split('.')[0], exist_ok=True)
    
    # Save chunks as WAV files
    for i, chunk in enumerate(chunks):
        chunk.export(f"{filename.split('.')[0]}/{filename.split('.')[0]}_{i+1}.wav", format="wav")
    
    # get chunking folder path
    chunkPath=os.path.abspath(filename.split('.')[0])

    return os.path.abspath(chunkPath)

def loadAudio(path):
    # extract filename from path
    filename=os.path.basename(path)
    
    # get filesize
    filesize=os.path.getsize(path)
    
    # read wav file
    wav=wave.open(path,"rb")
    
    # read audio
    audio=AudioSegment.from_wav(path)
    
    # split audio based on silence
    chunkPath=splitAudio(audio, filename)
    
    # get transcripted data from chukning audio files
    transcriptData=getTranscript(chunkPath)
    
    # get DB data
    pushDBData(filename, path, filesize, chunkPath, wav, transcriptData)
    
    wav.close()
    
    return chunkPath

if __name__=="__main__":
    loadAudio("testBN1.wav")