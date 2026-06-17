import sys
from stats import get_num_words
from stats import symbols_counter
from stats import sorted_count

def get_book_text(filepath):
    with open(filepath) as b:
        return b.read()
    
def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(sys.argv[1])
    word_count = get_num_words(text)
    character_counts = symbols_counter(text)
    sort = sorted_count(character_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")   
    for s in sort:
        if s["char"].isalpha():
            print(f"{s['char']}: {s['num']}")
    print("============= END ===============")
    
main()
