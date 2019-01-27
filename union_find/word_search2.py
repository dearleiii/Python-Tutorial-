# Note 1: 
    # visited.add((x_, y_)) 
    # after searching one postion, need to             visited.remove((x_, y_))

# Note 2: 
    """  if node.is_word: 
            result.add(node.word)
            return
    """ 
    # Reason: in one trie branch, might have multiple words, need ot keep searching until the end 
    # i.e. ["see", "se"]
  
# Note 3: 
    """
    Trie no need of extra functions since no search here, only need to check child node: 
    self.search_helper(board,
                trie.root.children.get(c),
                i, j, 
                visited, result)
                visited.remove((i, j))
    """

DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        node.word = word
        
    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
                
        return node
    
class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if board is None or len(board) == 0:
            return []
            
        trie = Trie()
        for word in words:
            trie.add(word)

        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                self.search(
                    board,
                    i,
                    j,
                    trie.root.children.get(c),
                    set([(i, j)]),
                    result,
                )
                
        return list(result)
    
    def search(self, board, x, y, node, visited, result):
        if node is None:
            return
        
        if node.is_word:
            result.add(node.word)
        
        for delta_x, delta_y in DIRECTIONS:
            x_ = x + delta_x
            y_ = y + delta_y
            
            if not self.inside(board, x_, y_):
                continue
            if (x_, y_) in visited:
                continue
            
            visited.add((x_, y_))
            self.search(board, x_, y_, 
                       node.children.get(board[x_][y_]), 
                       visited, result, )
            visited.remove((x_, y_))
            
    def inside(self, board, x, y): 
        return 0 <= x < len(board) and 0 <= y < len(board[0])
    
