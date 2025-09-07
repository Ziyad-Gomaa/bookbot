def get_book_text(path_to_file):
    with open(path_to_file) as file:
        contents = file.read()
    return contents

def count_words(contents):
    return len(contents.split())

def main():
    path_to_file = "./books/frankenstein.txt"
    word_count = count_words(get_book_text(path_to_file))
    print(f"{word_count} words found in the document")


main()
