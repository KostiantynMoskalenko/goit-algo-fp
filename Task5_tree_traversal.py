import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            e_left = x - 1 / 2 ** layer
            pos[node.left.id] = (e_left, y - 1)
            e_left = add_edges(graph, node.left, pos, x=e_left, y=y - 1,
                               layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            e_right = x + 1 / 2 ** layer
            pos[node.right.id] = (e_right, y - 1)
            e_right = add_edges(graph, node.right, pos, x=e_right, y=y - 1,
                                layer=layer + 1)
    return graph


def depth_first_traversal(node, colors):
    if node is None:
        return
    colors[node.id] = generate_color(len(colors))
    depth_first_traversal(node.left, colors)
    depth_first_traversal(node.right, colors)


def breadth_first_traversal(node, colors):
    queue = [node]
    while queue:
        current_node = queue.pop(0)
        colors[current_node.id] = generate_color(len(colors))
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)


def generate_color(index):
    base_color = 101010
    base_color = base_color + index * 101010
    color = "#" + str(base_color)
    return color


def draw_tree(tree_root, traversal_type):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = {}
    title = ''
    if traversal_type == 'DFS':
        depth_first_traversal(tree_root, colors)
        title = "DFS, Depth-first search traversal"
    elif traversal_type == 'BFS':
        breadth_first_traversal(tree_root, colors)
        title = "BFS, Breadth-first search traversal"
    # Використання значення вузла для міток
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    draw_colors = []
    for key, _ in labels.items():
        draw_colors.append(colors[key])

    plt.figure(figsize=(8, 8))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, font_color="#AFEEEE",
            font_weight="bold", font_size=19, arrows=False,
            node_size=2500, node_color=draw_colors)
    plt.show()


if __name__ == "__main__":
    # Створюємо дерево
    root = Node(90)
    root.left = Node(78)
    root.left.left = Node(77)
    root.left.right = Node(6)
    root.right = Node(42)
    root.right.left = Node(8)
    root.right.right = Node(1)

    # Зробимо обхід дерева в глибину з візуалізацією
    draw_tree(root, 'DFS')

    # Зробимо обхід дерева в ширину з візуалізацією
    draw_tree(root, 'BFS')
