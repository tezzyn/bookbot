from stats import word_count, char_count, sort_dict
import sys

def get_book_text(path_to_book):

    with open(path_to_book) as txt:
        content = txt.read()
    
    return content



def main():

    for items in sys.argv:
        # print(len(sys.argv))
        if len(sys.argv) <= 1:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
            


        text = get_book_text(str(sys.argv[1]))

    print("=========== BOOKBOT ============")

    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    
    print(f"Found {word_count(text)} total words")

    print("--------- Character Count -------")

    sort_dict(char_count(text))

    print("============= END ===============")

main()
