class Bookstore(object):
    def __init__ (self, name):
        
        self.name = name
        self.books = []
        
    def get_books(self):
        return self.books
    
    def add_book(self, book):
        self.books.append(book)
        
    def search_books(self, author = None, title = None):
        book_results = []
        
        if title is None:
            for i, value in enumerate(self.books):
                if author.name.lower() in self.books[i].author.name.lower():
                    book_results.append(self.books[i])
            return book_results
        else:
            for i, value in enumerate(self.books):
                if title.lower() in self.books[i].title.lower():
                    book_results.append(self.books[i])
            return book_results
            
class Author(object):
    def __init__ (self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.book_list = []
        
    def get_books(self):
        return self.book_list
        
    def add_book(self, book):
        self.book_list.append(book)

class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.add_book(self)
        
        

