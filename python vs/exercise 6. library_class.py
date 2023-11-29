class library:
    def __init__(self):
        self._books = []
        # self._no_of_books = len(self._books)

    def add(self, book):
        self._books.append(book)
    
    def show(self):
        i = 1
        print()
        for books in self._books:
            print(f"{i}. {books}")
            i = i + 1
        print("\nTotal books: ",len(self._books),"\n")  
            
a = library()
bs = input("Enter books deviding \", \":-\n")
sw = bs.split(", ")
for book in sw:
    a.add(book)

while True:
    t = int(input("\nEnter 1 to add a book, 2 to print all books and number of books:\n"))
    if t == 1:
        a.add(input("Enter book name: "))
    elif t == 2:
        a.show()
    else:
        exit()
    