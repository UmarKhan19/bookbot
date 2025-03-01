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

def get_report(book_text:str)->str:
    word_count = get_word_count(book_text)
    character_count = get_letter_count(book_text)
    report = f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
"""

    character_count

    for letter, count in sorted(character_count.items(),key=lambda x: x[1], reverse=True):
        report += f"{letter}: {count}\n"

    report += "============= END ==============="


    print(report)
