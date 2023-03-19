# import customtkinter
# from PIL import Image
#
# customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("blue")
#
# screen = customtkinter.CTk()
# screen.geometry("450x450")
# screen.config(padx=50, pady=45)
# screen.title("MORSE CODE CONVERTER")
#
# my_image = customtkinter.CTkImage(light_image=Image.open("morse-code.png"), size=(150,150))
# image_label = customtkinter.CTkLabel(master=screen, image=my_image, text="")
# image_label.grid(column=1, row=0, columnspan=2)
# app_title = customtkinter.CTkLabel(master=screen, text="Encrypt Your Text, Protect Your Secrets!", font=("Degular", 20))
# app_title.grid(column=1, row=1, columnspan=2, pady=20, padx=20)
#
# label_enter_string = customtkinter.CTkLabel(master=screen, text="Text in Human")
# label_enter_string.grid(column=1, row=2)
# string_entry = customtkinter.CTkEntry(master=screen, width=250)
# string_entry.grid(column=2, row=2, padx=15)
# string_entry.focus()
#
#
# label_morse = customtkinter.CTkLabel(master=screen, text="Text in Morse")
# label_morse.grid(column=1, row=3, pady=10)
# morse_entry = customtkinter.CTkEntry(master=screen, width=250)
# morse_entry.grid(column=2, row=3, padx=15)
#
#
# def to_morse(string):
#     morse_entry.delete(0, len(morse_entry.get()))
#     dict_input = [char.title() for char in string]
#     morse_string = ""
#     for char in dict_input:
#         if char in MORSE_CODE_DICT.keys():
#             morse_string += f"{MORSE_CODE_DICT[char]} "
#         elif char == " ":
#             morse_string += " "
#     morse_entry.insert(0, morse_string)
#
#
# def to_human(morse_string):
#     string_entry.delete(0, len(string_entry.get()))
#     morse_list = morse_string.split(" ")
#     og_string = ""
#     for char in morse_list:
#         for key, value in MORSE_CODE_DICT.items():
#             if char == value:
#                 og_string += f"{key}"
#         if char == "":
#             og_string += " "
#     string_entry.insert(0, og_string)
#
#
# frame = customtkinter.CTkFrame(master=screen, width=250,height=50, corner_radius=45, fg_color="transparent")
# frame.grid(column=1, columnspan=2, row=4, pady=10)
#
# button = customtkinter.CTkButton(master=frame, text="To Morse", command= lambda: to_morse(string_entry.get()))
# button.grid(column=1, row=4, padx=10)
# button_2 = customtkinter.CTkButton(master=frame, text="To Human", command= lambda: to_human(morse_entry.get()))
# button_2.grid(column=2, row=4)
#
#
# MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
#                     'C':'-.-.', 'D':'-..', 'E':'.',
#                     'F':'..-.', 'G':'--.', 'H':'....',
#                     'I':'..', 'J':'.---', 'K':'-.-',
#                     'L':'.-..', 'M':'--', 'N':'-.',
#                     'O':'---', 'P':'.--.', 'Q':'--.-',
#                     'R':'.-.', 'S':'...', 'T':'-',
#                     'U':'..-', 'V':'...-', 'W':'.--',
#                     'X':'-..-', 'Y':'-.--', 'Z':'--..',
#                     '1':'.----', '2':'..---', '3':'...--',
#                     '4':'....-', '5':'.....', '6':'-....',
#                     '7':'--...', '8':'---..', '9':'----.',
#                     '0':'-----', ', ':'--..--', '.':'.-.-.-',
#                     '?':'..--..', '/':'-..-.', '-':'-....-',
#                     '(':'-.--.', ')':'-.--.-'}
#
#
#
# screen.mainloop()
