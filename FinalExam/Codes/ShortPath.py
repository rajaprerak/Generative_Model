def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):
      
    # a few sanity checks
    if src not in graph:
        raise TypeError('Error')
    if dest not in graph:
        raise TypeError('Error')    
    # ending condition
    if src == dest:
        # We build the shortest path and display it
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        #print('shortest path: '+str(path)+" cost="+str(distances[dest]))
        print("Suggested Career Path")
        print("---------------------")
        print((path[0]))
        print("        ","|")
        print((path[1]))
        print("        ","|")
        print("       ",(path[2]))
        print("        ","|")
        print("       ",(path[3]))

              
    else :     
        # if it is the initial  run, initializes the cost
        if not visited: 
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        visited.append(src)
        # now that all neighbors have been visited: recurse                         
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))        
        x=min(unvisited, key=unvisited.get)
        dijkstra(graph,x,dest,visited,distances,predecessors)
        


if __name__ == "__main__":
    graph = {'CEO': {'a': 2, 'CTO': 1},
            'a': {'CEO': 3, 'CTO': 4, 'c':8},
            'CTO': {'CEO': 4, 'a': 2, 'Sr. Software Developer': 2},
            'c': {'a': 2, 'Sr. Software Developer': 7, 'Software Developer': 4},
            'Sr. Software Developer': {'CTO': 1, 'c': 11, 'Software Developer': 5},
            'Software Developer': {'c': 3, 'Sr. Softwrae Developer': 5}}
    dijkstra(graph,'CEO','Software Developer')
