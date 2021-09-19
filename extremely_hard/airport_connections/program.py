# time = O(a+r + a*(a+r) + aloga) and space = O(a+r)
def airportConnections(airports, routes, init):
    graph = makeGraph(airports, routes)
    unreachable_airport_nodes = getUnreachableAirports(airports, graph, init)
    markUnreachableAirports(graph, unreachable_airport_nodes)
    return getMinConnections(graph, unreachable_airport_nodes)

class Airport:
    def __init__(self, name):
        self.name = name
        self.destinations = []
        self.reachable = False
        self.unreachable_destinations = []

# time = O(a+r) and space = O(a+r)
def makeGraph(airports, routes):
    graph = {}
    for airport in airports:
        graph[airport] = Airport(airport)

    for route in routes:
        source, destination = route
        graph[source].destinations.append(destination)
    
    return graph

# time = O(a+r) and space = O(a)
def getUnreachableAirports(airports, graph, init):
    visted_airports = dfs(graph, init)

    unreachable_airport_nodes = []
    for airport in airports:
        if airport in visted_airports: continue
        unreachable_airport_nodes.append(graph[airport])
    
    return unreachable_airport_nodes

def dfs(graph, init):
    visted_airports = {}
    stack = [init]
    while len(stack):
        curr = stack.pop()
        if curr in visted_airports: continue
        curr_node = graph[curr]
        visted_airports[curr] = True
        curr_node.reachable = True
        stack.extend(curr_node.destinations)
    
    return visted_airports

# time = O(a*(a+r)) and space = O(a)
def markUnreachableAirports(graph, unreachable_airport_nodes):
    for airport_node in unreachable_airport_nodes:
        unreachable_airports = dfAddUnreachableAirports(graph, airport_node.name)
        airport_node.unreachable_destinations = unreachable_airports

def dfAddUnreachableAirports(graph, init):
    visted_airports = {}
    unreachable_airports = []
    stack = [init]
    while len(stack):
        airport = stack.pop()
        airport_node = graph[airport]
        if airport_node.reachable: continue
        if airport in visted_airports: continue

        visted_airports[airport] = True
        unreachable_airports.append(airport)
        stack.extend(airport_node.destinations)
    
    return unreachable_airports

# time = O(aloga + a+r) and space = O(1)
def getMinConnections(graph, unreachable_airport_nodes):
    unreachable_airport_nodes.sort(
        key=lambda airport_node: len(airport_node.unreachable_destinations), reverse=True
    )

    connections = 0
    for airport_node in unreachable_airport_nodes:
        if airport_node.reachable: continue
        connections += 1
        
        for airport in airport_node.unreachable_destinations:
            graph[airport].reachable = True

    return connections       