def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    chars = {}
    for char in text:
        char = char.lower()
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] +=1
    return chars

def sort_chars(chars):
    sorted_list = []
    for char in chars:
        sorted_list.append({"char": char, "num": chars[char]})
    sorted_list.sort(reverse=True, key=sort_dict)
    return sorted_list

def sort_dict(dict):
    return dict["num"]