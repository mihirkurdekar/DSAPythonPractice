# Problem: Given a string, find the first non-repeating character.
# Example: s = "aabbc"
# Output: c

class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key, None)

    def remove(self, key):
        if key in self.table:
            del self.table[key]

    def first_non_repeating_char(self, s):
        char_count = {}

        # Count occurrences of each character
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Find the first non-repeating character
        for char in s:
            if char_count[char] == 1:
                return char

        return None

# Example usage
if __name__ == "__main__":
    s = "aabbc"
    hash_table = HashTable()
    first_non_repeating = hash_table.first_non_repeating_char(s)
    print("First non-repeating character:", first_non_repeating)  # Output: c