#LRU
from collections import OrderedDict

class LRUPageReplacement:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = OrderedDict()

    def access_page(self, page):
        if page in self.pages:
            self.pages.move_to_end(page)
        else:
            if len(self.pages) >= self.capacity:
                self.pages.popitem(last=False)
            self.pages[page] = True

    def display(self):
        print(f"Pages in memory: {list(self.pages.keys())}")

# Example usage
lru = LRUPageReplacement(capacity=3)
pages_to_access = [1, 2, 3, 4, 2, 5, 1, 2, 3, 4, 5]

for page in pages_to_access:
    lru.access_page(page)
    lru.display()
