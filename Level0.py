import json
import numpy as np

inp = open("Mock-Hackathon/Student Handout/Input data/level0.json")

data = json.load(inp)
inp.close()
n_neigbour=data['n_neighbourhoods']
n_res=data['n_restaurants']
restaurants=data['restaurants']
neighbourhoods=data['neighbourhoods']
vehicles=list(data['vehicles'].keys())
res_to_neighbour=restaurants['r0']['neighbourhood_distance']
adj_matrix=[[0]+res_to_neighbour]
c=0
for i in neighbourhoods:
    adj_matrix.append([res_to_neighbour[c]]+neighbourhoods[i]['distances'])
    c+=1


def nearest_neighbor(adj_matrix):
    n = len(adj_matrix)
    visited = np.zeros(n, dtype=bool)
    path = []
    cost = 0
    start_vertex = 0  
    current_vertex = start_vertex
    path.append('r'+str(current_vertex))
    visited[current_vertex] = True

    for _ in range(n - 1):
        nearest_neighbor = np.argmin([adj_matrix[current_vertex][i] for i in range(n) if not visited[i]])
        next_vertex = [i for i in range(n) if not visited[i]][nearest_neighbor]
        path.append('n'+str(next_vertex-1))
        cost += adj_matrix[current_vertex][next_vertex]
        visited[next_vertex] = True
        current_vertex = next_vertex

    path.append('r'+str(start_vertex))
    cost += adj_matrix[current_vertex][start_vertex]

    return path, cost

adj_matrix = np.array(adj_matrix)
path, cost = nearest_neighbor(adj_matrix)
print(cost)
print(path)

result={}
d={}
d['path']=path
result[vehicles[0]]=d
print(result)

with open("Mock-Hackathon/level0_output.json", "w") as outfile:
    json.dump(result, outfile)

"""out=open("Mock-Hackathon/Student Handout/Sampleoutput/level0_output.json")

output = json.load(out)
print(output)
 
out.close()"""

  
 

 
