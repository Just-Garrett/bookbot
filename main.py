def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    get_word_count(text)
    print("")
    get_chars_count(text.lower())
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    print(f"{len(words)} words found in the document")

def get_chars_count(text):
    char_dict = {}
    for i in text:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    for j in sorted(char_dict, key=char_dict.get, reverse=True):
        if j.isalpha():
            print(f"The '{j}' character was found {char_dict[j]} times")


main()
