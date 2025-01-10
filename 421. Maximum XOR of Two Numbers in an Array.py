class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = False

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
        return currNode.eow[0]

    def startsWith(self, prefix):
        currNode = self.root
        for char in prefix:
            if char not in currNode.children:
                return False
            currNode = currNode.children[char]
        return True

class Solution:

    def findMaximumXOR(self, nums: List[int]) -> int:

        trie = Trie()
        ret = -math.inf

        for num in nums:
            trie.insert(format(num, '032b'))
            
        for num in nums:
            currNode = trie.root
            temp = 0
            for bit in (format(num, '032b')):
                flippedBit = '1' if bit == '0' else '0'

                if flippedBit in currNode.children:
                    temp = (temp << 1) | 1
                    currNode = currNode.children[flippedBit]
                else:
                    temp = temp << 1
                    currNode = currNode.children[bit]

            ret = max(ret, temp)          

        return ret
            
