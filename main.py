def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def count_words(text):
    word_count = len(text.split())
    return f"{word_count} words found in the document"

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    print(count_words(book_text))

main()
