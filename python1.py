import speech_recognition as sr
import moviepy.editor as mp

input_file = input("Enter the file =")

clip = mp.VideoFileClip(input_file)
clip.audio.write_audiofile(r'converted.wav')

r = sr.Recognizer()

audio_file = sr.AudioFile('converted.wav')

with audio_file as source:
    audio = r.record(source)
    
output = r.recognize_google(audio)

with open('test_file.txt',mode ='w') as file: 
   file.write("Recognized Speech:") 
   file.write("\n") 
   file.write(output) 
   print("ready!")
