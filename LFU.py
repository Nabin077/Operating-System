#LFU
from collections import defaultdict, deque

class LFUPageReplacement:
    def __init__(self, capacity):
        self.capacity = capacity
        self.page_frequency = defaultdict(int)  # Tracks frequency of each page
        self.pages = {}  # Tracks the pages in memory and their insertion order
        self.min_freq = 0  # The minimum frequency of pages in memory

    def access_page(self, page):
        if page in self.pages:
            self.page_frequency[page] += 1  # Increment frequency
        else:
            if len(self.pages) >= self.capacity:
                # Find the page with the least frequency
                lfu_pages = [k for k, v in self.pages.items() if self.page_frequency[k] == self.min_freq]
                lfu_page = lfu_pages[0]  # LFU page to be removed
                self.pages.pop(lfu_page)
                self.page_frequency.pop(lfu_page)

            # Insert new page
            self.pages[page] = len(self.pages)
            self.page_frequency[page] = 1  # Set frequency to 1

        # Update the minimum frequency
        self.min_freq = min(self.page_frequency.values())
        
        print(f"Accessed page: {page}")
        print(f"Pages in memory: {self.pages}")
        print(f"Page frequencies: {dict(self.page_frequency)}")
        print("---")

# Example usage
lfu = LFUPageReplacement(capacity=3)
pages_to_access = [4, 3, 4, 2, 3, 4, 1]

for page in pages_to_access:
    lfu.access_page(page)
