import sys

from consts import *
from frequency_analysis import *


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


def read_file(filename: str) -> str:
    """
    Text reading function.

    :param filename: Path to the text to be read
    :return: The input text
    """

    try:

        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()

    except:

        print(f"File '{filename}' not found.")
        sys.exit(1)


def main():

    save_freq_to_json(rus_freq_json, RUSSIAN_FREQ)

    encrypted_text = read_file(encrypted_text_txt)

    text_freq = calculate_freq(encrypted_text)

    save_freq_to_json(encrypted_freq_json, text_freq)

    rus_dict = load_freq_from_json(rus_freq_json)
    encrypt_dict = load_freq_from_json(encrypted_freq_json)

    encrypt_rus_dict = create_encrypt_rus_dict(encrypt_dict, rus_dict)

    key = load_freq_from_json(key_json)

    decrypted_text = decrypt_text(encrypted_text, key)

    write_encrypted_text(decrypted_text_txt, decrypted_text)


if __name__ == '__main__':
    main()
