class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            
            current = current.children[ch]
        
        current.is_word = True
        

    def search(self, word: str) -> bool:

        def dfs(index, node):
            if len(word) == index:
                return node.is_word
            
            ch = word[index]

            if ch != '.':
                if ch not in node.children:
                    return False

                return dfs(index+1, node.children[ch])
            else:
                for child  in node.children.values():
                    if dfs(index+1, child):
                        return True
                
                return False

        return dfs(0,self.root)

    
        
