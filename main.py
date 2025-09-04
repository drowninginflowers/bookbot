from pathlib import Path
from stats import count_words, get_alphabetic_char_counts
import sys

def get_book_text(book_path: Path) -> str:
    return Path(book_path).read_text(encoding='utf-8')

def analyze_book(book_path: Path) -> None:
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_counts = get_alphabetic_char_counts(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_data in char_counts:
        print(f"{char_data['char']}: {char_data['count']}")
    print("============= END ===============")

def main(book_path) -> None:
    try:
        analyze_book(book_path)
    except Exception as error:
        print(error)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = Path(sys.argv[1])
        main(path_to_book)
