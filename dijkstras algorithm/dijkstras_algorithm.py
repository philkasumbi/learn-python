import heapq



graph = {
    'A': [('B', 2), ('C', 1)],
    'B': [('A', 2), ('D', 3)],
    'C': [('A', 1), ('D', 4)],
    'D': [('B', 3), ('C', 4)]
}

distance = {node: float('inf') for node in graph}
distance['A'] = 0

pq = [(0,"A")]

visited = set()


while pq:
    current_dist, current_node = heapq.heappop(pq)

    if current_node in visited:
        continue

    visited.add(current_node)

    # Step 4: Check all neighbors of current_node
    for neighbor, weight in graph[current_node]:
        if neighbor in visited:
            continue

        new_distance = current_dist + weight

        # If new path is shorter, update it
        if new_distance < distance[neighbor]:
            distance[neighbor] = new_distance
            heapq.heappush(pq, (new_distance, neighbor))
    
# Print current status after visiting a node
print(f"Visited: {current_node}")
print(f"Distances: {distance}")
print(f"Queue: {pq}")
print("-" * 30)