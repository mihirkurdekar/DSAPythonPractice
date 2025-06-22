'''
Hash Tables (Dictionaries in Python)
Problem: Given a string, find all anagrams in a given array of strings.
Example: s = "listen", strs = ["enlist", "tinsel", "inlets"]
Output: ["enlist", "tinsel", "inlets"] (all anagrams of "listen")
'''

def find_anagrams(s, strs):
    sorted_s = ''.join(sorted(s))
    anagrams = []
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word == sorted_s:
            anagrams.append(word)
    return anagrams

# Example usage
if __name__ == "__main__":
    s = "listen"
    strs = ["enlist", "tinsel", "inlets", "google", "abc"]
    result = find_anagrams(s, strs)
    print("Anagrams of", s, "are:", result)  # Output: ["enlist", "tinsel", "inlets"]