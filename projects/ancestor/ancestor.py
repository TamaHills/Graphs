def earliest_ancestor(ancestors, starting_node):
    oldest_ancestor = 0
    ancestor_graph = {}
    # create a relationship graph
    for parent, child in ancestors:
        # if child in graph
        if not ancestor_graph.get(child):
            ancestor_graph[child] = []

        ancestor_graph[child].append(parent)
    
    # create a stack for traversing
    s = []
    # append path to starting node
    s.append([starting_node])
    # create an array to store paths
    paths = []

    # while stack not empty
    while len(s) > 0:
        line = s.pop()
        child = line[-1]
        parents = ancestor_graph.get(child)
        # if node has parents loop through
        for parent in parents if parents else []:
            # create new path
            path = line + [parent]
            # if current has parents
            if ancestor_graph.get(parent):
                # append to stack
                s.append(path)
            else:
                # add path to possible paths
                paths.append(path)
    
    gens = 0
    oldest = -1
    # loop through all possible paths
    for path in paths:
        path_gens = len(path)
        path_oldest = path[-1]
        # if path is longer than deepest path
        if path_gens > gens:
            # update deepest path
            gens = path_gens
            # set oldest to the oldest of the path
            oldest = path_oldest
        # if the path is as deep as the deepest and the paths oldest node has lower id
        elif path_gens == gens and oldest > path_oldest:
            # set oldest to the oldest of the path
            oldest = path_oldest
        
    return oldest
        