class Book:
    def init(self, title: str, author: str):
        """Initialize a Book with title and author."""
        self.title = title
        self.author = author

    def str(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def init(self, title: str, author: str, file_size: int):
        """Initialize an EBook, calling the Book constructor."""
        super().init(title, author)
        self.file_size = file_size

    def str(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def init(self, title: str, author: str, page_count: int):
        """Initialize a PrintBook, calling the Book constructor."""
        super().init(title, author)
        self.page_count = page_count

    def str(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def init(self):
        """Initialize the library with an empty book list."""
        self.books = []

    def add_book(self, book: Book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)