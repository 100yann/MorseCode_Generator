import requests
from bs4 import BeautifulSoup


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


def get_words():
    conn = requests.get('https://en.wikipedia.org/wiki/Most_common_words_in_English')
    soup = BeautifulSoup(conn.content, 'html.parser')
    top100_words = [word.get_text() for word in soup.find_all(class_='extiw')]
    while len(top100_words) >= 101:
        top100_words.pop()

    word_bank = {}
    for word in top100_words:
        word_to_morse = ""
        for char in word:
            word_to_morse += MORSE_CODE_DICT[char.upper()]
            word_to_morse += " "
        word_bank[word] = word_to_morse.strip()
    return word_bank