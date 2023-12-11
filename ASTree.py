#find the function, pass to another handler that will deal with the Function, then find a way to continue on the tree without adding more values to the function vector that aren't in the function scope

from pathlib import Path
import ast, math
import pandas as pd

def process_file(file_path: Path):
    # Get the AST object for the module
    ast_module = ast.parse(file_path.read_text())

    # Create a custom Node Visitor to traverse the AST looking for Function definitions (FunctionDef)
    node_visitor = NodeVisitor(file_path)

    # Begin the traversal of the AST (which also builds the Node objects into a single list)
    # Return the returned list of nodes
    return node_visitor.visit(ast_module)

class Node:
    def __init__(self, key):
        self.key = key
        self.profile = [0,0,0,0,0,0,0]
        #[# of function calls, # of while loops, # of expressions, # of arguments]
    def __repr__(self):
        return f"Node(key={self.key}, profile={self.profile})"


class NodeVisitor(ast.NodeVisitor):
    def __init__(self, file_path: Path):
        self.file_path = file_path  # for Node print out later on
        self.file_graph_node_list = []  # the list to be returned to the caller process_file()

    # overridden: STARTING POINT (root node of AST)
    def visit_Module(self, ast_node):
        self.generic_visit(ast_node)  # continue visiting breadth first
        return self.file_graph_node_list  # Once visiting complete return running Node list to caller

    # overridden: the cursor is currently at a Function definition node within the AST
    def visit_FunctionDef(self, ast_node):
        # NOT CALLING generic visit, visits of children of this node to be handled by create
        # Custom function to create a Node object for this function definition
        self.create_node(ast_node)
        # Should return and continue the generic visiting on any remaining parts of the AST
        self.generic_visit(ast_node)


    def create_node(self, ast_node):
        # Node is some simple class for holding your "Profile" according to some defined scheme
        node = Node(key=(self.file_path, ast_node.name))

        # NODE PROFILE FORM
        # [criteria1, criteria2, criteria3, ..., criteriaN]

        # Number of calls example
        # NOTE: will not be efficient to walk the tree for each sought after
        # node type, but this is for the idea, your improved approach would be in here
        # Get all calls made via list comprehension
        for x in ast.walk(ast_node):
            if isinstance(x, ast.Call):
                node.profile[0]+=1
            elif isinstance(x, ast.While):
                node.profile[1]+=1
            elif isinstance(x, ast.Expr):
                node.profile[2]+=1
            elif isinstance(x, ast.arg):
                node.profile[3]+=1
            elif isinstance(x, ast.Return):
                node.profile[4]+=1
            elif isinstance(x, ast.If):
                node.profile[5]+=1
            elif isinstance(x, ast.For):
                node.profile[6]+=1


        # Add the Node object for this function to the running list of the source code file
        self.file_graph_node_list.append(node)
    
def euclidean(p1,p2):
    sum = 0
    for i in range(len(p1)-1):
        sum += (p1[i] - p2[i])**2
    return math.sqrt(sum)

def similarity_ranker(nf1, nf2):
    similarity_score = []
    for node1 in nf1:
        for node2 in nf2:
            similarity_score.append((euclidean(node1.profile, node2.profile), node1.key[1], node2.key[1]))
    similarity_score.sort(key=lambda i:i[0])
    return similarity_score

def sim_df(sim):
    df = pd.DataFrame(sim, columns=("Distance", "File1 Function", "File2 Function"))
    return df
def main():
    # create Paths for the two files to process
    file1 = Path('test_code/rockpapergpt.py')
    file2 = Path('test_code/DrewRPS.py')

    #process the files
    nodes_file1 = process_file(file1)
    nodes_file2 = process_file(file2)

    #calculate and output similarity
    sim = similarity_ranker(nodes_file1, nodes_file2)
    simdf = sim_df(sim)
    print(simdf)

    # for each node pair of Nodes between 'nodes_file1' and 'nodes_file2'
    # compute and output Euclidean distance values between their respective profile vectors

    # normalize the distance values by the largest seen to be [0, 1]

    # for each Node pair as before output the names of the two nodes and the computed "distance"
    # NOTE: can invert to be similarity if preferable


if __name__ == "__main__":
    main()