import json
import numpy as np
import copy

inp = open("Mock-Hackathon/Student Handout/Input data/level1a.json")

data = json.load(inp)
print(data)
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
total_capacity=data['vehicles'][vehicles[0]]['capacity']
demand=[total_capacity]
for i in neighbourhoods:
    demand.append(neighbourhoods[i]['order_quantity'])

print(demand)




"""def calculate_savings(distance_matrix):
    n = len(distance_matrix)
    savings = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            if i != j:
                savings[i, j] = distance_matrix[0, i] + distance_matrix[0, j] - distance_matrix[i, j]
                
    return savings


def construct_routes(distance_matrix, capacity_constraint, demand):
    n = len(distance_matrix)
    savings = calculate_savings(distance_matrix)
    savings_list = [(i, j, savings[i, j]) for i in range(n) for j in range(n) if i != j]
    savings_list = sorted(savings_list, key=lambda x: x[2], reverse=True)

    print(savings_list)

    visited_nodes = set()
    vehicle_routes = []
    current_route = [0]  
    current_load = 0

    def exceeds_capacity(route, load):
        return load > capacity_constraint

    def calculate_route_distance(route):
        distance = 0
        for i in range(len(route) - 1):
            distance += distance_matrix[route[i]][route[i + 1]]
        return distance

    def apply_2_opt(route):
        best_route = copy.deepcopy(route)
        best_distance = calculate_route_distance(route)

        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                new_route = route[:i] + list(reversed(route[i:j])) + route[j:]
                new_distance = calculate_route_distance(new_route)

                if new_distance < best_distance:
                    best_route = new_route
                    best_distance = new_distance

        return best_route

    for i, j,savings in savings_list:
        if i not in visited_nodes and j not in visited_nodes  :
            if current_load + demand[j] <= capacity_constraint:
                current_route.extend([i, j])
                current_load += demand[j]
                visited_nodes.update([i, j])
            elif len(current_route) > 2:  
                current_route.append(0) 
                vehicle_routes.append(current_route)
                current_route = [0, i, j, 0]
                current_load = demand[j]
                visited_nodes.update([i, j])

   
    if len(current_route) > 2:
        current_route.append(0)  
        vehicle_routes.append(current_route)

    # Optimize routes using 2-opt
    optimized_routes = [apply_2_opt(route) for route in vehicle_routes]

    return optimized_routes


adj_matrix = np.array(adj_matrix)



result_routes = construct_routes(adj_matrix, total_capacity,demand)

def result_path(route):
    res=['r0']
    for i in route[1:-1]:
        res.append('n'+str(i))
    res.append('r0')
    print(res)
    return res

print("Result Routes:")
x=1
d={}
result={}
for i in result_routes:
    print(len(i))
    print(i)
    d['path'+str(x)]=result_path(i)
    x+=1
result[vehicles[0]]=d
print(result)"""

sample_path=[]
result=[]
capacity1=[]
cost1=[]
def nearest_neighbor(adj_matrix):
    n = len(adj_matrix)
    visited = [i for i in range(n)]
      
    visited.remove(0)
    print(visited)
    capacity=600
    while(True):
        path = []
        cost = 0
        start_vertex = 0  
        current_vertex = start_vertex
        path.append('r'+str(current_vertex))
        sample_path.append(current_vertex)
        load=0
        for _ in range(1,n):
            l=[adj_matrix[current_vertex][i] for i in range(n) if i in visited]
           
            if(l!=[]):
                nearest_neighbor = np.argmin(l)
                next_vertex = [i for i in range(n) if i in  visited][nearest_neighbor]
                print(nearest_neighbor,next_vertex)
                if((load+demand[next_vertex])<=capacity):
                    path.append('n'+str(next_vertex-1))
                    sample_path.append(next_vertex)
                    load+=demand[next_vertex]
                    cost += adj_matrix[current_vertex][next_vertex]
                    visited.remove(next_vertex)
                    current_vertex = next_vertex
                    print(path)
                else:
                    path.append('r'+str(start_vertex))
                    sample_path.append(start_vertex)
                    cost += adj_matrix[current_vertex][start_vertex]
                    result.append(path)
                    cost1.append(cost)
                    capacity1.append(load)
                    load=0
                    print(path,load)  
                    break
            else:
                break  
        
        if(visited==[]):
            break
    result.append(path)
    cost1.append(cost)
    capacity1.append(load)
    return result,cost1,capacity

adj_matrix = np.array(adj_matrix)
final,cost1,capacity = nearest_neighbor(adj_matrix)
print(final,cost1,capacity1)
print("Result Routes:")
x=1
d={}
result={}
for i in final:
    print(len(i))
    print(i)
    d['path'+str(x)]=(i)
    x+=1
result[vehicles[0]]=d
print(result)

with open("Mock-Hackathon/level1a_output.json", "w") as outfile:
    json.dump(result, outfile)

"""out = open("Mock-Hackathon/Student Handout/Sampleoutput/level1a_output.json")

sample_output = json.load(out)
print(sample_output)
out.close()"""