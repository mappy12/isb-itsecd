from card_finder import *
from luhn import *

def main():
    serialization(find_card_number())

    is_valid(find_card_number())

if __name__ == "__main__":
    main()