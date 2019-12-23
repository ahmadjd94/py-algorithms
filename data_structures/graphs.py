class Graph:
    def __init__(self, nodes, edges):
        self.nodes = {}

        for i in set(nodes):
            self.add_node(i)

        for j in edges:
            self.add_edge(j[0], j[1])

    def add_node(self, name):
        self.nodes[name] = {"edges": []}

    def add_edge(self, node1, node2):
        self.nodes[node1]["edges"].append(node2)

    def get_edges_node(self, node: str):
        return self.nodes[node]["edges"]

    def got_edge(self,node1,node2):
        return node2 in self.nodes[node1]["edges"]
