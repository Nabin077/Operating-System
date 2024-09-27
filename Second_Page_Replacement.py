#Second Chance Page Replacement
class SecondChancePageReplacement:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = []
        self.reference_bits = []

    def access_page(self, page):
        if page in self.pages:
            index = self.pages.index(page)
            self.reference_bits[index] = 1
        else:
            if len(self.pages) < self.capacity:
                self.pages.append(page)
                self.reference_bits.append(1)
            else:
                while True:
                    if self.reference_bits[0] == 0:
                        self.pages.pop(0)
                        self.reference_bits.pop(0)
                        self.pages.append(page)
                        self.reference_bits.append(1)
                        break
                    else:
                        self.pages.append(self.pages.pop(0))
                        self.reference_bits.append(self.reference_bits.pop(0))
                        self.reference_bits[-1] = 0

    def display(self):
        print(f"Pages in memory: {self.pages}")
        print(f"Reference bits: {self.reference_bits}")

# Example usage
second_chance = SecondChancePageReplacement(capacity=3)
pages_to_access = [1, 2, 3, 2, 4, 1, 5, 2, 4, 3]

for page in pages_to_access:
    second_chance.access_page(page)
    second_chance.display()
