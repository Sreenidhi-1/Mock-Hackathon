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

#12440
sample_path=[]
def nearest_neighbor(adj_matrix):
    n = len(adj_matrix)
    visited = np.zeros(n, dtype=bool)
    path = []
    cost = 0
    start_vertex = 0  
    current_vertex = start_vertex
    path.append('r'+str(current_vertex))
    sample_path.append(current_vertex)
    visited[current_vertex] = True

    for _ in range(n - 1):
        nearest_neighbor = np.argmin([adj_matrix[current_vertex][i] for i in range(n) if not visited[i]])
        next_vertex = [i for i in range(n) if not visited[i]][nearest_neighbor]
        path.append('n'+str(next_vertex-1))
        sample_path.append(next_vertex)
        cost += adj_matrix[current_vertex][next_vertex]
        visited[next_vertex] = True
        current_vertex = next_vertex

    path.append('r'+str(start_vertex))
    sample_path.append(start_vertex)
    cost += adj_matrix[current_vertex][start_vertex]

    return sample_path,path, cost

adj_matrix = np.array(adj_matrix)
sample_path,path, cost = nearest_neighbor(adj_matrix)
print(cost)
print(path)

initial_tour=list(sample_path)
print(initial_tour)
result={}
d={}
d['path']=path
result[vehicles[0]]=d
print(result)


def calculate_tour_cost(tour, adj_matrix):
    n = len(tour)
    total_cost = 0

    for i in range(n):
        total_cost += adj_matrix[tour[i - 1]][tour[i]]

    return total_cost

optimised_path=[]
def two_opt_swap(tour, adj_matrix):
    n = len(tour)
    print(tour)
    improvement = True

    while improvement:
        improvement = False
        for i in range(1, n - 2):
            for j in range(i + 1, n):
                if j - i == 1:
                    continue  

                current_distance = (
                    adj_matrix[tour[i - 1]][tour[i]]
                    + adj_matrix[tour[j - 1]][tour[j]]
                )

                new_distance = (
                    adj_matrix[tour[i - 1]][tour[j - 1]]
                    + adj_matrix[tour[i]][tour[j]]
                )


                if new_distance < current_distance:
                    tour[i:j] = reversed(tour[i:j])
                    #print(tour)
                    improvement = True
                #print(tour)

    final_cost = calculate_tour_cost(tour, adj_matrix)
    return tour, final_cost



optimized_tour, final_cost = two_opt_swap(initial_tour[:-1], adj_matrix)

print("Initial Tour:", sample_path)
print("Optimized Tour:", optimized_tour)
print("Final Cost:", final_cost)

optimised_path.append('r'+str(optimized_tour[0]))
for i in optimized_tour[1:(len(optimized_tour))]:
    optimised_path.append('n'+str(i-1))
optimised_path.append('r'+str(0))
print(len(optimised_path))
result={}
d={}
d['path']=optimised_path
result[vehicles[0]]=d
print(result)

with open("Mock-Hackathon/level0_output.json", "w") as outfile:
    json.dump(result, outfile)

"""out=open("Mock-Hackathon/Student Handout/Sampleoutput/level0_output.json")

output = json.load(out)
print(output)
 
out.close()"""

  
 

 
