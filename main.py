import sys

from stats import (
    get_word_count,
    get_char_count,
    sort_chars,
)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_count = get_char_count(book_text)
    sorted_list = sort_chars(char_count)

    print_report(book_path, word_count, sorted_list)
    
def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

def print_report(book_path, word_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()