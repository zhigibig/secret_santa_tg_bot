
from random import randint 

def key_generation():
    KEY_LENGTH = 100

    lower_case = 'qwertyuiopasdfghjklzxcvbnm'
    upper_case = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    digits = '1234567890'
    signs = '{}[];:.,!~$%&*()-=+'
    symbols = [lower_case, upper_case, digits, signs]

    key = str()
    
    while len(key) < KEY_LENGTH:
        row = randint(0, len(symbols) - 1)
        count_of_items = randint(1, KEY_LENGTH - len(key))
        for i in range(count_of_items):
            key += symbols[row][randint(0, len(symbols[row]) - 1)]

    return key

def main():
    return 0

if __name__ == "__main__":
    main()
