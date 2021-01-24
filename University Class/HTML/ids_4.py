A -> [1: B, 1: C, 1: E]
B -> [1: A, 1: D, 1: F]
C -> [1: G, 1: A]
D -> [1: B]
E -> [1: F, 1: A]
F -> [1: E, 1: B]
G -> [1: C]


Node = {
    'A' : ['B', 'C', 'E']
    'B' : ['A', 'D', 'F']
    'C' : ['G', 'A']
    'D' : ['B']
    'E' : ['F', 'A']
    'F' : ['E', 'B']
    'G' : ['C']
        }

def iddfs(root: Node, goal: str, maximum_depth: int=10):
    """
    Return the IDDFS path from the root node to the node with the goal label.
    
    Args:
        root: the node to start at
        goal: the label of the goal node
        maximum_depth: the maximum depth to search
        
    Returns: a list with the nodes from root to goal
    
    Raises: value error if the goal isn't in the graph
    """
    for depth in range(0, maximum_depth):
        result = _dls([root], goal, depth)
        if result is None:
            continue
        return result
    
    raise ValueError('goal not in graph with depth {}'.format(maximum_depth))

def _dls(path: list, goal: str, depth: int):
    """
    Return the depth limited search path from a subpath to the goal.
    
    Args:
        path: the current path of Nodes being taken
        goal: the label of the goal node
        depth: the depth in the graph to search
        
    Returns: the path if it exists, none otherwise
    """
    current = path[-1]
    if current.label == goal:
        return path
    if depth <= 0:
        return None
    for edge in current.children:
        new_path = list(path)
        new_path.append(edge.destination)
        result = _dls(new_path, goal, depth - 1)
        if result is not None:
            return result
			

			
iddfs(D, 'G')
Out[6]:
[D -> [1: B],
 B -> [1: A, 1: D, 1: F],
 A -> [1: B, 1: C, 1: E],
 C -> [1: G, 1: A],
 G -> [1: C]]
 
 
 
 
 