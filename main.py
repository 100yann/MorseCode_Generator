import customtkinter
from PIL import Image
import sqlalchemy
from sqlalchemy import create_engine, text

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


# Create SQLAlchemy engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# Create a temporary db for this instance, needs to be a specific db
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE morse_db (Original_Input, Morse_Code)"))
    conn.commit()

def log_input(string, morse):
    #store the original input and morse code into the temporary db
    with engine.connect() as conn:
        conn.execute(text("INSERT INTO morse_db (Original_Input, Morse_Code) VALUES (:Original_Input, :Morse_Code)"),
                    [{"Original_Input": string, "Morse_Code": morse}]
        )
        conn.commit()
    results()


def results():
    # shows if the original input and morse code were logged in properly
    with engine.connect() as conn:
        result = conn.execute(text("SELECT Original_Input, Morse_Code FROM morse_db"))
        for row in result:
            print(f"x: {row.Original_Input}  y: {row.Morse_Code}")


def to_morse(string):
  
    # Converts the string input into morse code
    morse_entry.delete(0, len(morse_entry.get()))
    dict_input = [char.title() for char in string]
    morse_string = ""
    for char in dict_input:
        if char in MORSE_CODE_DICT.keys():
            morse_string += f"{MORSE_CODE_DICT[char]} "
        elif char == " ":
            morse_string += " " #Retains spacing 
    morse_entry.insert(0, morse_string)
    log_input(string, morse_string)


def to_human(morse_string):
    # Convert morse code back to readable text, 
    # since morse code doesn't retain capitalization the string is returned as if the program is yelling at you (all caps)
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


frame = customtkinter.CTkFrame(master=screen, width=250,height=50, corner_radius=45, fg_color="transparent")
frame.grid(column=1, columnspan=2, row=4, pady=10)

button = customtkinter.CTkButton(master=frame, text="To Morse", command= lambda: to_morse(string_entry.get()))
button.grid(column=1, row=4, padx=10)
button_2 = customtkinter.CTkButton(master=frame, text="To Human", command= lambda: to_human(morse_entry.get()))
button_2.grid(column=2, row=4)


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



screen.mainloop()

# Added a temporary DB that stores the input and morse code generated in this instance of the code, need to
# connect to a permanent db that stores the information, not one that creates a new db table on each 
# instance of the code. I would also work on separating the functionality into different files
