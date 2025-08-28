from stats import get_num_words
from stats import get_book_text
    
def main(file_path):
    book_text = get_book_text(file_path)
    print(book_text)

get_num_words("books/frankenstein.txt")