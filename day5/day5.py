def parse_line(line):
    
    point1, point2 = line.split('->')
    x1, y1 = point1.split(',')
    x2, y2 = point2.split(',')
    
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    
    return x1, y1, x2, y2

def calc_danger_sum(xy_dict):
    
    danger_sum = 0
    
    for i in xy_dict:
        if xy_dict[i] > 1:
            danger_sum += 1
            
    return danger_sum
    

if __name__ == '__main__':
    
    with open('day5.txt') as f:
        lines = f.read().splitlines()

    xy_dict_part1 = {}
    xy_dict_part2 = {}
    
    for line in lines:
        
        x1, y1, x2, y2 = parse_line(line)
        
        # if non-diagonal line, record each point in both dictionaries
        if x1 == x2 or y1 == y2:
            
            x_low = min(x1,x2)
            x_high = max(x1,x2)
            y_low = min(y1,y2)
            y_high = max(y1,y2)
            
            for xs in range(x_low,x_high+1):
                for ys in range(y_low,y_high+1):
                    
                    if (xs,ys) in xy_dict_part1:
                        xy_dict_part1[(xs,ys)] += 1
                    else:
                        xy_dict_part1[(xs,ys)] = 1
                    
                    if (xs,ys) in xy_dict_part2:
                        xy_dict_part2[(xs,ys)] += 1
                    else:
                        xy_dict_part2[(xs,ys)] = 1
        
        # if line is diagonal, record each point in part 2 dictionary
        else:
            
            x_iter = x1
            y_iter = y1
            x_end = x2
            y_end = y2
            
            while x_iter != x_end:
                
                if (x_iter,y_iter) in xy_dict_part2:
                    xy_dict_part2[(x_iter,y_iter)] += 1
                else:
                    xy_dict_part2[(x_iter,y_iter)] = 1
                
                if x_iter < x_end:
                    x_iter += 1
                else:
                    x_iter -= 1
                    
                if y_iter < y_end:
                    y_iter += 1
                else:
                    y_iter -= 1
            
            # get final point at end of while loop
            if (x_iter,y_iter) in xy_dict_part2:
                xy_dict_part2[(x_iter,y_iter)] += 1
            else:
                xy_dict_part2[(x_iter,y_iter)] = 1
            
    print(calc_danger_sum(xy_dict_part1))
    print(calc_danger_sum(xy_dict_part2))
    