from Stack import Stack
from Graph import Graph


def dfs(g, start):
    """
    given a graph and a start point node as an input
    return list of visited nodes DFS
    """

    visited = []

    s = Stack()

    while not s.isEmpty():
        u = s.pop()
        if u not in visited:
            visited.append(u)
            for n in g.children(u):
                if n not in visited:
                    s.push(n)


    



if __name__ == "__main__":
    ### DO NOT MODIFY
    nodes = [1, 2, 3, 4, 5, 6]

    ### DO NOT MODIFY
    pairs = [(1, 2), (3, 4), (4, 6), (1, 6), (2, 3)]


    ###############################################################################
    # Complete the tasks using the Graph Class (Directional)
    print("" + "="*30 + " Directional Graph " + "="*30 + "")
    g = Graph(nodes, True) # DONE: Should be a directional graph

    # Adds all the edges to the graph
    for p in pairs:
        g.add_edge(p)
    print("dfs list:")
    print(dfs(g, 1))


