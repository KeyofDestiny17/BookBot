def get_num_words(text):
    return len(text.split())

def symbols_counter(text):
    character_count = {}
    lower_case = text.lower()
    for lower in lower_case:
        if lower in character_count:
            character_count[lower] += 1
        else:
            character_count[lower] = 1
    return character_count

def sort_on(d):
    return d["num"]

def sorted_count(dictionary):
    list_sorting = []
    for d in dictionary:
        list_sorting.append({"char": d, "num": dictionary[d]})
    list_sorting.sort(reverse=True, key=sort_on)
    return list_sorting