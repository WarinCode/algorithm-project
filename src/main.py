import heapq

def dijkstra(graph, start, end):
    # กำหนดระยะทางเริ่มต้น
    distances = {start: 0}
    previous_nodes = {start: None}
    priority_queue = [(0, start)]
    
    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node == end:
            break
        
        for neighbor, weight in graph.get(current_node, {}).items():
            distance = current_distance + weight
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    
    # สร้างเส้นทางจาก start ไปยัง end
    path = []
    current_node = end
    while current_node:
        path.append(current_node)
        current_node = previous_nodes.get(current_node)
    path.reverse()
    
    return distances.get(end, float('inf')), path

# กราฟตัวอย่าง
graph = {
    'A': {'B': 10, 'C': 15},
    'B': {'A': 10, 'D': 20},
    'C': {'A': 15, 'D': 30},
    'D': {'B': 20, 'C': 30, 'E': 5},
    'E': {'D': 5}
}

# เรียกใช้ฟังก์ชัน Dijkstra
start_node = 'A'
end_node = 'E'
distance, path = dijkstra(graph, start_node, end_node)

# แสดงผลลัพธ์
print(f"The shortest distance from {start_node} to {end_node} is {distance} units.")
print(f"The path taken: {' -> '.join(path)}")