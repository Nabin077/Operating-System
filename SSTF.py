#SSTF
def sstf_disk_scheduling(requests, head):
    seek_sequence = []
    seek_count = 0
    current_head = head

    while requests:
        # Find the request with the minimum seek time from the current head
        closest_request = min(requests, key=lambda r: abs(current_head - r))
        seek_sequence.append(closest_request)
        seek_count += abs(current_head - closest_request)
        current_head = closest_request
        requests.remove(closest_request)  # Remove the processed request

    return seek_sequence, seek_count


# Example usage with corrected seek count
requests = [100, 50, 10, 150, 180, 90]
head = 75

seek_sequence, total_seek_count = sstf_disk_scheduling(requests, head)

print("Seek Sequence:", seek_sequence)
print("Total Seek Count:", total_seek_count)