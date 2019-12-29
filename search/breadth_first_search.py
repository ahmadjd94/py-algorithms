from data_structures import Graph, Queue


def bfs(graph: Graph, start_node: str, target_node: str, visited_nodes: set):
    queue = Queue()
    queue.enqueue(start_node)

    while not queue.is_empty():
        current = queue.deque()

        if current == target_node:
            return True

        adj = graph.get_edges_node(current)
        for node in adj:
            if node not in visited_nodes:

                queue.enqueue(node)
        visited_nodes.add(current)

    return False
