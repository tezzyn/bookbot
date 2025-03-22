from stats import word_count 
from stats import char_count
from stats import sort_dict

def get_book_text(path_to_book):

    with open(path_to_book) as txt:
        content = txt.read()
    
    return content



def main():

    text = get_book_text("books/frankenstein.txt")

    print("=========== BOOKBOT ============")

    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    
    print(word_count(text))

    print("--------- Character Count -------")

    sort_dict(char_count(text))

    print("============= END ===============")

main()
