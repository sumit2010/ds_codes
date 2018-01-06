class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for l in word:
            cur = cur.setdefault(l, {})

        cur['END'] = 'END'
        print self.root

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for l in word:
            if l not in cur:
                return False
            cur = cur[l]
        return 'END' in cur

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for l in prefix:
            if l not in cur:
                return False
            cur = cur[l]
        return len(cur) != 0



        # Your Trie object will be instantiated and called as such:


obj = Trie()
word = "abcd"
obj.insert(word)
param_2 = obj.search(word)
