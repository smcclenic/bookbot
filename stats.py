def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(file_path):
    num_words = len(get_book_text(file_path).split())
    print(f"{num_words} words found in the document.")