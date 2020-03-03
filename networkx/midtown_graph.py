# Pulling data from the Graphattan API and converting it to a networkx graph.
# Using MultiGraph
import json
import requests
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def __eq__(self, other):
        return self.posX == other.posX and self.posY == other.posY
    
    def __hash__(self):
        return hash((self.posX, self.posY))

base_url = 'http://graphattan.us-west-1.elasticbeanstalk.com/graph?'

def read_midtown_graph_data(start_st, start_ave, start_corner, finish_st, finish_ave, finish_corner):
    url = base_url + \
        f'start_st={start_st}&start_ave={start_ave}&start_corner={start_corner}&finish_st={finish_st}&finish_ave={finish_ave}&finish_corner={finish_corner}'
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def convert_data_to_graph(data):
    pass

graph_data = read_midtown_graph_data(51, 1, 'NE', 53, 3, 'NE')
start = Node(graph_data['start']['posX'], graph_data['start']['posY'])
finish = Node(graph_data['finish']['posX'], graph_data['finish']['posY'])

graph = nx.MultiGraph()

for item in graph_data['graph']:
    vertex = item['vertex']
    for edge in item['edges']:
        source = Node(vertex['posX'], vertex['posY'])
        destination = Node(edge['destination']['posX'], edge['destination']['posY'])
        graph.add_edge(source, destination, weight=edge['weight'], type=edge['type'])

print(graph.number_of_edges())

positions = {n: (n.posX, n.posY) for n in graph.nodes}
# nx.draw_networkx_nodes(graph, pos=positions)
sidewalks = [e for e in graph.edges(data=True) if e[2]['type'] == 'SIDEWALK']
crossings = [e for e in graph.edges(data=True) if e[2]['type'] == 'CROSSING']
# sidewalks
nx.draw_networkx(graph, pos=positions, edgelist=sidewalks, edge_color='b', with_labels=False)
# crossings
nx.draw_networkx(graph, pos=positions, edgelist=crossings, edge_color='purple', with_labels=False)
# plt.xticks(ticks=[x for x in positions.values])
plt.xlabel('x-position relative to starting point (ft)')
plt.ylabel('y-position relative to starting point (ft)')
plt.show()

# color start and finish

# add xticks and yticks

# reduce dot size

# sanity check traversals against neworkx pathfinding library
# GraphvizAnim.. consider switching 
