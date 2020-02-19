def earliest_ancestor(ancestors, starting_node):
    oldest_ancestor = 0
    ancestor_graph = {}
    for parent, child in ancestors:
        if ancestor_graph.get(child):
            ancestor_graph[child] += [parent]
        else:
            ancestor_graph[child] = [parent]
    
    s = []

    s.append([starting_node])

    paths = []

    print(ancestor_graph)

    while len(s) > 0:
        line = s.pop()
        child = line[-1]
        parents = ancestor_graph.get(child)
        for parent in parents if parents else []:
            path = line + [parent]
            print(path)
            if ancestor_graph.get(parent):
                s.append(path)
            else:
                paths.append(path)

    print(paths)
    if len(paths) == 0:
        return -1


    elif len(paths) == 1:
        oldest = paths[0][-1]
        return oldest

    elif len(paths) >= 2:
        depth = 0
        oldest = None
        for path in paths:
            if len(path) > depth:
                depth = len(path)
                oldest = path[-1]
            elif len(path) == depth:
                if oldest > path[-1]:
                    oldest = path[-1]
        
        return oldest
        

