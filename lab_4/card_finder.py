import hashlib
import os
import json

import multiprocessing

from consts import *


def get_cpu_count():
    return os.cpu_count()


def gen_card_nums(bin_code: str):
    nums = []

    for i in range(1000000):
        mid = f"{i:06}"
        nums.append(bin_code + mid + LAST_4_DIGITS)

    return nums


def check_hash(card_nums: str) -> str | None:
    hashed = hashlib.sha3_256(card_nums.encode()).hexdigest()

    if hashed == CARD_HASH:
        return card_nums

    else:
        return None


def find_card_number() -> str | None:
    cpu_count = get_cpu_count()

    with multiprocessing.Pool(cpu_count) as pool:

        for bin_code in BINS:

            card_nums = gen_card_nums(bin_code)
            for result in pool.imap_unordered(check_hash, card_nums, chunksize=500):

                if result:
                    return result

    return None


def serialization(card_nums: str, path: str = "result.json") -> None:

    data = {
        "card_numbers": card_nums
    }

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)