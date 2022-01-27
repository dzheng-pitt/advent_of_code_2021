import numpy as np

if __name__ == '__main__':
    
    with open('day10.txt') as f:
        lines = f.read().splitlines()
    
    dict_paren = {'(':')','[':']','{':'}','<':'>'}
    bad_chars = []
    bad_chars_dict = {')':3,']':57,'}':1197,'>':25137}
    bad_chars_count = 0
    
    for line in lines:
        
        queue = []
        
        for i in line:
            
            if i in dict_paren:
                queue.append(dict_paren[i])
                
            else:
                if i != queue[-1]:
                    bad_chars.append(i)
                    bad_chars_count += bad_chars_dict[i]
                    break
                
                else:
                    queue.pop(len(queue)-1)
                    
    print(bad_chars_count)
        
    scores = []
    missing_score = {')':1,']':2,'}':3,'>':4}
    
    for line in lines:
        
        queue = []
        line_score = 0
        
        for i in line:
            
            if i in dict_paren:
                queue.append(dict_paren[i])
                
            else:
                if i != queue[-1]:
                    break
                
                else:
                    queue.pop(-1)
                    
        else:
            for qi in range(len(queue),0,-1):
                line_score = line_score*5 + missing_score[queue[qi-1]]
                
            scores.append(line_score)
    
    print(np.median(scores))