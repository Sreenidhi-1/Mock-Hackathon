import json
import numpy as np
import copy

inp = open("Mock-Hackathon/Student Handout/Input data/level1b.json")

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


sample_path=[]
result=[]
capacity1=[]
cost1=[]
x=[]
def nearest_neighbor(adj_matrix):
    n = len(adj_matrix)
    visited = [i for i in range(n)]
      
    visited.remove(0)
    print(visited)
    capacity=total_capacity
    while(True):
        path = []
        sample_path=[]
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
                    x.append(list(sample_path))
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
    x.append(sample_path)
    capacity1.append(load)
    return x,result,cost1,capacity

adj_matrix = np.array(adj_matrix)
x,final,cost1,capacity = nearest_neighbor(adj_matrix)
print(final,cost1,capacity1)

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
print("xxxxxxxxxx",x)
"""main=[]
c=[]
for i in x:
    def calculate_tour_cost(tour, adj_matrix):
        n = len(tour)
        total_cost = 0

        for i in range(n):
            total_cost += adj_matrix[tour[i - 1]][tour[i]]

        return total_cost+adj_matrix[tour[-1]][0]

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
        print("tourrrrrrr",tour)
        return tour, final_cost
    print(i)
    optimized_tour, final_cost = two_opt_swap(i[:-1], adj_matrix)
    main.append(optimized_tour)
    c.append(final_cost)
print(main,sum(c))
def change(l):
    res=[]
    res.append('r0')
    for i in l[1:]:
        res.append('n'+str(i-1))
    res.append('r0')
    print(len(res))
    return res
print("Result Routes:")
p=1
d={}
result={}
print(main)
for i in main:
    print(len(i))
    print(i)
    d['path'+str(p)]=change(i)
    p+=1
result[vehicles[0]]=d
print(result)"""

with open("Mock-Hackathon/level1b_output.json", "w") as outfile:
    json.dump(result, outfile)
"""out = open("Mock-Hackathon/Student Handout/Sampleoutput/level1b_output.json")

sample_output = json.load(out)
print(sample_output)
out.close()"""