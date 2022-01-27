import numpy as np

class node_class:
    
    def __init__(self, parent = None, value = None):
        self.parent = parent
        self.value = value
        self.left_node = None
        self.right_node = None

class tree_class:
    
    def __init__(self):
        self.root = node_class()
        self.current_node = self.root
    
    def create_node(self, parent = None, value = None, 
                    left_node = False, right_node = False):
        node = node_class(parent, value)

        if left_node == True:
            node.parent.left_node = node
        elif right_node == True:
            node.parent.right_node = node
        self.current_node = node
    
    def build_tree(self, line):
        
        for i in line:
            if i == '[':
                self.create_node(parent = self.current_node, 
                                 left_node = True)
            if i.isdigit():
                self.current_node.value = int(i)
            if i == ',':
                self.create_node(parent = self.current_node.parent, 
                                 right_node = True)
            if i == ']':
                self.current_node = self.current_node.parent
    
    # for diagnostics...
    def traverse_postorder_print(self, node = None, depth = 0):
        
        if node == None:
            node = self.root
        print(node)
        if node.left_node != None:
            depth += 1
            depth = self.traverse_inorder_print(node.left_node, depth)
        if node.right_node != None:
            depth += 1
            depth = self.traverse_inorder_print(node.right_node, depth)
        print(node.value, depth)
        depth -= 1

        return depth   

    # perhaps can use a double linked list here instead
    def find_nearest_left_node(self, node):
        val_to_move = node.value
        old_node = node
        node = node.parent
        
        node.value = 0
        node.left_node = None
        del old_node
        
        while node != self.root:
            old_node = node
            node = node.parent
            if old_node != node.left_node:
                node = node.left_node
                while node.right_node != None:
                    node = node.right_node
                break
        else:
            return 
        
        node.value += val_to_move

    def find_nearest_right_node(self, node):
        val_to_move = node.value
        old_node = node
        node = node.parent
        
        node.value = 0
        
        node.right_node = None
        del old_node
        
        while node != self.root:
            old_node = node
            node = node.parent
            if old_node != node.right_node:
                node = node.right_node
                while node.left_node != None:
                    node = node.left_node
                break

        else:
            return
        
        node.value += val_to_move
    
    # our two main functions
    def find_and_explode(self, node = None, depth = 0, 
                         left_exploded = 0, right_exploded = 0):
        
        if node == None:
            node = self.root
     
        if node.left_node != None and left_exploded == 0:
            depth += 1
            depth, left_exploded, right_exploded = \
                self.find_and_explode(node.left_node, depth, 
                                      left_exploded, right_exploded)
                
        if node.right_node != None and right_exploded == 0:
            depth += 1
            depth, left_exploded, right_exploded = \
                self.find_and_explode(node.right_node, depth, 
                                      left_exploded, right_exploded)
        
        if depth > 4:
            if node == node.parent.left_node:
                self.find_nearest_left_node(node)
                left_exploded = 1
            elif node == node.parent.right_node:
                self.find_nearest_right_node(node)
                right_exploded = 1
            
        depth -= 1
        
        return depth, left_exploded, right_exploded
    
    def find_and_split(self, node = None, depth = 0, split = 0, exploded = 0):
                    
        if node == None:
            node = self.root
     
        if node.left_node != None and exploded == 0:
            split, exploded = self.find_and_split(node.left_node, 
                                                  depth, split, exploded)
                
        if node.right_node != None and exploded == 0:
            split, exploded = self.find_and_split(node.right_node, 
                                                  depth, split, exploded)

        if node.value != None and node.value > 9:
            self.create_node(parent = node, value = \
                             int(np.floor(node.value/2)), left_node = True)
            self.create_node(parent = node, value = \
                             int(np.ceil(node.value/2)), right_node = True)
            node.value = None
            return 1, 1
        
        return split, exploded

    # for adding numbers
    def print_tree(self, node = None):
        
        string = ''
        if node == None:
            node = self.root
     
        if node.left_node != None:
            string += '['
            string += self.print_tree(node.left_node)
                
        if node.right_node != None:
            string += ','
            string += self.print_tree(node.right_node)
            string += ']'

        if node.value != None:
            return str(node.value)
        
        return string
        
    def final_sum(self, node = None):
        
        left_sum = 0
        right_sum = 0
        
        if node == None:
            node = self.root
            
        if node.left_node != None:
            left_sum += self.final_sum(node.left_node)
            
        if node.right_node != None:
            right_sum += self.final_sum(node.right_node)
        
        if node.value != None:
            return node.value

        final_sum = left_sum*3 + right_sum*2
        
        return final_sum

def calc_magnitude(lines):
       
    tree = tree_class()
    tree.build_tree(lines[0])

    for line in lines[1:]:
    
        current_line = tree.print_tree()
        add_line = '[' + current_line + ',' + line +']'
        
        tree = tree_class()
        tree.build_tree(add_line)
                
        left_exploded = 1
        split = 1
        while left_exploded == 1 or split == 1:
            while left_exploded == 1:
                _, left_exploded, right_exploded = tree.find_and_explode()
            split, left_exploded = tree.find_and_split()
    
    
    return tree.final_sum()

if __name__ == '__main__':
    
    with open('day18.txt') as f:
        lines = f.read().splitlines()
        
    print(calc_magnitude(lines))
    
    max_mag = 0
    for i in lines:
        for j in lines:
            mag = calc_magnitude([i]+[j])
            if mag > max_mag:
                max_mag = mag
    print(max_mag)