# # c++ class def pseudocode
# class TrieNode:
#     def __init__(self, letter):
#         self.nodes = Array<TrieNode*>[27] # extra for end symbol *
#         self.letter = letter

class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.node = TrieNode()

        # can also use a tree of dictionaries instead of trieNodes 
        # if u do this approach you need a delimter to know when an end exists for a word

    def insert(self, word: str) -> None:
        curNode = self.node

        for c in word:
            if c in curNode.nodes:
                curNode = curNode.nodes[c]
                continue
            
            curNode.nodes[c] = TrieNode()
            curNode = curNode.nodes[c]
        
        curNode.isWord = True

    def search(self, word: str) -> bool:
        curNode = self.node

        for c in word:
            if c not in curNode.nodes:
                return False
            
            curNode = curNode.nodes[c]
        
        return curNode.isWord
        

    def startsWith(self, prefix: str) -> bool:
        curNode = self.node

        for c in prefix:
            if c not in curNode.nodes:
                return False
            
            curNode = curNode.nodes[c]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
