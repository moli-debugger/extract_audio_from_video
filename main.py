


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, I am {name} this code is all about extracting audiio from a video source')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('mohamed ali')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import speech_recognition as sr
import moviepy.editor as mp
video = mp.VideoFileClip(r"C:\Users\Binary\Downloads\funvideo.mp4 ")
video.audio.write_audiofile("Extracted_audio.wav")

r=sr.Recognizer()
audio=sr.AudioFile("Extracted_audio.wav")
with audio as source:
    audio_file=r.record(source)

final = r.recognize_google(audio_file)
with open("Final_Extracted_audio.txt" ,mode='w') as File:
    File.write("the below lines are text format of Extracted audio:")
    File.write("\n")
    File.write("final")
    print("...ready...")
