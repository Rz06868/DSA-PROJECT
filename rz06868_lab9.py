G = {}
nodes = [0, 1, 2, 3, 4, 5]
edges = [(0, 1, 1), (0, 2, 1), (1, 2, 1), (1, 3, 1), (2, 4, 1), (3, 4, 1), (3, 5, 1), (4, 5, 1)]

def addNodes(G, nodes):
    for i in nodes:
        G[i] = []
    return G
# print(addNodes(G, nodes))

G = addNodes(G, nodes)

def addEdges(G, edges, directed = False):
    if directed == True:
        for i in edges:
            a = i[0]
            for key, values in G.items():
                if a == key:
                    tuples = (i[1], i[2])
                    G[key].append(tuples)
                    break
        return G
        
    if directed == False:
        for i in edges:
            a = i[0]
            b = i[1]
            for key, values in G.items():
                if a == key:
                    tuples1 = (i[1], i[2])
                    G[key].append(tuples1)
                if b == key:
                    tuples2 = (i[0], i[2])
                    G[key].append(tuples2)
                    break
        return G
# print(addEdges(G, edges, directed = True))
# print(addEdges(G, edges, directed = False))

G = { 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
def listOfNodes(G):
    lst1 = []
    for i in G.keys():
        lst1.append(i)
    return (lst1)
# print(listOfNodes(G))

def listOfEdges(G, directed = False):
    lst1 = []
    if directed == True:
        for i in G.keys():
            a = G.get(i)
            for j in a:
                tup = (i, j[0], j[1])
                lst1.append(tup)
        return lst1

    if directed == False:
        for i in G.keys():
            a = G.get(i)
            for j in a:
                tup = (i, j[0], j[1])
                lst1.append(tup)
        return lst1
# print(listOfEdges(G, directed = True))
# print(listOfEdges(G, directed = False))

def printIn_OutDegree(G):
    lst = []
    lst0 = []
    lst1 = []
    lst2 = []
    for i in G.keys():
        a = G.get(i)
        x = len(a)
        lst0.append(i)
        lst.append(x)
        lst1.append(x)
    lst1.reverse()
    for j in lst1:
        lst2.append(j)
    for i in range(len(lst0)):
        print(lst0[i], "=> In-Degree:", lst2[i], "Out-Degree", lst[i])
# printIn_OutDegree(G)

G = { 0: [(1, 1), (2, 1)], 1: [(0, 1), (2, 1), (3, 1)], 2: [(0, 1), (1, 1), (4, 1)], 3: [(1, 1), (4, 1), (5, 1)], 4: [(3, 1), (2, 1), (5, 1)], 5: [(3, 1), (4, 1)] }
def printDegree(G):
    for i in G.keys():
        a = G.get(i)
        x = len(a)
        print(i, "=>", x)
printDegree(G)

G = { 0: [(1, 1), (2, 1)], 1: [(0, 1), (2, 1), (3, 1)], 2: [(0, 1), (1, 1), (4, 1)], 3: [(1, 1), (4, 1), (5, 1)], 4: [(3, 1), (2, 1), (5, 1)], 5: [(3, 1), (4, 1)] }
def getNeighbors(G, node):
    lst1 = []
    a = G.get(node)
    for i in a:
        lst1.append(i[0])
    return lst1
# print(getNeighbors(G, 0))

G = { 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
def getInNeighbors(G, node):
    lst = []
    for i in G.keys():
        a = G[i]
        for j in a:
            if j[0] == node:
                lst.append(i)
    return lst
# print(getInNeighbors(G, 2))

def getOutNeighbors(G, node):
    lst = []
    a = G.get(node)
    for i in a:
        lst.append(i[0])
    return lst
# print(getOutNeighbors(G, 5))

G = { 0: [(1, 21), (2, 15)], 1: [(0, 21), (2, 10), (3, 70)], 2: [(0, 15), (1, 10), (4, 50)], 3: [(1, 70), (4, 24), (5, 39)], 4: [(3, 24), (2, 50), (5, 99)], 5: [(3, 39), (4, 99)] }
def getNearestNeighbor(G, node):
    lst = []
    a = G.get(node)
    for i in a:
        lst.append(i[1])
    b = min(lst)
    for j in a:
        if j[1] == b:
            return j[0]
# print(getNearestNeighbor(G, 0))

G = { 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
def isNeighbor(G, Node1, Node2):
    lst = []
    a = G.get(Node1)
    for i in a:
        lst.append(i[0])
    if Node2 in lst:
        return True
    else:
        return False
# print(isNeighbor(G, 1, 0))

G = { 0: [(1, 1), (2, 1)], 1: [(0, 1), (2, 1), (3, 1)], 2: [(0, 1), (1, 1), (4, 1)], 3: [(1, 1), (4, 1), (5, 1)], 4: [(3, 1), (2, 1), (5, 1)], 5: [(3, 1), (4, 1)] }
def removeNode(G, node):
    G.pop(node)
    for i in G.keys():
        a = G.get(i)
        for j in range(len(a)-1, -1, -1):
            if a[j][0] == node:
                G[i].remove(a[j])
    return G
# print(removeNode(G, 1))

G = { 0: [(1, 1), (2, 1)], 1: [(0, 1), (2, 1), (3, 1)], 2: [(0, 1), (1, 1), (4, 1)], 3: [(1, 1), (4, 1), (5, 1)], 4: [(3, 1), (2, 1), (5, 1)], 5: [(3, 1), (4, 1)] }
def removeNodes(G, nodes):
    for node in range(len(nodes)):
        nod = nodes[node]
        G.pop(nod)
        for i in G.keys():
            a = G.get(i)
            for j in range(len(a)-1, -1, -1):
                if a[j][0] == nod:
                    G[i].remove(a[j])
    return G 
# print(removeNodes(G, [1, 2]))

G = { 0: [(1, 1), (2, 1)], 1: [(0, 1), (2, 1), (3, 1)], 2: [(0, 1), (1, 1), (4, 1)], 3: [(1, 1), (4, 1), (5, 1)], 4: [(3, 1), (2, 1), (5, 1)], 5: [(3, 1), (4, 1)] }
def displayGraph(G):
    return G
# print(displayGraph(G))


G = {0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [
    (4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: []}


def display_adj_matrix(G):
    lst = []
    matrix = []
    total = len(G)

    for i in G.keys():
        lst = [0 for i in range(total)]
        a = G.get(i)
        for j in a:
            v1 = j[0]
            w1 = j[1]
            lst[v1] = w1
        matrix.append(lst)
    return matrix


# print(display_adj_matrix(G))









    
