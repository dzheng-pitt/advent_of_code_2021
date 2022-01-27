def calc_problem(pair_dict):
    
    char_counts = {}
    for i in pair_dict:
        
        x = i[0]
        
        if x not in char_counts:
            char_counts[x] = pair_dict[i]
            
        else:
            char_counts[x] += pair_dict[i]
        
    char_counts[char_list[-1]] += 1
    
    return max(char_counts.values()) - min(char_counts.values())

if __name__ == '__main__':

    with open('day14.txt') as f:
        lines = f.read().splitlines()
    
    # initialize the pairs dictionary with the current data
    char_list = list(lines[0])
    pair_dict = {}
    
    for i in range(len(char_list)-1):
        
        pair = char_list[i]+char_list[i+1]
        
        if pair not in pair_dict:
            pair_dict[pair] = 1
            
        else:
            pair_dict[pair] += 1
    
    # define how the system grows according to the rules
    poly_map = {}
    
    for i in lines:
        
        if '->'  in i:
            key, val = i.split('->')
            poly_map[key.strip()] = val.strip()
          
    # process according to question
    for i in range(40):
        
        # each iteration, make a new dictionary and grow the 
        # pairs according to poly_map
        new_dict = {}
        
        for pair in pair_dict:
            
            mid_char = poly_map[pair]
            pair1 = pair[0]+mid_char
            pair2 = mid_char+pair[1]
            
            if pair1 not in new_dict:
                new_dict[pair1] = pair_dict[pair]
                
            else:
                new_dict[pair1] += pair_dict[pair]
                
            if pair2 not in new_dict:
                new_dict[pair2] = pair_dict[pair]
                
            else:
                new_dict[pair2] += pair_dict[pair]
                
        pair_dict = new_dict
        
        if i == 9:
            part1_dict = new_dict
    
    print(calc_problem(part1_dict), calc_problem(pair_dict))
