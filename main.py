from stats import word_count 
from stats import char_count
from stats import sort_dict

def get_book_text(path_to_book):

    with open(path_to_book) as txt:
        content = txt.read()
    
    return content



def main():

    
    print(word_count(get_book_text("books/frankenstein.txt")+"\n"))


    # print(char_count(get_book_text("books/frankenstein.txt")))


    print(sort_dict(char_count(get_book_text("books/frankenstein.txt"))))

main()
