#!/usr/bin/env python3

# made by : H4Z3

# https://pypi.org/project/twofish/
from twofish import Twofish

help_menu = """
USAGE:
  key twofish [FLAGS] [OPTIONS]

FLAGS:
  -d, --decode   Decrypt input text or file
  -e, --encode   Encrypt input text or file

OPTIONS:
  -i, --inputFile <input file>   Input file to encrypt or decrypt
  -k, --key <key>                Encryption key (1-32 characters)
  -o, --output <output file>     Output file for encrypted or decrypted text
  -t, --text <text>              Input text to encrypt or decrypt (16 bytes)

EXAMPLES:
  key twofish -e -t YELLOWSUBMARINES -k mySecretKey
  key twofish -d -t 27570f92486cff1b8bf056671533864b -k mySecretKey
"""

def encode(args):
    text = args.text
    key = args.key

    # check for valid input
    if text and key:
        # check for valid block & key length
        if len(text.encode('utf-8')) == 16 and len(key) <= 32:
            secret = Twofish(bytes(key.encode('ascii')))
            rawciphertext = secret.encrypt(bytes(text.encode('ascii')))
            ciphertext = rawciphertext.hex()

            output = "Encrypting | {}\nKey | {}\nRaw Ciphertext | {}\nCiphertext | {}".format(
                                text, key, rawciphertext, ciphertext)
            
            # check for output file
            if args.output:
                return [ciphertext, True]

            else:
                return [output, True]
        
        # invalid block & key length error handling
        else:
            if len(text.encode('utf-8')) != 16:
                return ['Error: Invalid Block Length {}, must be 16 bytes'.format(
                                text), False]
            
            elif len(key) > 32:
                return ['Error: Invalid key Length {}, must be 1 to 32 characters long'.format(
                                key), False]

            else:
                return ['Error: Make sure to have a 16 byte block and a key', False]

    # input error handling
    else:
        if text == None and key == None:
            return ['Error: No text or key supplied', False]

        elif text == None and key != None:
            return ['Error: No text supplied', False]
        
        elif key == None and text != None:
            return ['Error: No key supplied', False]

        else:
            return ['Error: Make sure to use a 16 byte string and a key', False]

def decode(args):
    ciphertext = args.text
    key = args.key

    # check for valid input
    if ciphertext and key:
        # check for valid block & key length
        if len(key) <= 32:
            secret = Twofish(bytes(key.encode('ascii')))
            rawciphertext = bytes.fromhex(ciphertext)

            # decode attempt
            try:
                plaintext = secret.decrypt(bytes.fromhex(ciphertext)).decode()

            # decode attempt failure handling
            except:
                plaintext = secret.decrypt(bytes.fromhex(ciphertext))
    
            output = "Decrypting | {}\nRaw Ciphertext | {}\nKey | {}\nPlaintext | {}".format(
                                ciphertext, rawciphertext, key, plaintext)

            # check for output file
            if args.output:
                return [plaintext, True]
        
            else:
                return [output, True]

        # invalid block & key length error handling
        else:
            if len(key) > 32:
                return ['Error: Invalid key Length {}, must be 1 to 32 characters long'.format(
                                key), False]

            else:
                return ['Error: Make sure to have a 16 byte block and a key', False]

    # input error handling
    else:
        if ciphertext == None and key == None:
            return ['Error: No text or key supplied', False]

        elif ciphertext == None and key != None:
            return ['Error: No text supplied', False]

        elif key == None and ciphertext != None:
            return ['Error: No key supplied', False]

        else:
            return ['Error: Make sure to use a 16 byte string and a key', False]

