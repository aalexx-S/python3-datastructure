class Trie:

    def __init__(self):
        self.s = ''
        self.isroot = True
        self._tran = {}
        self.end = False

    def tran(self, k):
        if k not in self._tran:
            self._tran[k] = Trie()
            self._tran[k].isroot = False
        return self._tran[k]

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if self.isroot:
            self.tran(word[0]).insert(word)
            return
        if not len(self.s):
            self.s = word
            self.end = True
            return
        assert(self.isroot or self.s[0] == word[0])
        i = 0
        while i < len(self.s) and i < len(word) and word[i] == self.s[i]:
            i += 1
        if len(self.s) == len(word) and i == len(self.s):
            # equal
            self.end = True
            return
        if i == len(self.s):
            # self.s is prefix of word
            # split the rest of word to subtree
            self.tran(word[i]).insert(word[i:])
        elif i == len(word):
            # word is prefix of self.s
            # split the reset of self.s to subtree
            tmp = self.s[i:]
            self.s = word
            tmp_tran = self._tran
            self._tran = {}
            self.tran(tmp[0])._tran = tmp_tran
            self.tran(tmp[0]).insert(tmp)
            self.tran(tmp[0]).end = self.end
            self.end = True
        else:
            # word and self.s differ from pos i
            # split tree
            tmp_s = self.s[i:]
            tmp_w = word[i:]
            self.s = self.s[:i]
            tmp_tran = self._tran
            self._tran = {}
            self.tran(tmp_s[0])._tran = tmp_tran
            self.tran(tmp_s[0]).insert(tmp_s)
            self.tran(tmp_s[0]).end = self.end
            self.end = False
            self.tran(tmp_w[0]).insert(tmp_w)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if self.isroot:
            return self.tran(word[0]).search(word)
        i = 0
        if not len(self.s): return False
        while i < len(self.s) and i < len(word) and word[i] == self.s[i]:
            i += 1
        if len(word) == len(self.s) and i == len(word):
            return self.end
        if i == len(self.s):
            # self.s is prefix of word
            # search subtree
            return self.tran(word[i]).search(word[i:])
        return False

    def startsWith(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if self.isroot:
            return self.tran(word[0]).startsWith(word)
        if not len(self.s): return False
        i = 0
        while i < len(self.s) and i < len(word) and word[i] == self.s[i]:
            i += 1
        if i == len(word):
            return True
        if i == len(self.s):
            return self.tran(word[i]).startsWith(word[i:])
        return False
