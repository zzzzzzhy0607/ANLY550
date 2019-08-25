#### Programming Assignment 2
#### Heng Zhou, Hongyang Zheng


# Import necessary libraries
import sys
import random
import math


# Create a class for union-find data structure
class UnionFind:
    
    # Create a new empty union-find structure.
    def __init__(self):
        self.weights = {}
        self.parents = {}
        
    # Find and return the name of the set containing v.
    def __getitem__(self, v):
        # Check for previously unknown object
        if v not in self.parents:
            self.parents[v] = v
            self.weights[v] = 1
            return v

        # Find path of vertices leading to the root
        path = [v]
        root = self.parents[v]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # Compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root
    
    # Iterate through all items or unioned by this structure.
    def __iter__(self):
        return iter(self.parents)
    
    # Find the sets containing the objects and merge them all.
    def union(self, *objects):
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r], r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest


# Function for Kruskal's algorithm to return the minimum spanning tree of a graph G
def MST(G):
    
    # Initialize union-find data structure
    subtrees = UnionFind()
    # Initialize the list to store the final results
    tree = []
    
    # G[u][v] gives the length of edge u,v and G[u] gives the neighbors of u
    for w, u, v in sorted((G[u][v], u, v) for u in G for v in G[u]):
        if subtrees[u] != subtrees[v]:
            tree.append((u, v))
            subtrees.union(u, v)
            
    # The tree is returned as a list of edges.
    return tree


if __name__ == "__main__":
    
    # Take arguments 
    if sys.argv[1] != "0" or len(sys.argv) != 5:
        print("python randmst.py 0 numpoints numtrials dimension")
    if sys.argv[4] > "4" or sys.argv[4] == "1":
        print("Wrong Input Dimension! It can only be 0, 2, 3, and 4.")
    else:
        numpoints = sys.argv[2]
        numtrials = sys.argv[3]
        dimension = sys.argv[4]

    # Create a list to store the weight
    mst_weight = []
    n = int(numpoints)
    
    for i in range(int(numtrials)):
        G = {}
        for u in range(n):
            G[u] = {}
        
        # For different dimensions we have different methods to generate the graph
        if dimension == "0":
            for u in range(n):
                for v in range(u):
                    if v != u:
                        e = random.uniform(0, 1)
                        # Throw away large edges for n >= 512
                        if n < 512 or e < math.log(n, 2) / n:
                            G[u][v] = e
                            G[v][u] = G[u][v]

        elif dimension == "2":
            for u in range(n):
                x1 = random.uniform(0, 1)
                y1 = random.uniform(0, 1)
                for v in range(u):
                    if v != u:
                        x2 = random.uniform(0, 1)
                        y2 = random.uniform(0, 1)
                        e = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                        # Save time for big values
                        if e < 2.0 / math.log(n, 2):
                            G[u][v] = e
                            G[v][u] = G[u][v]

        elif dimension == "3":
            for u in range(n):
                x1 = random.uniform(0, 1)
                y1 = random.uniform(0, 1)
                z1 = random.uniform(0, 1)
                for v in range(u):
                    if v != u:
                        x2 = random.uniform(0, 1)
                        y2 = random.uniform(0, 1)
                        z2 = random.uniform(0, 1)
                        e = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
                        # Save time for big values
                        if e < 3.0 / math.log(n, 2):
                            G[u][v] = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
                            G[v][u] = G[u][v]

        elif dimension == "4":
            for u in range(n):
                x1 = random.uniform(0, 1)
                y1 = random.uniform(0, 1)
                z1 = random.uniform(0, 1)
                w1 = random.uniform(0, 1)
                for v in range(u):
                    if v != u:
                        x2 = random.uniform(0, 1)
                        y2 = random.uniform(0, 1)
                        z2 = random.uniform(0, 1)
                        w2 = random.uniform(0, 1)
                        e = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2 + (w1 - w2) ** 2)
                        # Save time for big values
                        if e < 4.0 / math.log(n, 2):
                            G[u][v] = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2 + (w1 - w2) ** 2)
                            G[v][u] = G[u][v]
                            
        # Find the minimum spinning tree                    
        T = MST(G)
        # Calculate the sum of the weights
        mst_weight.append(sum([G[u][v] for u, v in T]))
    
    # Print the results
    print(sum(mst_weight)/(int(numtrials)), numpoints, numtrials, dimension)
