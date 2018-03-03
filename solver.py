from treelib import Tree, Node

def is_valid(a, b):
    if a.startswith(b) or b.startswith(a): 
        return True
    return False

def is_solution(a, b):
    return a == b

def solve(alpha, beta, k):
    # Maain initializers
    solutions = []
    tree = Tree()
    
    # Parents starts with root value aka empty string. 
    # We need to ensure the depth does not exceed k due to complexity issues.
    parents = ['']
    tree.create_node(tag='', identifier='')

    depth = 1
    while len(parents) > 0 and depth <= k:
        item = parents.pop()

        for i in range(0, len(alpha)):
            split = item.split()
            newAlpha = ""
            newBeta = ""

            # Try to retrieve the parent node string and append. 
            # Otherwise node is root.
            if len(split) > 1:
                newAlpha =  split[0] + alpha[i] 
                newBeta = split[1] + beta[i]
            else:
                newAlpha = alpha[i] 
                newBeta = beta[i]

            # Check to see if the node is valid. 
            # The node will be valid if there is a prefix. 
            if is_valid(newAlpha, newBeta):
                node = newAlpha + ' ' + newBeta

                # Check to see if node is a solution.
                if is_solution(newAlpha, newBeta):
                    solutions.append(node)

                # Create tree node since it is valid.
                tree.create_node(tag=node, identifier=node, parent=item)
                parents.append(node)
        
        depth += 1

    # Will leave only valid solutions.
    tree.show()
    return solutions

alpha = 'a', 'ab', 'bba'
beta = 'baa', 'aa', 'bb'
k = 6

solutions = solve(alpha, beta, k)
print("Solution(s):")
for solution in solutions:
    print(solution)