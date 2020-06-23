class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False            

    def insert_string(self, string):
        node = self
        # Special Character to denote end of tree
        string += "$"
        def insert_char(node, char, isEnd=False):
            if char not in node.children:
                node.children[char] = TrieNode()
            if isEnd == True:
                node.isEndOfWord = True
            return node.children[char]

        for i, char in enumerate(string):
            node = insert_char(node, char, i == len(string) - 1)
            

    def search(self, string):
        node = self
        for i,ch in enumerate(string):
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return i == len(string) - 1 and node.isEndOfWord


    def auto_suggest(self, string):
        # visit till the string characters
        node = self
        for char in string:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        items = []

        def traverse(node, prefix):
            for key in node.children:
                if node.children[key].isEndOfWord:
                    items.append(prefix + key)
                traverse(node.children[key], prefix + key)

        traverse(node, string)

        return items
        


    
if __name__ == "__main__":
    string = "apples"
    prefix = "app"
    items = ["apply", "apples", "appy"]
    root = TrieNode()
    for item in items:
        root.insert_string( item)
    print()
    print("Items added:", items)
    print("String to search '{}' Found: {}".format(string, root.search(string)))
    print("String to search '{}' Found: {}".format("apple", root.search("apple")))
    print("Lookup for word '{}': {}".format(prefix, root.auto_suggest(prefix)))