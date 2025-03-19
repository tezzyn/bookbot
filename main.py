from stats import word_count
from stats import char_count

def get_book_text(path_to_book):

    with open(path_to_book) as txt:
        content = txt.read()
    
    return content



def main():
    print(word_count(get_book_text("books/frankenstein.txt")))

    print("  ")

    print(char_count(get_book_text("books/frankenstein.txt")))

main()
