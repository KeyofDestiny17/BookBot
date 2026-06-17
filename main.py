import sys
from stats import chars_dict_to_sorted_list
from stats import get_num_words
from stats import symbols_counter


def get_book_text(filepath):
    with open(filepath) as b:
        return b.read()


def print_report(text, path):
    word_count = get_num_words(text)
    character_counts = symbols_counter(text)
    chars_sorted_list = chars_dict_to_sorted_list(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in chars_sorted_list:
        if char.isalpha():
            print((char, count))
    print("============= END ===============")


def main():
    if len(sys.argv) == 1:
        path = "books/frankenstein.txt"
    else:
        path = sys.argv[1]

    text = get_book_text(path)
    print_report(text, path)


main()
