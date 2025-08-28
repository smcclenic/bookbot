def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(file_path):
    num_words = len(get_book_text(file_path).split())
    return num_words

def get_char_dict(file_path):
    book_text = get_book_text(file_path)
    char_dict = {}
    for char in book_text:
        lowered = char.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

def sort_on(d):
    return d["num"]

def char_dict_to_sorted(char_dict):
    char_list = []
    for char, num in char_dict.items():
        char_list.append({"char": char, "num": num})
    char_list.sort(key=sort_on, reverse=True)
    return char_list