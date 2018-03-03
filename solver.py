'''
MIT License

Copyright (c) 2018 Ben Brown

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

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

    while len(parents) > 0:
        item = parents.pop()

        for i in range(0, len(alpha)):
            # Ensure we do not exceed the depth for a single node.
            if tree.depth(item) == k:
                break

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

    # Will leave only valid solutions.
    return solutions



