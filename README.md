# MorseCode_Generator
Converts user input to morse code and vise versa. Do you need it? Probably not. Does it exist? Yes.

![morse code](https://user-images.githubusercontent.com/111984273/227352444-6335d2b6-c9c7-40f6-9998-7ebe549d8e68.jpg)


Used a custom Tkinter library to make a modern UI instead of the classic Tkinter Windows 95 style.

Custom Tkinter - courtesy of TomSchimansky, https://github.com/TomSchimansky/CustomTkinter
- Added a SQL Database that stores all input/output of strings and their conversion to morse code.
- Added a Wikipedia's top 100 words scrape which takes those words, converts them into morse code, adds both to a dictionary and acts as the source for a random word generator in the GUI.
