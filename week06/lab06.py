class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'"{self.title}" by {self.author}\nPublished: {self.year}'

    def get_age(self):
        return 2026 - self.year


class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        # Get the parent's string representation
        parent_str = super().__str__()
        # Extend it with EBook-specific information
        return f"{parent_str}\nFile Size: {self.file_size} MB"


# Test the classes
book = Book("1984", "George Orwell", 1949)
print("Book:")
print(book)
print(f"Age: {book.get_age()} years\n")

ebook = EBook("Digital Fortress", "Dan Brown", 1998, 2.5)
print("EBook:")
print(ebook)
print(f"Age: {ebook.get_age()} years")
