from stats import num_words
from stats import count_chars
from stats import format_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    #analyze book & prepare data structures
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    freq_dict = count_chars(book_text)
    formatted_dict = format_dict(freq_dict)

    #fancy print
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words(book_text)} total words")
    print("--------- Character Count -------")
    for dict in formatted_dict:
        if dict["character"].isalpha():
            print(f"{dict["character"]}: {dict["count"]}")
    print("============= END ===============")

main()
