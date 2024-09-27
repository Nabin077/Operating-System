#OPR
def find_farthest_page(pages, current_index, frames):
    farthest = current_index
    page_to_replace = None

    for frame_page in frames:
        try:
            next_index = pages[current_index:].index(frame_page) + current_index
        except ValueError:
            return frame_page  # If the page is not in the future, return it immediately
        
        if next_index > farthest:
            farthest = next_index
            page_to_replace = frame_page

    return page_to_replace

def optimal_page_replacement(pages, capacity):
    frames = []
    page_faults = 0
    page_hits = 0

    for i, page in enumerate(pages):
        if page in frames:
            page_hits += 1
        else:
            page_faults += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                page_to_replace = find_farthest_page(pages, i + 1, frames)
                frames[frames.index(page_to_replace)] = page

        print(f"Accessed page: {page}")
        print(f"Frames: {frames}")
        print(f"Page Faults: {page_faults}, Page Hits: {page_hits}")
        print("---")

# Example usage
pages_to_access = [7, 0, 1, 2, 3, 4, 2]
capacity = 3
optimal_page_replacement(pages_to_access, capacity)
