class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                currNode.children[char] = TrieNode()
            currNode = currNode.children[char]
        currNode.eow = True

    def search(self, word):
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                return False
            currNode = currNode.children[char]
        return currNode.eow

    def startsWith(self, prefix):
        currNode = self.root
        for char in prefix:
            if char not in currNode.children:
                return False
            currNode = currNode.children[char]
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        dd = defaultdict(list)
        trie = Trie()
        for word in words:
            trie.insert(word)

        ret = ''

        for word in words:
            if len(word) < len(ret):
                continue

            curr = trie.root

            for char in word:
                curr = curr.children[char]
                if not curr.eow:
                    break
                    
            if curr.eow and (len(word)>len(ret) or (len(word)==len(ret) and word<ret)):
                ret = word

        return ret 