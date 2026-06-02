class Book:
    current_year = 2026

    def __init__(self, title, author, isbn, publication_year):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._publication_year = publication_year

    def get_age(self):
        return Book.current_year - self._publication_year

    def get_summary(self):
        return (
            f"Title: {self._title}, "
            f"Author: {self._author}, "
            f"Published: {self._publication_year}"
        )


# Creating book instances
book1 = Book(
    title="Harry Potter and the Philosopher's Stone",
    author="J. K. Rowling",
    isbn="978-0-7475-3269-9",
    publication_year=1997,
)
book2 = Book(
    title="The Alchemist",
    author="Paulo Coelho",
    isbn="0-06-250217-4",
    publication_year=1988,
)
book3 = Book(
    title="A Man Called Ove",
    author="Fredrik Backman",
    isbn="9781476738024",
    publication_year=2012,
)

# Displaying book summaries and ages
book1_info = f"{book1.get_summary()} is {book1.get_age()} years old."
book2_info = f"{book2.get_summary()} is {book2.get_age()} years old."
book3_info = f"{book3.get_summary()} is {book3.get_age()} years old."
print(f"First book summaries: {book1_info}")
print(f"Second book summaries: {book2_info}")
print(f"Third book summaries: {book3_info}")
