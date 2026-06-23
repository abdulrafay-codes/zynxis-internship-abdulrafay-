def check_if_anagram(word1, word2):
    # If the lengths are different, they can't be anagrams
    if len(word1) != len(word2):
        return False
        
    # Dictionaries to count letters for both words
    letter_count1 = {}
    letter_count2 = {}
    
    # Count letters in the first word
    for letter in word1:
        letter_count1[letter] = letter_count1.get(letter, 0) + 1
        
    # Count letters in the second word
    for letter in word2:
        letter_count2[letter] = letter_count2.get(letter, 0) + 1
        
    # If the dictionaries match, the words have the exact same letter counts
    return letter_count1 == letter_count2

# --- Testing our logic ---
print(check_if_anagram("anagram", "nagaram"))  # Should output: True
print(check_if_anagram("hello", "world"))      # Should output: False
