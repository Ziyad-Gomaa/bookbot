def word_count(contents):
    return len(contents.split())

def char_count(contents):
    char_stats = {}

    for char in contents.lower():
        if char.isalpha():
            if char in char_stats:
                char_stats[char] += 1
            else:
                char_stats[char] = 1

    return char_stats

def dict_sort(dict_of_chars):
    sorted_list = []

    for char in dict_of_chars:
        sorted_list.append({"char": char, "num": dict_of_chars[char]})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

def sort_on(list_of_dicts):
        return list_of_dicts["num"]
