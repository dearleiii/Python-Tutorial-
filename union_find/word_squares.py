"""
Prunning: 
  for row_index in range(curr_index, n): 
            prefix = ''.join([square[i][row_index] for i in range(curr_index)])
            if trie.find(prefix) is None: 
                return 
"""

class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.is_word = False
        self.word_list = []
        
class Trie: 
    def __init__(self): 
        self.root = TrieNode()
    
    def add(self, word): 
        node = self.root
        for c in word: 
            if c not in node.children: 
                node.children[c] = TrieNode()
            node = node.children[c]
            node.word_list.append(word)
        node.is_word = True
        
    def find(self, word):
        node = self.root
        for c in word: 
            if c not in node.children: 
                return None
            node = node.children[c]
            
        return node
    
    def get_words_with_prefix(self, prefix): 
        node = self.find(prefix)
        return [] if node is None else node.word_list
    
    def contains(self, word): 
        node = self.find(word)
        return node is not None and node.is_word
        
class Solution:
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        trie = Trie()
        for word in words: 
            trie.add(word)
        
        squares = []
        for word in words: 
            self.search(trie, [word], squares)
            
        return squares 
    
    def search(self, trie, square, squares): 
        n = len(square[0])
        curr_index = len(square)
        if curr_index == n: 
            squares.append(list(square))
            return 
        
        # Prunning
        for row_index in range(curr_index, n): 
            prefix = ''.join([square[i][row_index] for i in range(curr_index)])
            if trie.find(prefix) is None: 
                return 
            
        prefix = ''.join([square[i][curr_index] for i in range(curr_index)])        
        for word in trie.get_words_with_prefix(prefix): 
            square.append(word)
            self.search(trie, square, squares)
            square.pop()
        
    
