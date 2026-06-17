def get_num_words(text: str) -> int:
    return len(text.split())


def symbols_counter(text: str) -> dict[str, int]:
    character_count: dict[str, int] = {}
    lower_case = text.lower()
    for char in lower_case:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count


def sort_on(char_count: tuple[str, int]) -> int:
    return char_count[1]


def chars_dict_to_sorted_list(character_counts: dict[str, int]) -> list[tuple[str, int]]:
    chars_sorted_list: list[tuple[str, int]] = []
    for char, count in character_counts.items():
        chars_sorted_list.append((char, count))
    return sorted(chars_sorted_list, reverse=True, key=sort_on)