class Book:
    def __init__(self, title, pages) -> None:
        self.title = title
        self.pages = pages
        
    def __add__(self, other):
        total = self.pages + other.pages
        return total
        
b1 = Book('Unknown Soul', 300)
b2 = Book('Road Story', 200)

total_pages = b1 + b2
print("The total number of pages in both books is: ", total_pages)