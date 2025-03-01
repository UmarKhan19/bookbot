def get_book_text(filepath:str) -> str:
    """
    Reads the content of a book from the given file path and returns it.

    Parameters:
    filepath (str): The path to the book file.
    """
    with open(filepath, encoding='utf-8') as file:
        book_text = file.read()
        return book_text

def get_word_count(book_text : str) -> int:
    """
    Returns the number of words in the given book text.

    Parameters:
    book_text (str): The text of the book.
    """
    words = book_text.split()
    return len(words)

def get_letter_count(book_text : str):
    book_text_lowercase = book_text.lower()
    letter_count = {}
    for letter in book_text_lowercase:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

    return letter_count
