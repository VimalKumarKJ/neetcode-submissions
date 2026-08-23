class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root

        def backtrack(child_node, index):
            if index == len(word):
                return child_node.is_end
            
            char = word[index]

            if char == '.':
                for child in child_node.children.values():
                    if backtrack(child, index+1):
                        return True
                return False
            else:
                if char not in child_node.children:
                    return False
                
                return backtrack(child_node.children[char], index+1)
        return backtrack(node, 0)
                    



