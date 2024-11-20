# FIFO Page Replacement Algorithm
def fifo_page_replacement(pages, capacity):
    memory = []  # List to hold pages in memory
    page_faults = 0  # Count of page faults

    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)  # Add page to memory if space available
            else:
                memory.pop(0)  # Remove the first page (FIFO)
                memory.append(page)  # Add the new page
            page_faults += 1
        # Optional: Print memory state for each step
        print("Memory:", memory)
    
    return page_faults


# LRU (Least Recently Used) Page Replacement Algorithm
def lru_page_replacement(pages, capacity):
    memory = []  # List to hold pages in memory
    page_faults = 0  # Count of page faults
    page_index = {}  # Dictionary to keep track of the last accessed index of pages

    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)  # Add page to memory if space available
            else:
                # Find the least recently used page by using page_index
                lru_page = min(memory, key=lambda p: page_index[p])
                memory.remove(lru_page)  # Remove LRU page
                memory.append(page)  # Add the new page
            page_faults += 1
        # Update the index of the current page to the latest access
        page_index[page] = i
        # Optional: Print memory state for each step
        print("Memory:", memory)
    
    return page_faults


# Optimal Page Replacement Algorithm
def optimal_page_replacement(pages, capacity):
    memory = []  # List to hold pages in memory
    page_faults = 0  # Count of page faults

    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)  # Add page to memory if space available
            else:
                # Find the page that will not be used for the longest time
                future_indices = []
                for mem_page in memory:
                    if mem_page in pages[i + 1:]:
                        future_indices.append(pages[i + 1:].index(mem_page))
                    else:
                        future_indices.append(float('inf'))  # This page won't be used again

                # Replace the page that won't be used for the longest time
                replace_index = future_indices.index(max(future_indices))
                memory[replace_index] = page
            page_faults += 1
        # Optional: Print memory state for each step
        print("Memory:", memory)
    
    return page_faults


# Test cases
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 3

print("FIFO Page Faults:", fifo_page_replacement(pages, capacity))
print("LRU Page Faults:", lru_page_replacement(pages, capacity))
print("Optimal Page Faults:", optimal_page_replacement(pages, capacity))
