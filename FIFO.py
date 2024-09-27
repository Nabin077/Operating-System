#FIFO
from collections import deque

class FIFOPageReplacement:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = deque()
        self.page_faults = 0
        self.page_hits = 0

    def access_page(self, page):
        if page in self.pages:
            self.page_hits += 1
        else:
            self.page_faults += 1
            if len(self.pages) >= self.capacity:
                self.pages.popleft()
            self.pages.append(page)

    def display(self):
        print(f"Pages in memory: {list(self.pages)}")
        print(f"Page Faults: {self.page_faults}, Page Hits: {self.page_hits}")

# Example usage
fifo = FIFOPageReplacement(capacity=3)
pages_to_access = [1, 2, 3, 4, 1, 2, 5, 1]

for page in pages_to_access:
    fifo.access_page(page)
    fifo.display()
    print("---")
