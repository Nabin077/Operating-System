#Bitmaps
class BitmapAllocator:
    def __init__(self, total_blocks):
        self.total_blocks = total_blocks
        self.bitmap = [0] * total_blocks  # Initialize all blocks as free (0)

    def allocate(self, num_blocks):
        start_index = -1

        for i in range(self.total_blocks - num_blocks + 1):
            if all(b == 0 for b in self.bitmap[i:i + num_blocks]):
                start_index = i
                break

        if start_index != -1:
            for i in range(start_index, start_index + num_blocks):
                self.bitmap[i] = 1
            print(f"Allocated {num_blocks} block(s) starting from index {start_index}.")
        else:
            print("Not enough free blocks available.")

    def deallocate(self, start_index, num_blocks):
        if all(self.bitmap[start_index:start_index + num_blocks]) == 1:
            for i in range(start_index, start_index + num_blocks):
                self.bitmap[i] = 0
            print(f"Deallocated {num_blocks} block(s) starting from index {start_index}.")
        else:
            print("Error: Some blocks were not allocated.")

    def display(self):
        print(f"Bitmap: {self.bitmap}")

# Example usage
allocator = BitmapAllocator(total_blocks=10)

allocator.allocate(3)
allocator.display()

allocator.allocate(4)
allocator.display()

allocator.deallocate(0, 3)
allocator.display()

allocator.allocate(5)
allocator.display()
