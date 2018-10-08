def depth_first_search(node):
    visited = []
    if node is None:
        return visited
    graph_traverse(node, visited)
    return visited


def graph_traverse(node, visited):
    visited.append(node)
    for adj_node in node.adjacent:
        if adj_node not in visited:
            graph_traverse(adj_node, visited)
