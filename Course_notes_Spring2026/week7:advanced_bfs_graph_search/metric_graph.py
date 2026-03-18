import networkx as nx
import numpy as np

# Step 1: Generate some points in 2D space
num_nodes = 5
points = np.random.rand(num_nodes, 2)  # random points in [0,1]x[0,1]

# Step 2: Create an empty graph
G = nx.Graph()

# Step 3: Add nodes with coordinates
for i, (x, y) in enumerate(points):
    G.add_node(i, pos=(x, y))

# Step 4: Add edges with Euclidean distance as weight
for i in range(num_nodes):
    for j in range(i+1, num_nodes):
        distance = np.linalg.norm(points[i] - points[j])
        G.add_edge(i, j, weight=distance)

# Step 5: Optional - Draw the graph with edge weights
import matplotlib.pyplot as plt

pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500)
edge_labels = nx.get_edge_attributes(G, 'weight')
# Round distances for display
edge_labels_rounded = {k: f"{v:.2f}" for k, v in edge_labels.items()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels_rounded)
plt.show()