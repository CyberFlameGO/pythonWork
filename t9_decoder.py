"""
Decodes T9-format numbers into words.
"""

# number to be decoded: 7667972687326230

keymap: dict = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def decode(numbers: str) -> str:
    """Decodes T9-format numbers into words."""
    if isinstance(numbers, int):
        numbers = str(numbers)
    
    for i, v in enumerate(numbers):
        if v not in keymap:
            return 'Invalid input'
        if i == 0:
            words = list(keymap[v])
        else:
            words = [word + letter for word in words for letter in keymap[v]]
    return words
    



def main():
    """Main function."""

    numbers = input('Enter T9-format numbers: ')
    words = decode(numbers)
    print(words)

if __name__ == '__main__':
    main()

