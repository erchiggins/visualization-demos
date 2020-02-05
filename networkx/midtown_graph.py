# Pulling data from the Graphattan API and converting it to a networkx graph.
# Using just Graph, not DiGraph or MultiGraph or MultiDiGraph.
# I KNOW there aren't parallel edges in this dataset because of Graphattan's grid generation logic.
import json
import requests

base_url = 'http://graphattan.us-west-1.elasticbeanstalk.com/graph?'

def read_midtown_graph(start_st, start_ave, start_corner, finish_st, finish_ave, finish_corner):
    url = base_url + \
        f'start_st={start_st}&start_ave={start_ave}&start_corner={start_corner}&finish_st={finish_st}&finish_ave={finish_ave}&finish_corner={finish_corner}'
    response = requests.get(url)
    graph_data = json.loads(response.text)
    return graph_data

print(read_midtown_graph(51, 1, 'NE', 53, 3, 'NE'))

