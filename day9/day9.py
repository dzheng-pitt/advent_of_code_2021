import numpy as np

def get_neighbors(data,i,j):
    
    n = []
    
    if i != 0:
        n.append((i-1,j))
           
    if i != rows-1:
        n.append((i+1,j))
           
    if j != 0:
        n.append((i,j-1))
       
    if j != cols-1:
        n.append((i,j+1))
           
    return n
   
def find_basin_size(data,i,j,basin_collection):
   
    basin_collection.add((i,j))
    n = get_neighbors(data,i,j)
    n = set(n) - basin_collection
   
    for p in n:
        adj_points = get_neighbors(data,p[0],p[1])
   
        adj_points = set(adj_points) - basin_collection
           
        not_smallest = 0
        for adj in adj_points:
            if data[p[0],p[1]] > data[adj[0],adj[1]]:
                not_smallest = 1
        if data[p[0],p[1]] == 9:
            not_smallest = 1
           
        if not_smallest == 0:
            find_basin_size(data,p[0],p[1],basin_collection)
   
    return basin_collection
   
if __name__ == '__main__':
    
    # put data into numpy array
    with open('day9.txt') as f:
        lines = f.read().splitlines()
    
    cols = len(lines[0])
    rows = len(lines)    
        
    data = np.ndarray((rows,cols))
    
    iters = 0
    for i in lines:
        data[iters,:] = np.array(list(i)).astype(int)
        iters +=1 
    
    # find low points and basin sizes recursively
    count = 0
    big_basin_collect = {}
    basin_size = {}
    for i in range(rows):
        for j in range(cols):
            
            n = get_neighbors(data,i,j)
            not_smallest = 0
            item = data[i,j]
            
            for k in n:
                if item >= data[k[0],k[1]]:
                    not_smallest = 1
                    
            if not_smallest == 0:
                count += 1 + data[i,j]
                big_basin_collect[(i,j)] = find_basin_size(data,i,j,{(i,j)})
                basin_size[(i,j)] = len(big_basin_collect[(i,j)])
                
    print(count)
    
    sizes = []
    for i in basin_size:
        sizes.append(basin_size[i])
    sizes.sort()
    
    print(sizes[-3:], np.prod(sizes[-3:]))
