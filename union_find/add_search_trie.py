class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.is_word = False
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word: 
            if c not in node.children: 
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if word is None: 
            return False
        return self.search_helper(self.root, word, 0)
    
    def search_helper(self, node, word, index): 
        if node is None: 
            return False
        
        if index >= len(word): 
            return node.is_word
        
        char = word[index]
        if char != '.': 
            return self.search_helper(node.children.get(char), word, index + 1)
        # if char == '.'
        for child in node.children: 
            if self.search_helper(node.children[child], word, index + 1) == True: 
                return True
            
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
