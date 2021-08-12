# time = O(j+d) and space = O(j+d) => j = len(jobs) or nodes | d = len(deps) or edges
def topologicalSort(jobs, deps):
    graph = {}
    for job in jobs:
        graph[job] = {
            "deps": [], # nodes that depend on this node
            "n_dep": 0, # number of nodes this node depends on
            "job": job,
        }
    
    for job, dep in deps: 
        graph[job]["deps"].append(dep)
        graph[dep]["n_dep"] += 1

    order = []
    zero_dep = []
    ptr = 0
    for node in graph.values():
        if node["n_dep"] == 0: zero_dep.append(node)
    
    while ptr != len(zero_dep):
        curr = zero_dep[ptr]
        for dep in curr["deps"]:
            graph[dep]["n_dep"] -= 1
            if graph[dep]["n_dep"] == 0: zero_dep.append(graph[dep])
        order.append(curr["job"])
        ptr += 1

    return [] if len(order) != len(jobs) else order
