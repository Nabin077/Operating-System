#Implementation of SCAN
def scan_disk_scheduling(requests, head, disk_size, direction):
    # Separate requests into two lists: requests less than the head, and requests greater than or equal to the head
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]
    
    # Sort the lists
    left.sort()
    right.sort()

    seek_sequence = []
    seek_count = 0

    # If the direction is left (towards 0)
    if direction == "left":
        # Process requests to the left of the head
        for track in reversed(left):
            seek_sequence.append(track)
            seek_count += abs(head - track)
            head = track

        # After reaching the beginning, move to 0 and reverse direction to process requests to the right
        seek_count += abs(head - 0)
        head = 0

        for track in right:
            seek_sequence.append(track)
            seek_count += abs(head - track)
            head = track

    # If the direction is right (towards the end of the disk)
    elif direction == "right":
        # Process requests to the right of the head
        for track in right:
            seek_sequence.append(track)
            seek_count += abs(head - track)
            head = track

        # After reaching the end, move to the max disk size and reverse direction to process requests to the left
        seek_count += abs(head - (disk_size - 1))
        head = disk_size - 1

        for track in reversed(left):
            seek_sequence.append(track)
            seek_count += abs(head - track)
            head = track
    return seek_sequence, seek_count

# Example usage
requests = [98, 183, 37, 122, 14, 124, 65, 67]
head = 53
disk_size = 200
direction = "left"  # Direction can be either "left" or "right"

seek_sequence, total_seek_count = scan_disk_scheduling(requests, head, disk_size, direction)

print("Seek Sequence:", seek_sequence)
print("Total Seek Count:", total_seek_count)