import math

from consts import *


def frequency_bit_test(sequence: str) -> float:

    n = len(sequence)

    if n == 0:
        raise ValueError("Sequence is empty")

    s = sum([1 if bit == "1" else -1 for bit in sequence])

    p_value = math.erfc((abs(s) / math.sqrt(n)) / math.sqrt(2))

    return p_value


def main():

    CPP_sequence = read_file(CPP_sequence_txt)

    print(frequency_bit_test(CPP_sequence))


def read_file(filename: str) -> str:

    try:

        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()

    except Exception as e:

        print(f"Error reading file: {e}")


def write_file(filename: str, text: str) -> None:

    try:

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)

    except Exception as e:

        print(f"Error writing file: {e}")


if __name__ == "__main__":
    main()

