import argparse

from argparse import Namespace

import sys

from  vigenere import *


def parser_create() -> Namespace:
    """
    Parser

    :return: Parsed arguments
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('input_text', type=str, help='Name of input text file')
    parser.add_argument('output_text', type=str, help='Name of output text file')
    parser.add_argument('key_filename', type=str, help='Filename containing the key')

    return parser.parse_args()


def read_text(filename: str) -> str:
    """
    Text reading function.

    :param filename: Path to the text to be read
    :return: The input text
    """

    try:

        with open(filename, 'r', encoding='utf-8') as text:
            return text.read()

    except:

        print(f"File '{filename}' not found.")
        sys.exit(1)


def write_encrypted_text(filename: str, text: str) -> None:
    """
    Function to write text to file.

    :param filename: Path to the file where the text will be saved.
    :param text: Encrypted text
    :return: None
    """

    try:

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)

    except Exception as e:

        print(f"Error writing to file '{filename}': {e}")
        sys.exit(1)


def main():

    args = parser_create()

    key = read_text(args.key_filename)
    input_text = read_text(args.input_text)
    encrypted_text = vigenere_cipher_encrypt(input_text, key)
    output_text = args.output_text

    write_encrypted_text(output_text, encrypted_text)


if __name__ == "__main__":
     main()
