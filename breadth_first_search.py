from data_structures import Graph, Stack, Queue


def bfs(graph: Graph, start_node: str, target_node: str, visited_nodes: set):
    queue = Queue()
    queue.enqueue(start_node)

    while not queue.is_empty():
        current = queue.deque()
        print(current)

        if current == target_node:
            return True

        adj = graph.get_edges_node(current)
        for node in adj:
            if node not in visited_nodes:

                queue.enqueue(node)
        visited_nodes.add(current)

    return False


a = Graph(["0", "1", "2", "3", "5", "6"], [
    ("0", "1"), ("1", "2"), ("1", "6"), ("2", "5"),("2", "3")])


print(bfs(a, "0", "3", visited_nodes=set()))
