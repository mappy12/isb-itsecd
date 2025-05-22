def luhn_check(card_nums: str) -> bool:
    sum = 0
    reverse_nums = card_nums[::-1]

    for i, digit in enumerate(reverse_nums):
        num = int(digit)

        if i % 2 == 1:
            num *= 2

            if num > 9:
                num -= 9

        sum += num

    return sum % 10 == 0


