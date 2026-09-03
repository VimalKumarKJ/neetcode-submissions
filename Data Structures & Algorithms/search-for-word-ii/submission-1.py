class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        result = []

        trie = Trie()
        for w in words:
            trie.insert(w)
        
        def dfs(row, col, node):
            char = board[row][col]

            if char not in node.children:
                return
            
            next_node = node.children[char]

            if next_node.is_end:
                result.append(next_node.word)
                next_node.is_end = False
            
            board[row][col] = '#'

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = row+dr, col+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc, next_node)
            
            board[row][col] = char

            if not next_node.children:
                del node.children[char]
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root)
        
        return result

        