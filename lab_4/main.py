import argparse

from card_finder import *
from collision_timing import *
from luhn import *


def mode_1():
    print("MODE 1: Подбор номера карты по ее хешу с использованием оптимального числа процессов\n")

    cpu_count = get_cpu_count()

    print(f"Используемое число процессов: {cpu_count}")
    card_nums = find_card_number()

    if card_nums:
        print(f"Найденный номер карты: {card_nums}\n")
        serialization(card_nums)
        print("Результат сериализован в result.json")

    else:
        print("Номер карты не найден")


def mode_2():
    print("MODE 2: Проверка карты алгоритмом Луна (корректность номера)\n")

    card_nums = find_card_number()
    print(f"Номер карты: {card_nums}\n")

    print("Проверка:\n")
    is_valid(card_nums)


def mode_3():
    print("MODE 3: Замер времени поиска коллизии хеша при различном числе процессов\n")

    print("Обработка ->...\n")

    process_counts, timings = collect_times()
    print("Число процессов:")
    print(process_counts)
    print("Время:")
    print(timings)
    print("\n\n")

    get_timing_graph(process_counts, timings)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "mode",
        type=int,
        choices=[1,2,3],
        help="Режимы работы: \n"
             "1 - Подбор номера карты по хэшу\n"
             "2 - Проверка корректности номера алгоритмом Луна\n"
             "3 - Замер времени подбора при разном числе процессов"
    )

    args = parser.parse_args()

    match args.mode:

        case 1:
            mode_1()
        case 2:
            mode_2()
        case 3:
            mode_3()


if __name__ == "__main__":
    main()