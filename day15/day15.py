import numpy as np

def set_up_graph(lines, part):
      
    # set up data in numpy
    iters = 0
    rows = len(lines)
    cols = len(lines[0])
    template = np.zeros((rows, cols))
    
    for line in lines:
        
        template[iters] = np.array(list(line)).astype(int)
        iters += 1
    
    if part == 'part1':
        mult = 1
        
    elif part == 'part2':
        mult = 5
        
    rows = len(lines)*mult
    cols = len(lines[0])*mult
    data = np.zeros((rows, cols))
        
    for i in range(mult):
        
        for j in range(mult):
            
            data_insert = template + i + j 
            data_insert = np.where(data_insert > 9, data_insert - 9, data_insert)
            data[i*int(rows/mult):(i+1)*int(rows/mult),j*int(cols/mult):(j+1)*int(cols/mult)] = data_insert
    
    # make nodes
    nodes = {}
    edges = []
    node_idx = 0
    
    for i in range(data.shape[0]):
        
        for j in range(data.shape[0]):
    
            nodes[(i, j)] = node_idx
            edges.append([])
            
            node_idx += 1
    
    # make edges and weights
    for i in range(data.shape[0]):
        
        for j in range(data.shape[1]):
            
            node_idx = nodes[(i,j)]
            
            if i > 0:
                edges[node_idx].append((i-1,j,data[i-1,j]))
                
            if j > 0:
                edges[node_idx].append((i,j-1,data[i,j-1]))
                
            if i < rows-1:
                edges[node_idx].append((i+1,j,data[i+1,j]))
                
            if j < cols-1:
                edges[node_idx].append((i,j+1,data[i,j+1]))
                
    return nodes, edges

def calc_shortest_path(nodes, edges, final_key):
    
    # find shortest distance with Dijkstra
    shortest_dist = {(0,0):0}
    dist_queue = {0:{(0,0)}}
    
    while True:
        
        min_value = min(dist_queue.keys())
        node = dist_queue.pop(min_value)
        
        if len(node) > 1:
            do_node = node.pop()
            dist_queue[min_value] = node
            node = do_node
            
        else:
            node = node.pop()
            
        for adj_node in edges[nodes[node]]:
            
            if adj_node[0:2] not in shortest_dist or \
                shortest_dist[adj_node[0:2]] > shortest_dist[node] + adj_node[2]:
                    
                shortest_dist[adj_node[0:2]] = shortest_dist[node] + adj_node[2]
            
                if shortest_dist[adj_node[0:2]] in dist_queue:
                    dist_queue[shortest_dist[adj_node[0:2]]].add(adj_node[0:2])
                    
                else:
                    dist_queue[shortest_dist[adj_node[0:2]]] = {adj_node[0:2]}
        
        if len(dist_queue) == 0:
            break
    
    print(shortest_dist[final_key])
    
if __name__ == '__main__':
    
    with open('day15.txt') as f:
        lines = f.read().splitlines()
    
    nodes, edges = set_up_graph(lines, 'part1')
    calc_shortest_path(nodes, edges, (99,99))

    nodes, edges = set_up_graph(lines, 'part2')
    calc_shortest_path(nodes, edges, (499,499))

  