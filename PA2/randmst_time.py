#### Programming Assignment 2
#### Heng Zhou, Hongyang Zheng
#### This program is for measureing run time


# Import necessary libraries
import random
import math
import time


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
    
    # Try dimension 0, 2, 3, 4
    for dimension in ['0', '2', '3', '4']:
        
        # Try n 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16348
        numbers = ['16', '32', '64', '128', '256', '512', '1024', '2048', '4096', '8192', '16348']
    
        for number in numbers:
            n=int(number)
            
            # Start time for generating graph
            t0 = time.time()
            mst_weight = []
            
            # 5 trails
            for i in range(5):
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
                                
                # End time for generating graph
                # Start time for MST
                t1 = time.time()
                
                # Generate the MST
                T = MST(G)
                mst_weight.append(sum([G[u][v] for u, v in T]))
                # End time for MST
                t2 = time.time()
                
            # Print results and time
            print(sum(mst_weight)/5, ",", n, ",", dimension)
            print(n, ",", t2 - t1, ",", t2 - t0, ",", dimension)


