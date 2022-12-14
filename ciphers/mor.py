#!/usr/bin/python

# morsecode cipher [encoding] package for the the codex project
# created by : Fyzz

# help menu for cipheringing process
help_menu = """
USAGE:
  key mor [FLAGS] [OPTIONS]

FLAGS:
  -d, --decode  Decrypt input text or file
  -e, --encode  Encrypt input text or file

OPTIONS:
  -i, --inputFile <input file>   Input file to encrypt or decrypt
  -o, --output <output file>     Output file for encrypted or decrypted text
  -t, --text <text>              Input text to encrypt or decrypt

EXAMPLES:
  key mor -e -t hello
"""

morseAlphabet ={
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        " " : "/"
        }

inverseMorseAlphabet = dict((v,k) for (k,v) in morseAlphabet.items())

# encode morse
def encode(input):
    text = input.text.upper()
    output = []

    for character in text:
        if character in morseAlphabet:
            output.append(morseAlphabet[character])
        else:
            output.append(character)
    
    return [" ".join(output), True]

# decode morse
def decode(input):
    text = input.text.split(" ")
    output = ''

    for character in text:
        if character in inverseMorseAlphabet:
            output += inverseMorseAlphabet[character]
        else:
            output += character

    return [output.capitalize(), True]
