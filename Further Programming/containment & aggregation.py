class Book:
    def __init__(self,title,author,genre):
        self.title = title
        self.author = author
        self.genre = genre

class Library:
    def __init(self,location,librarian):
        self.location = location
        self.librarian = librarian
    Catalogue = []
    def storeBook(self):
        Library.Catalogue.append(self)


library1 = ("BBS", "Nicholas")
book1 = Book("Rachel Karen", "Charly", "Horror")
book2 = Book("Lincoln", "Sean Alson", "Romance")
Library.storeBook(book1)
Library.storeBook(book2)
print(Library.Catalogue)



    