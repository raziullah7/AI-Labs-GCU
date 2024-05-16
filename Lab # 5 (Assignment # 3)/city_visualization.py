### WORKS IN GOOGLE COLAB ONLY ###

import networkx as nx
import matplotlib.pyplot as plt

class CityGraph:
    def __init__(self):
        self.graph = nx.Graph()
        
    def add_edge(self, node1, node2, value):
        self.graph.add_edge(node1, node2, weight=value)
        
    def add_node(self, node, edges=None):
        self.graph.add_node(node)
        if edges:
            for edge in edges:
                self.add_edge(node, edge[0], edge[1])
                

    def visualize(self):
        pos = nx.spring_layout(self.graph)
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        
        nx.draw(self.graph, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=15, font_color="black", font_weight="bold", edge_color="gray")
        
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.show()


city_graph = CityGraph()
city_graph.add_edge("Lahore", "Karachi", 4500)
city_graph.add_edge("Lahore", "Islamabad", 1200)
city_graph.add_edge("Karachi", "Multan", 3200)
city_graph.add_edge("Islamabad", "peshawar", 1500)
city_graph.add_edge("Lahore", "Peshawar", 2000)
city_graph.add_edge("Multan", "Peshawar", 2200)

city_graph.visualize()

city_graph.add_node("Quetta")
city_graph.add_edge("Quetta", "Lahore", 7000)

city_graph.visualize()