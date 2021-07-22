from tkinter import *
from tkinter import scrolledtext
from gtts import gTTS
from playsound import playsound

#creating window
root = Tk()
root.geometry("300x400")
root.configure(bg='#151515')
root.title("Text to Speech")

#headings and labels in the window
main_title = Label(root, text = 'Text to Speech', font = "arial 15 bold", fg = 'white', bg = '#121212')
entry_title = Label(root, text = 'Enter the Text', font = "arial 10 bold", fg = 'white', bg = '#121212')
text_input = scrolledtext.ScrolledText(root, height = 8, width = 30, padx = 10, pady = 10, wrap = 'word', fg = '#151515', bg = '#A3DDCB')

#functions
def tts():
    message = text_input.get("1.0","end-1c")
    speech = gTTS(message, slow = False)
    speech.save('demo.mp3')
    playsound('demo.mp3')

def Exit():
    root.destroy()

def Reset():
    text_input.delete("1.0","end")

#Buttons
play_button = Button(root, text = "Play", font = 'arial 10 bold', bg = '#FFE3D8', command = tts, width = '4')
reset_button = Button(root, text = "Reset", font = 'arial 10 bold', bg = '#BBBBBB', command = Reset, width = '5')
exit_button = Button(root, text = "Exit", font = 'arial 10 bold',bg = '#E94560', command = Exit, width = '4')

#layout managing
main_title.pack(pady = 10)
entry_title.pack(pady = 10)
text_input.pack(pady = 7)
play_button.pack(pady = 5)
reset_button.pack(pady = 5)
exit_button.pack(pady = 10)

#runs the program
root.mainloop()