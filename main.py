from stats import get_book_text, get_word_count

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = get_word_count(book_text)
    print(f"Word count: {word_count}")

main()
