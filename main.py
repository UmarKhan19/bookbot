from stats import get_book_text, get_report
import sys

def main():
    args = sys.argv
    book_path = None
    if len(args) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return
    book_path = args[1]
    book_text = get_book_text(book_path)
    get_report(book_text)


main()
