def find_top_frequent(numbers, k_elements):
    # Step 1: Create a dictionary to count how often each number appears
    frequency_tracker = {}
    for num in numbers:
        frequency_tracker[num] = frequency_tracker.get(num, 0) + 1
        
    # Step 2: Sort the numbers based on their counts (frequencies) in descending order
    # This looks at the dictionary and sorts keys by their values high-to-low
    sorted_by_count = sorted(frequency_tracker, key=frequency_tracker.get, reverse=True)
    
    # Step 3: Slice the list to return only the top 'k' elements requested
    return sorted_by_count[:k_elements]

# --- Testing our logic ---
test_data = [1, 1, 1, 2, 2, 3]
k_val = 2
print(find_top_frequent(test_data, k_val))  # Should output: [1, 2]
