def main():
    book_path = "../books/frankenstein.txt"
    book_file = book_path.split("/")[-1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_character_count(text)
    word_dict = convert_dict(char_count)
    word_dict.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_file} ---")
    print(f"{word_count} words found in the document")
    print_report(word_dict)
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if char.isalpha():        
            if char in char_count and char:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def print_report(dicts):
    for dict in dicts:
        print(f'The \'{dict["letter"]}\' character was found {dict["num"]} times')
        
def convert_dict(dict):
    return [{"letter": key, "num": value} for key, value in dict.items()]

def sort_on(dict):
    return dict["num"]

main()