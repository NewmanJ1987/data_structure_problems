def breadth_first_search(node):
    to_return = {}
    visited = []
    level = 0
    if node is None:
        return to_return
    graph_traverse(level, node, to_return, visited)
    return to_return


def graph_traverse(level, node, to_return, visited):
    insert_node(level, node, to_return, visited)
    for adj_node in node.adjacent:
        if adj_node not in visited:
            graph_traverse(level + 1, adj_node, to_return, visited)


def insert_node(level, node, to_return, visited):
    visited.append(node)
    if to_return.get(level):
        to_return.get(level).append(node)
    else:
        to_return.update({level: []})
        to_return.get(level).append(node)
