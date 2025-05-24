import time

import matplotlib.pyplot as plt

from card_finder import *


def find_card_number_time(process_count: int) -> float:
    start = time.time()
    with multiprocessing.Pool(process_count) as pool:
        for bin_code in BINS:
            card_nums = gen_card_nums(bin_code)

            for result in pool.imap_unordered(check_hash, card_nums, chunksize=500):
                if result:
                    pool.terminate()
                    pool.join()
                    end = time.time()
                    return end - start

    end = time.time()
    return end - start


def collect_times() -> tuple[list[int], list[float]]:
    max_cpu = int(get_cpu_count() * 1.5)
    process_counts = list(range(1, max_cpu + 1))
    timings = []

    for count in process_counts:
        duration = find_card_number_time(count)
        timings.append(duration)

    return process_counts, timings


def get_timing_graph(process_counts: list[int], timings: list[float]) -> None:
    min_time = min(timings)
    min_idx = timings.index(min_time)
    optimal_proc = process_counts[min_idx]

    plt.figure(figsize=(11,7))
    plt.plot(process_counts, timings, color="royalblue", label="Время подбора")
    plt.scatter(optimal_proc, min_time, color="red", label="Глобальный минимум")

    plt.title("Зависимость времени подбора хэша от количества процессов")
    plt.xlabel("Количество процессов")
    plt.ylabel("Время (в секундах)")

    plt.grid(True)

    plt.show()
