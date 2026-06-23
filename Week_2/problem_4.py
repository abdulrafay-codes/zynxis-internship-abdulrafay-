def group_similar_words(word_list):
    # HashMap dictionary to store our grouped words
    grouped_dictionary = {}
    
    for word in word_list:
        # Sort the letters alphabetically to create a uniform "key"
        # e.g., "tea" becomes "aet"
        sorted_key = "".join(sorted(word))
        
        # If this key doesn't exist yet, create an empty list for it
        if sorted_key not in grouped_dictionary:
            grouped_dictionary[sorted_key] = []
            
        # Add the original word to its matching group
        grouped_dictionary[sorted_key].append(word)
        
    # Return just the grouped lists from our dictionary
    return list(grouped_dictionary.values())

# --- Testing our logic ---
test_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_similar_words(test_words))
# Expected output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
