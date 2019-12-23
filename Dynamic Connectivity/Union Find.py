MODE_EAGER = 1
MODE_QUICK = 2

class QF:

    def __init__(self,n,mode=MODE_QUICK):
        # basic initialization
        self.__nodes = [i for i in range(n)]
        self.__weights = [1 for i in range(n)]
        self.__n = n 
        self.__mode = mode

    def connected(self,a,b):
        # used to find if there are connections between a and b
        if self.__mode == MODE_EAGER:
            return self.eager_connected(a,b)
        elif self.__mode == MODE_QUICK:
            return self.quick_connected(a,b)

    def union(self,a,b):
        # connects a and b based on the mode set
        if self.__mode == MODE_EAGER:
            self.eager_union(a,b)
        elif self.__mode == MODE_QUICK:
            self.quick_union(a,b)


    # eager find to check connectivity
    def eager_connected(self,a,b):
        return self.__nodes[a] == self.__nodes[b]

    # connect two nodes by using eager approach
    def eager_union(self,a,b):
        if self.eager_connected(a,b) == False:
            valA = self.__nodes[a]
            valB = self.__nodes[b]
            for i in range(self.__n):
                if self.__nodes[i] == valB:
                    self.__nodes[i] = valA 

    # quick-union
    def find(self,a):
        # find the root of the tree
        if self.__nodes[a] != a:
            # point nodes to root
            self.__nodes[a] = self.__nodes[self.__nodes[a]]
            return self.find(self.__nodes[a])
        else:
            return a

    def quick_connected(self,a,b):
        # find the nodes conncetivity using roots
        rootA = self.find(a)
        rootB = self.find(b)
        return rootA == rootB

    def quick_union(self,a,b):
        # to connect two nodes and form a tree
        if self.quick_connected(a,b) == False:
            rootA = self.find(a)
            rootB = self.find(b)
            # based on no. of nodes available, attach the node to form a tree with small depth
            if self.__weights[rootA] < self.__weights[rootB]:
                self.__nodes[rootA] = rootB
                self.__weights[rootB] += self.__weights[rootA]
            else:
                self.__nodes[rootB] = rootA
                self.__weights[rootA] += self.__weights[rootB]



if __name__ == "__main__":
    n = 10
    edges = [(1,2),(3,4),(5,6),(5,0),(7,8),(7,9),(9,1),(2,8)]
    queries = [(5,6),(5,7),(3,4),(1,9),(0,8)]
    expected = [True,False,True,True,False]

    qf = QF(n)
    for edge in edges:
        qf.union(edge[0],edge[1])
    
    for i,query in enumerate(queries):
        print("Actual:",qf.connected(query[0],query[1]),"Real:",expected[i])