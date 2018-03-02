from treelib import Tree, Node

def is_valid(a, b):
    if a.startswith(b) or b.startswith(a): 
        return True
    return False

def is_solution(a, b):
    return a == b

def solve(alpha, beta, k):
    solutions = []
    tree = Tree()
    
    tree.create_node('root', None)
    for i in range(0, k):
        parent = None
        # Assumes alpha and beta are of equal size.
        for j in range(0, len(alpha)):
            node = alpha[j], beta[j]
            if is_valid(alpha[j], beta[j]):
                if is_solution(alpha[j], beta[j]):
                    solutions.insert(node)
                tree.create_node(data=node, parent=parent)
            # Update parent node.
            parent = node
            print(parent)
    # Will leave only valid solutions.
    return solutions

alpha = 'a', 'ab', 'bba'
beta = 'baa', 'aa', 'bb'
k = 4

solutions = solve(alpha, beta, k)
for solution in solutions:
    print("Solutions:")
    print(solution)