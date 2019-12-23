from data_structures import Graph, Stack


def dfs(graph: Graph, start_node: str, target_node: str, visited_nodes: set):
    stack = Stack()
    stack.push(start_node)

    while not stack.is_empty():
        current = stack.pop()
        if current == target_node:
            return True

        adj = graph.get_edges_node(current)
        for node in adj:
            if node not in visited_nodes:
                stack.push(node)
    return False


a = Graph(["0", "1", "2", "3", "5", "6"], [
    ("0", "1"), ("1", "3"), ("2", "3"), ("2", "5"), ("1", "6")])


print(dfs(a, "0", "3", visited_nodes=set()))

