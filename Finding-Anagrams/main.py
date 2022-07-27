# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

    
def find_anagrams(word, anagram):
    # [assignment] Add your code here
    if sorted(word) == sorted(anagram):
        return True
    else:
        return False


input1 = input("Enter your first word:")
input2 = input("Enter your anagram:")
print(find_anagrams(input1, input2))
