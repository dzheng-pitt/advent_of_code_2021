import numpy as np

if __name__ == '__main__':

    with open('day6.txt') as f:
        lines = f.read().splitlines()
    
    # make a list of fish ages and counts
    fish = np.array(lines[0].split(','))
    distinct_fish, count_fish = np.unique(fish,return_counts=True)
    distinct_fish = distinct_fish.astype(int)
    
    distinct_fish = np.append(np.append([0],distinct_fish), [6,7,8])
    count_fish = np.append(np.append([0],count_fish),[0,0,0])
    
    # simulate fish growth
    for day in range(256):
        
        distinct_fish = distinct_fish - 1
        new_fish = count_fish[np.where(distinct_fish < 0)]
        
        count_fish[np.where(distinct_fish < 0)] = new_fish
        distinct_fish[np.where(distinct_fish < 0)] = 8
        
        count_fish[np.where(distinct_fish == 6)] += new_fish
        
        if day == 79:
            
            print(np.sum(count_fish))
            
        elif day == 255:
            
            print(np.sum(count_fish))
