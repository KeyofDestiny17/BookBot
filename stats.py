def get_num_words(text):
    return len(text.split())

def symbols_counter(text):
    character_count = {}
    lower_case = text.lower()
    for char in lower_case:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_on(char_count):
    return char_count[1]

def chars_dict_to_sorted_list(character_counts):
    chars_sorted_list = []
    for char, count in character_counts.items():
        chars_sorted_list.append((char, count))
    return sorted(chars_sorted_list, reverse=True, key=sort_on)