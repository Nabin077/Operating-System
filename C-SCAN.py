#C-SCAN
def c_scan(requests, head, disk_size):
    # Separate requests that are greater than and less than the head
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]
    # Sort requests in both directions
    left.sort()
    right.sort()
    # C-SCAN service order: go to the right first, then jump to the left end
    seek_sequence = right + left
    seek_count = 0
    current_head = head
    # Traverse the requests in seek sequence and calculate the seek time
    for track in seek_sequence:
        seek_count += abs(current_head - track)
        current_head = track
    # Add the cost of moving from the last request on the right end to the left end (circular movement)
    if right:
        seek_count += abs(disk_size - 1 - right[-1]) + abs(left[0])
    return seek_sequence, seek_count
# Example usage
requests = [98, 183, 37, 122, 14, 124, 65, 67]
head = 53
disk_size = 200
seek_sequence, total_seek_count = c_scan(requests, head, disk_size)
print("Seek Sequence:", seek_sequence)
print("Total Seek Count:", total_seek_count)