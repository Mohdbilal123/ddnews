# Import necessary libraries:
import pyttsx3
import PyPDF2

# Read the file in binary mode:
book=open(r"F:\SnapTube Video\BOOKS\The-Alchemist(1).pdf", "rb")

# Create aPdfFileReader object:
pdfreader=PyPDF2.PdfFileReader(book)

# To determine total number of pages in the PDF file:
pages=pdfreader.numPages

# Initialize the player:
# Here, init() function is used to get a reference to a pyttsx3. Engine instance
player = pyttsx3.init()

# To access voice property of the player:
voices=player.getProperty('voices')

vo=int(input("enter '0' for male and '1' for female"))
player.setProperty('voice',voices[vo].id)
rate=player.getProperty('rate')
rt=int(input("enter player's rate"))
player.setProperty('rate',rt)
volume=player.getProperty('volume')
vol=float(input("enter player's volume"))
player.setProperty('volume',vol)
print("Total number of pages in file are", pages)

# Iterate through the pages you want to access
# For accessing specific pages: Iterate through the corresponding page indices
# Note: Index of first page-> 0
# Here, entire PDF is accessed:
for num in range(pages):
    # To read current page index:
    page=pdfreader.getPage(num)
    # To extract the text present in current page:
    text = page.extractText()
    # say() function takes a string as the parameter and then queues the same to be converted from text-to-speech
    player.say(text)
    # runAndWait() function blocks the player instance until all the currently queued commands are processed
    player.runAndWait()

# To save the audio output as a MP3 file, within this project:
# Make use of any MP3 player to access this recording whenever required
player.save_to_file(text,'audio.mp3')
player.runAndWait()

"""import pyttsx3
import PyPDF2
from tkinter.filedialog import*
book=askopenfilename()
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
for num in range(pages):
    page=pdfreader.getPage(num)
    text=page.extractText()
    player=pyttsx3.init()
    player.say(text)
    player.runAndWait()

 #Initialize the player
    rate=player.getProperty('rate')
    print(rate)
    player.setProperty('rate',125)
    voices=player.getProperty('voices')
    print(voices)

    #changing index, changes
    voices, 0 for male
    player.setProperty('voice',voices[0].id)

    #changing index, changes
    voices, 1 for female
    player.setProperty('voice',voices[1].id)

    volume=player.getProperty('volume')
    print(volume)
    player.setProperty('volume',1.0)

    player.save_to_file(text,'audio.mp3')
    player.runAndWait()"""