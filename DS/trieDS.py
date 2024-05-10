"""
This code defines a Trie data structure in Python.

A Trie (pronounced "try") is a tree-like data structure used for efficient retrieval of a key in a dataset of strings. 
Each node in the Trie represents a single character of the string. The root node represents an empty string, and each 
child node represents a character in the string. Each node may have multiple children, one for each possible next 
character in the strings being stored. The presence of a node's child signifies that the character corresponding to 
that child is present in the string.
"""

class TrieNode:
    # Define a class for Trie nodes
    def __init__(self):
        # Initialize a Trie node
        self.children = {}  # Dictionary to store children nodes
        self.is_end_of_word = False  # Flag to mark the end of a word

class Trie:
    # Define a class for Trie
    def __init__(self):
        # Initialize a Trie
        self.root = TrieNode()  # Create a root node
    
    def insert(self, word):
        # Method to insert a word into the Trie
        node = self.root  # Start from the root
        for char in word:
            # Iterate through each character in the word
            if char not in node.children:
                # If the character is not in the children nodes
                node.children[char] = TrieNode()  # Create a new node
            node = node.children[char]  # Move to the next node
        node.is_end_of_word = True  # Mark the end of the word
    
    def search(self, word):
        # Method to search for a word in the Trie
        node = self.root  # Start from the root
        for char in word:
            # Iterate through each character in the word
            if char not in node.children:
                # If the character is not in the children nodes
                return False  # Word does not exist
            node = node.children[char]  # Move to the next node
        return node.is_end_of_word  # Return if it's the end of a word
    
    def starts_with(self, prefix):
        # Method to check if any word in the Trie starts with the given prefix
        node = self.root  # Start from the root
        for char in prefix:
            # Iterate through each character in the prefix
            if char not in node.children:
                # If the character is not in the children nodes
                return False  # No word with the given prefix
            node = node.children[char]  # Move to the next node
        return True  # Prefix found in at least one word in the Trie

# Example usage:
trie = Trie()  # Create a Trie object
trie.insert("apple")  # Insert "apple" into the Trie
trie.insert("app")  # Insert "app" into the Trie
trie.insert("banana")  # Insert "banana" into the Trie

print(trie.search("apple"))  # Output: True, "apple" exists in the Trie
print(trie.search("app"))    # Output: True, "app" exists in the Trie
print(trie.search("banana")) # Output: True, "banana" exists in the Trie
print(trie.search("orange")) # Output: False, "orange" does not exist in the Trie
print(trie.starts_with("pp"))  # Output: True, "app" is a prefix of "apple" and "app"
