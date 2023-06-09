import customtkinter
from PIL import Image
from sql import DB
from top100_words import get_words
import random


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Create Tkinter Screen
screen = customtkinter.CTk()
screen.geometry("450x450")
screen.config(padx=50, pady=45)
screen.title("MORSE CODE CONVERTER")

# Load a custom image and title
my_image = customtkinter.CTkImage(light_image=Image.open("morse-code.png"), size=(150,150))
image_label = customtkinter.CTkLabel(master=screen, image=my_image, text="")
image_label.grid(column=1, row=0, columnspan=2)
app_title = customtkinter.CTkLabel(master=screen, text="Encrypt Your Text, Protect Your Secrets!", font=("Degular", 20))
app_title.grid(column=1, row=1, columnspan=2, pady=20, padx=20)

# String Field
label_enter_string = customtkinter.CTkLabel(master=screen, text="Text in Human")
label_enter_string.grid(column=1, row=2)
string_entry = customtkinter.CTkEntry(master=screen, width=250)
string_entry.grid(column=2, row=2, padx=15)
string_entry.focus()


# Morse Field
label_morse = customtkinter.CTkLabel(master=screen, text="Text in Morse")
label_morse.grid(column=1, row=3, pady=10)
morse_entry = customtkinter.CTkEntry(master=screen, width=250)
morse_entry.grid(column=2, row=3, padx=15)


# Load DB
db = DB()

def to_morse(string):
    if len(string_entry.get()) > 0:
        # Converts the string input into morse code
        morse_entry.delete(0, len(morse_entry.get()))
        dict_input = [char.title() for char in string]
        morse_string = ""
        for char in dict_input:
            if char in MORSE_CODE_DICT.keys():
                morse_string += f"{MORSE_CODE_DICT[char]} "
            elif char == " ":
                morse_string += " " # Retains spacing 
        morse_entry.insert(0, morse_string)
        # log the input/output to the db
        db.log_input(string, morse_string)


def to_human(morse_string):
    # Convert morse code back to readable text, 
    # since morse code doesn't retain capitalization the string is returned as if the program is yelling at you (all caps)
    if len(morse_entry.get()) > 0:
        string_entry.delete(0, len(string_entry.get()))
        morse_list = morse_string.split(" ")
        og_string = ""
        for char in morse_list:
            for key, value in MORSE_CODE_DICT.items():
                if char == value:
                    og_string += f"{key}"
            if char == "":
                og_string += " "
        string_entry.insert(0, og_string)
        db.log_input(og_string, morse_string)


def random_word():
    string_entry.delete(0, len(string_entry.get()))
    morse_entry.delete(0, len(morse_entry.get()))
    rand_word, rand_morse = random.choice(list(get_words().items()))
    string_entry.insert(0, rand_word)
    morse_entry.insert(0, rand_morse)


frame = customtkinter.CTkFrame(master=screen, width=250,height=50, corner_radius=45, fg_color="transparent")
frame.grid(column=1, columnspan=2, row=4, pady=10)

input_text = customtkinter.CTkButton(master=frame, 
                                 text="To Morse",
                                 width=110,
                                 command= lambda: to_morse(string_entry.get()))
input_text.grid(column=1, row=4, padx=10)

input_morse = customtkinter.CTkButton(master=frame, 
                                   text="To Human",
                                   width=110,
                                   command= lambda: to_human(morse_entry.get()))
input_morse.grid(column=2, row=4)

get_random_word = customtkinter.CTkButton(master=frame, 
                                   text="Random", 
                                   width=30,
                                   command=random_word)
get_random_word.grid(column=3, row=4, padx=10)

screen.mainloop()
# db.delete_data()
