def find_target_pair(numbers, target_val):
    # Dictionary to keep track of numbers we have already checked
    checked_numbers = {}
    
    for index, current_num in enumerate(numbers):
        needed_num = target_val - current_num
        
        # Check if the missing piece of the puzzle is already in our dictionary
        if needed_num in checked_numbers:
            return [checked_numbers[needed_num], index]
        
        # If not found, store the current number with its index and move to the next
        checked_numbers[current_num] = index

# Test to make sure it works
print(find_target_pair([2, 7, 11, 15], 9))  # Output should be: [0, 1]
