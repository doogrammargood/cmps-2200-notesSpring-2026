import networkx as nx
import random

def windowed_path_graph(n=200, m=250, window=10, seed=None):
    """
    Args:
        n is the number of vertices
        m is the number of edges.
        window is how far apart the edges can be.
    Returns:
        A graph with the given parameters.
        It is formed by starting with a path
        and adding edges between randomly selected pairs of
        vertices that are not more than window apart on the path.
    """

    if seed is not None:
        random.seed(seed)

    G = nx.path_graph(n)
    edges = set(tuple(sorted(e)) for e in G.edges())

    target = m

    while G.number_of_edges() < target:
        u = random.randrange(n)
        v = u + random.randint(-window, window)

        if v < 0 or v >= n:
            continue
        if u == v:
            continue

        e = (min(u, v), max(u, v))
        if e in edges:
            continue

        G.add_edge(u, v)
        edges.add(e)

    return G
import networkx as nx

def modular_band_graph(n=200, k=5):
    """
    Each vertex connects to next k vertices (no wrap-around).
    Treewidth = k
    """
    G = nx.Graph()
    G.add_nodes_from(range(n))

    for i in range(n):
        for j in range(1, k+1):
            if i + j < n:
                G.add_edge(i, i + j)

    return G
#G=modular_band_graph()
#G = nx.circulant_graph(200, [1,2,3])

#Graphs with small enough treewidth
#example_graphs = [nx.circulant_graph(200, [1,2,3])]
import networkx as nx
import random

def generate_cactus(n_nodes: int, n_cycles: int, cycle_size_range=(3, 6)):
    """
    Generate a connected cactus graph with:
      - approximately n_nodes nodes
      - exactly n_cycles cycles (if feasible)
    """

    if n_cycles == 0:
        return nx.path_graph(n_nodes)

    G = nx.Graph()
    next_node = 0

    # ---- helper: create first cycle ----
    first_size = min(n_nodes, random.randint(*cycle_size_range))
    first_cycle = list(range(next_node, next_node + first_size))
    G.add_edges_from(zip(first_cycle, first_cycle[1:] + first_cycle[:1]))

    next_node += first_size
    used_nodes = first_size
    cycles_left = n_cycles - 1

    attachment_points = first_cycle[:]

    # ---- add remaining cycles ----
    while cycles_left > 0 and used_nodes < n_nodes:
        attach = random.choice(attachment_points)

        max_new = n_nodes - used_nodes
        if max_new <= 1:
            break

        size = random.randint(3, min(max_new + 1, cycle_size_range[1]))

        # cycle uses 1 existing node + (size-1) new nodes
        new_nodes = list(range(next_node, next_node + size - 1))
        next_node += size - 1
        used_nodes += size - 1

        cycle = [attach] + new_nodes

        G.add_edges_from(zip(cycle, cycle[1:] + cycle[:1]))

        attachment_points.extend(new_nodes)
        cycles_left -= 1

    return G