from urllib import response
import requests

class Book():
    def __init__(self, title, authors=[]):
        self.title = title
        self.authors = authors

    def setTitle(self, title):
        self.title = title

    def setAuthor(self, author):
        self.authors.append(author)

    def getTitle(self):
        return self.title

    def getAuthors(self):
        return self.authors

    def __str__(self):
        retStr = self.title
        retStr += " by "
        retStr += ", ".join(self.authors)
        return retStr

class Bookshelf():
    def __init__(self):
        self.myBooks = []
    
    def addBook(self, book):
        self.myBooks.append(book)

    def showBookself(self):
        for book in self.myBooks:
            print(book)

    def searchForBook(self, title):
        for book in self.myBooks:
            if (book.getTitle() == title):
                return book
        return None



def getData(subject):
    URL = "http://openlibrary.org/subjects/"+subject+".json"

    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        response_JSON = response.json()
        return response_JSON

    except requests.exceptions.HTTPError as errc:
        print(errc)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
    
myBookshelf = Bookshelf()
jsonBookData = getData("python")

for currentBook in jsonBookData["works"]:
    bookTitle = currentBook["title"]

    authors = []
    for author in currentBook["authors"]:
        authors.append(author["name"])

    newBook = Book(bookTitle, authors)
    myBookshelf.addBook(newBook)

myBookshelf.showBookself()
