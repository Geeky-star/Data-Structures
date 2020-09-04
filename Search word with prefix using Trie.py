
class TrieNode:

    def __init__(self):
        self.children=[None]*26
        self.isendofword=False
        self.count=0

class Trie:

    def __init__(self):
        self.root=self.getNode()

    def getNode(self):
        return TrieNode()

    def insert(self,key):

        crawl=self.root
        length = len(key)

        for i in range(length):
            index = ord(key[i])-ord('a')

            if not crawl.children[index]:
                crawl.children[index] = self.getNode()
            crawl = crawl.children[index]
            crawl.count+=1

        crawl.isendofword=True
        

    def search(self,key):
        crawl = self.root
        length = len(key)

        for i in range(length):
            index=ord(key[i])-ord('a')
            if not crawl.children[index]:
                return c
            crawl=crawl.children[index]

        return crawl.count


t = int(input())
tr=Trie()
for i in range(t):
    s = input()
    if s[0]=='a':
        s = s[4:]
        tr.insert(s)
        
    else:
        s = s[5:]
        c=0
        print(tr.search(s))
        
