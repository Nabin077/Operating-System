#LOOK
def look_disk_scheduling(requests, head, direction):
    # Separate requests into two lists: those less than the head and those greater than or equal to the head
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
        # After reaching the end of the left requests, move to the start of the disk and then to the right requests
        if right:
            seek_count += abs(head - right[0])
            head = right[0]
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
        # After reaching the end of the right requests, move to the start of the disk and then to the left requests
        if left:
            seek_count += abs(head - left[-1])
            head = left[-1]
            for track in reversed(left):
                seek_sequence.append(track)
                seek_count += abs(head - track)
                head = track
    return seek_sequence, seek_count
# Example usage with corrected calculation
requests = [98, 183, 37, 122, 14, 124, 65, 67]
head = 53
direction = "left"
seek_sequence, total_seek_count = look_disk_scheduling(requests, head, direction)
print("Seek Sequence:", seek_sequence)
print("Total Seek Count:", total_seek_count)