import hashlib
import os

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