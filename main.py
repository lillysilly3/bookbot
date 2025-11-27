from stats import get_num_words
from stats import get_character_counts
from stats import character_sorted
import sys

def get_book_text(filepath):
    # Opening the file to read
    with open(filepath) as f:
        return f.read()

def main():
    # Check if correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    
    number_of_words = get_num_words(text)
    character_count = get_character_counts(text)
    character_sort = character_sorted(character_count)
    
    print(f"Found {number_of_words} total words")
    
    print(character_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("–----------- Word Count –-----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for item in character_sort:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    for number in sys.argv:
        print(number)


main()