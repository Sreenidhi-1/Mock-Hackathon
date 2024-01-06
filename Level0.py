import json
import numpy as np

inp = open("Mock-Hackathon/Student Handout/Input data/level0.json")

data = json.load(inp)
inp.close()
n_neigbour=data['n_neighbourhoods']
n_res=data['n_restaurants']
restaurants=data['restaurants']
neighbourhoods=data['neighbourhoods']
res_to_neighbour=restaurants['r0']['neighbourhood_distance']
adj_matrix=[[0]+res_to_neighbour]
c=0
for i in neighbourhoods:
    adj_matrix.append([res_to_neighbour[c]]+neighbourhoods[i]['distances'])
    c+=1

print(len(adj_matrix))



import numpy as np

def nearest_neighbor(adj_matrix):
    n = len(adj_matrix)
    visited = np.zeros(n, dtype=bool)
    path = []
    cost = 0

    start_vertex = 0  

    current_vertex = start_vertex
    path.append(current_vertex)
    visited[current_vertex] = True

    for _ in range(n - 1):
        nearest_neighbor = np.argmin([adj_matrix[current_vertex][i] for i in range(n) if not visited[i]])
        next_vertex = [i for i in range(n) if not visited[i]][nearest_neighbor]
        path.append(next_vertex)
        cost += adj_matrix[current_vertex][next_vertex]
        visited[next_vertex] = True
        current_vertex = next_vertex

    # Returning to the starting vertex to complete the cycle
    path.append(start_vertex)
    cost += adj_matrix[current_vertex][start_vertex]

    return path, cost

# Example adjacency matrix (replace it with your actual data)
adj_matrix = np.array(adj_matrix)

path, cost = nearest_neighbor(adj_matrix)

print("Path:", path)
print("Cost:", cost)

out=open("Mock-Hackathon/Student Handout/Sampleoutput/level0_output.json")

output = json.load(out)
print(output)
 
out.close()

  
 

 
