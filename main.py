from stats import get_num_words
from stats import get_character_counts
from stats import character_sorted

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    number_of_words = get_num_words(text)
    character_count = get_character_counts(text)
    character_sort = character_sorted(character_count)
    print(f"Found {number_of_words} total words")
    print(character_count)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("–----------- Word Count –-----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for item in character_sort:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    


main()