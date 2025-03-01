import heapq

# ฟังก์ชัน Dijkstra เพื่อหาทางที่สั้นที่สุด
def dijkstra(graph, start, end):
    # กำหนดระยะทางเริ่มต้นสำหรับแต่ละโหนด
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # ระยะทางจากจุดเริ่มต้นเป็น 0
    
    # ใช้ heapq เพื่อให้การเลือกโหนดที่ใกล้ที่สุดเร็วขึ้น
    priority_queue = [(0, start)]  # (ระยะทาง, โหนด)
    previous_nodes = {node: None for node in graph}  # เพื่อเก็บเส้นทางที่เดินผ่าน
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # ถ้าเราเจอระยะทางที่ใหญ่กว่าที่คำนวณได้แล้ว ไม่ต้องทำอะไร
        if current_distance > distances[current_node]:
            continue
        
        # ตรวจสอบเพื่อนบ้านของโหนดปัจจุบัน
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # อัพเดตระยะทางถ้าคำนวณได้ระยะทางที่สั้นกว่า
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # สร้างเส้นทางจาก start ไปยัง end โดยการย้อนกลับจาก end
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()
    
    return distances[end], path

# กราฟตัวอย่าง (Adjacency List) สำหรับการเดินทางในแผนที่
# โหนดคือเมืองต่างๆ และขอบคือถนนที่เชื่อมโยงกัน มีระยะทางที่แตกต่างกัน
graph = {
    'CityA': {'CityB': 10, 'CityC': 15},
    'CityB': {'CityA': 10, 'CityD': 20},
    'CityC': {'CityA': 15, 'CityD': 30},
    'CityD': {'CityB': 20, 'CityC': 30, 'CityE': 5},
    'CityE': {'CityD': 5}
}

# เรียกใช้ฟังก์ชัน Dijkstra เพื่อหาทางที่สั้นที่สุดจาก 'CityA' ไปยัง 'CityE'
start_node = 'CityA'
end_node = 'CityE'
distance, path = dijkstra(graph, start_node, end_node)

# แสดงผลลัพธ์
print(f"The shortest distance from {start_node} to {end_node} is {distance} units.")
print(f"The path taken: {' -> '.join(path)}")