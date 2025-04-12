import math

from scipy.special import gammainc

from consts import *


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


def frequency_bit_test(sequence: str) -> float:

    n = len(sequence)

    if n == 0:
        raise ValueError("Sequence is empty")

    s = sum([1 if bit == "1" else -1 for bit in sequence])

    p_value = math.erfc((abs(s) / math.sqrt(n)) / math.sqrt(2))

    return p_value


def runs_test(sequence: str) -> float:

    p_value = 0

    n = len(sequence)

    p = sequence.count('1') / n

    if abs(p - 0.5) >= 2 / math.sqrt(n):
        return p_value

    v_n = 0

    for i in range(n):

        if i == 0 or sequence[i] != sequence[i - 1]:
            v_n += 1

    numerator = abs(v_n - 2 * n * p * (1 - p))
    denominator = 2 * math.sqrt(2 * n) * p * (1 - p)

    return math.erfc(numerator / denominator)


def block_run_test(sequence: str) -> float:

    n = len(sequence)

    if n < 128:
        raise ValueError("Minimum 128 bits")

    N = n // 8

    v = [0, 0, 0, 0]

    for i in range(N):

        block = sequence[i * 8 : (i + 1) * 8]

        max_run = 0
        current_run = 0

        for bit in block:

            if bit == '1':
                current_run += 1

                if current_run > max_run:
                    max_run = current_run

            else:
                current_run = 0

        match max_run:

            case 0 | 1:
                v[0] += 1

            case 2:
                v[1] += 1

            case 3:
                v[2] += 1

            case _:
                v[3] += 1

    x_2 = 0.0

    for i in range(len(v)):
        x_2 += (v[i] - 16 * PI[i]) ** 2 / (16 * PI[i])

    p_value = gammainc(3 / 2, x_2 / 2)

    return p_value


def main():

    cpp_sequence = read_file(cpp_sequence_txt)
    print("Последовательность:", cpp_sequence)
    print(block_run_test(cpp_sequence))


if __name__ == "__main__":
    main()
