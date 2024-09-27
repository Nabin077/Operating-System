#LINKED LIST
class Node:
    def __init__(self, start, size):
        self.start = start  # Starting address of the free block
        self.size = size    # Size of the free block
        self.next = None    # Pointer to the next node in the list

class LinkedListFreeSpaceManager:
    def __init__(self, total_memory):
        self.head = Node(0, total_memory)  # Initialize with a single large free block

    def allocate(self, size):
        prev = None
        current = self.head

        while current:
            if current.size >= size:  # Found a block large enough
                allocated_start = current.start

                if current.size == size:  # Exact match
                    if prev:
                        prev.next = current.next
                    else:
                        self.head = current.next
                else:  # Split the block
                    current.start += size
                    current.size -= size

                print(f"Allocated {size} unit(s) of memory starting from address {allocated_start}.")
                return allocated_start

            prev = current
            current = current.next

        print("Error: Not enough free space available.")
        return None

    def deallocate(self, start, size):
        new_node = Node(start, size)
        prev = None
        current = self.head

        # Find the correct place to insert the new node
        while current and current.start < start:
            prev = current
            current = current.next

        # Coalesce with adjacent blocks if possible
        if prev and prev.start + prev.size == start:
            prev.size += size
            new_node = prev
        else:
            new_node.next = current
            if prev:
                prev.next = new_node
            else:
                self.head = new_node

        if new_node.next and new_node.start + new_node.size == new_node.next.start:
            new_node.size += new_node.next.size
            new_node.next = new_node.next.next

        print(f"Deallocated {size} unit(s) of memory starting from address {start}.")

    def display(self):
        current = self.head
        free_blocks = []
        while current:
            free_blocks.append((current.start, current.size))
            current = current.next
        print(f"Free memory blocks: {free_blocks}")

# Example usage
memory_manager = LinkedListFreeSpaceManager(total_memory=100)

memory_manager.allocate(20)
memory_manager.display()

memory_manager.allocate(10)
memory_manager.display()

memory_manager.deallocate(20, 10)
memory_manager.display()

memory_manager.allocate(15)
memory_manager.display()

memory_manager.deallocate(0, 20)
memory_manager.display()