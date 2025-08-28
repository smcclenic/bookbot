import sys
from stats import (
    get_num_words, 
    get_char_dict,
    char_dict_to_sorted
)
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    num_words = get_num_words(file_path)
    char_dict = get_char_dict(file_path)
    char_sorted = char_dict_to_sorted(char_dict)
    print_report(file_path, num_words, char_sorted)

def print_report(file_path, num_words, char_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()