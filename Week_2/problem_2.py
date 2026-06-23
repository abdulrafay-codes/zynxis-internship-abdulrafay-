def check_for_duplicates(num_list):
    # A set to store the unique numbers we encounter
    seen_items = set()
    
    for number in num_list:
        # If the number is already in our set, it's a duplicate!
        if number in seen_items:
            return True
        
        # Otherwise, add it to our record and keep looking
        seen_items.add(number)
        
    # If the loop finishes and we found nothing, all numbers are unique
    return False

# --- Testing our logic ---
print(check_for_duplicates([1, 2, 3, 1]))  # Should output: True (because 1 appears twice)
print(check_for_duplicates([1, 2, 3, 4]))  # Should output: False (all unique)
