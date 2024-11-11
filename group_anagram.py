from collections import defaultdict
def groupAnagrams(strs):
        # Create a defaultdict to store groups of anagrams
        anagrams = defaultdict(list)
        print(anagrams)
        # Iterate through each string in the input list
        for word in strs:
            # Sort the characters of the word to use it as a key
            sorted_word = ''.join(sorted(word))
            # Add the word to the corresponding group in the dictionary
            anagrams[sorted_word].append(word)
            print(anagrams)
        # Convert the values of the dictionary to a list and return
        return list(anagrams.values())
s=["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(s))