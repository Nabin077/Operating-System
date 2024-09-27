#C-LOOK
def clook_disk_scheduling(requests, head):
    # Separate requests into two lists: those less than the head and those greater than or equal to the head
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    # Sort the lists
    left.sort()
    right.sort()

    seek_sequence = []
    seek_count = 0

    # First, service the requests to the right of the head
    for track in right:
        seek_sequence.append(track)
        seek_count += abs(head - track)
        head = track

    # Jump to the leftmost request and service remaining requests
    if left:
        seek_count += abs(head - left[0])
        head = left[0]

        for track in left:
            seek_sequence.append(track)
            seek_count += abs(head - track)
            head = track

    return seek_sequence, seek_count


# Example usage
requests = [98, 183, 37, 122, 14, 124, 65, 67]
head = 53

seek_sequence, total_seek_count = clook_disk_scheduling(requests, head)

print("Seek Sequence:", seek_sequence)
print("Total Seek Count:", total_seek_count)
