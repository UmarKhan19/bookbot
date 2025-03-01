def get_book_text(filepath):
    """
    Reads the content of a book from the given file path and returns it.

    Parameters:
    filepath (str): The path to the book file.
    """
    with open(filepath, encoding='utf-8') as file:
        book_text = file.read()
        return book_text

def get_word_count(book_text : str):
    """
    Returns the number of words in the given book text.

    Parameters:
    book_text (str): The text of the book.
    """
    words = book_text.split()
    return len(words)
