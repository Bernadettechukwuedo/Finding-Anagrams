# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    str1 = input("insert your first word:")
    str2 = input("insert your second word:")
    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)
    if str1_sorted == str2_sorted:
        return True
    if str1_sorted != str2_sorted:
        return False
find_anagrams(str1, str2)

    

