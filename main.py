from stats import word_count, char_count

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        contents = file.read()

    return contents



def main():
    path_to_file = "./books/frankenstein.txt"
    text = get_book_text(path_to_file)

    num_of_words = word_count(text)
    
    print(f"{num_of_words} words found in the document")

    chars_dict = char_count(text)

    print(chars_dict)


main()
