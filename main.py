import sys
from stats import chars_dict_to_sorted_list
from stats import get_num_words
from stats import symbols_counter


def get_book_text(filepath: str) -> str:
    with open(filepath) as b:
        return b.read()


def print_report(text: str, path: str) -> None:
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


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    print_report(text, sys.argv[1])


if __name__ == "__main__":
    main()
