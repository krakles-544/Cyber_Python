class Book:

    def __init__(self, title, author, page_num):
        self.title = title
        self.author = author
        self.page_num = page_num

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.page_num < other.page_num
    
    def __gt__(self, other):
        return self.page_num > other.page_num
    
    def __add__(self, other):
        return self.page_num + other.page_num
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "page_num":
            return self.page_num
        else:
            return f"Key '{key}' was mot found"
        

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

print(book1["audio"])