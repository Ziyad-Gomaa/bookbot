from stats import word_count, char_count, dict_sort

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        contents = file.read()

    return contents

def main():
    path_to_file = "./books/frankenstein.txt"
    text = get_book_text(path_to_file)

    num_of_words = word_count(text)
    dict_of_chars = char_count(text)
    chars_sorted = dict_sort(dict_of_chars)

    print(12 * "=", "BOOKBOT", "=" * 12)
    print("Analyzing book found at books/frankenstein.txt...")

    print(11 * "-", "Word Count", "-" * 11)
    print(f"Found {num_of_words} total words")

    print(9 * "-", "Character Count", "-" * 9)
    for char in chars_sorted:
        print(char["char"] + ":", char["num"])

    print(13 * "=", "END", "=" * 13)


main()
