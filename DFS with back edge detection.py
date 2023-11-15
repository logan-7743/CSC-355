class Vertex:
    def __init__(self, name):
        self.name = name
        self.color = "W"
        self.time = 0
        self.pred = None
        self.adj = []
        self.path = None
        self.back_num=0

    def __repr__(self):
        return str(self.name)
time = 0

def DFSVisit(v, time):
    v.color = "G"
    time += 1
    for edges in v.adj:
        if edges.color == "G":
            # Cycle detection logic remains unchanged
            print(f"Cycle {vertex}->{edges}")
        elif edges.color == "W":
            edges.color = "G"
            edges.pred = v
            edges.time = time
            time = DFSVisit(edges, time)

    v.color = "B"
    time += 1
    return time

def DFS(vertices):
    time = 0  # Initialize time for the traversal
    for vertex in vertices:
        if vertex.color == "W":
            time = DFSVisit(vertex, time)
    return time


vertices = []

with open("network.txt") as file:
    for line in file:
        cur = line.split()
        from_name = cur[0]
        to_name = cur[1]

        from_vertex = next((v for v in vertices if v.name == from_name), None)
        to_vertex = next((v for v in vertices if v.name == to_name), None)

        if not from_vertex:
            from_vertex = Vertex(from_name)
            vertices.append(from_vertex)
        if not to_vertex:
            to_vertex = Vertex(to_name)
            vertices.append(to_vertex)

        from_vertex.adj.append(to_vertex)
        from_vertex.adj = sorted(from_vertex.adj, key=lambda x: x.name)

vertices = sorted(vertices, key=lambda x: x.name)
for vertex in vertices:
    print(f"Vertex: {vertex}, Adjacency List: {[adj for adj in vertex.adj]}")
time = DFS(vertices)

print(f"Done in time {time}")
