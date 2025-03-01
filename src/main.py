# function สำหรับการเช็ค vertices ใน graph ว่าถ้ามีจะ return True ไม่มีจะ return False  
def has_vertices(graph, start, end):
    # เก็บเป็น set เพื่อให้ไม่มี vertices มีค่าซ้ำกัน
    all_vertices = set()

    # วนลูปรอบแรกของ graph ให้ดึง key และ value ใน dict ออกมา
    for key, values in graph.items():
        # เพิ่มค่า key ลงใน all_vertices
        all_vertices.add(key)
        # วนลูปรอบที่สองของ values เพราะ value ที่ได้มาตอนแรกใน dict เป็น list 
        # ต้องวน loop อีกรอบเพื่อได้ค่า element
        for value in values:
            # เพิ่มค่า value
            all_vertices.add(value)
        
    # เขียน condition return ออกมาว่าถ้า start และ end อยู่ใน all_vertices 
    # ให้ return True ไม่อยู่ให้ return False
    return start in all_vertices and end in all_vertices
    
# Algorithm: Deep-Firth-Search    
def dfs(graph, start, end, path=None):
    # เช็ค condition นี้ว่าถ้า vertices ที่รับค่ามาจาก paramters ไม่มีอยู่ใน graph ที่ส่งมาให้ return None
    if not has_vertices(graph, start, end):
        print("ไม่มี vertices ที่ระบุใน graph!")
        return None
        
    # เช็คว่าถ้าค่า path เป็น None ให้กำหนดค่าเป็น list (สำหรับรัน algorithm นี้ในครั้งแรก)
    if path is None:
        path = []

    # เพิ่มค่า start ลงใน path
    path.append(start)

    # ถ้าพบเส้นทางเป้าหมายแล้วให้ return ค่า path ออกมา
    if start == end:
        return path

    # วน loop หาเส้นทางของ end เมื่อวน loop ค่าของตัวแปร neighbor จะเป็นค่า value ของ dict 
    for neighbor in graph[start]:
        # ถ้าค่า neighbor ไม่อยู่ใน path ให้เรียกใช้ dfs ตัวมันเองอีกครั้ง(recursive)
        # และ หลีกเลี่ยงปัญหาเกิดการเก็บค่าเดิมของ path ที่เราเคยเดินมาแล้ว
        if neighbor not in path:
            # ส่ง arguments ไปใหม่เปลี่ยนจาก start -> neightbor ที่เหลือเหมือนเดิม
            result = dfs(graph, neighbor, end, path.copy()) 
            # เช็คถ้ามีผลลัพธ์(มี elemnet ใน list) ให้ return ผลลัพธ์นั้นออกมา 
            if result:
                return result  # Return the first found path
            
# เส้นทางของ graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

# กำหนดค่า start และ end
# start คือจุดเริ่มต้นใน graph
start = 'A'
# end คือจุดสิ้นสุดใน graph
end = 'C'

# เรียกใช้ algorithm: dfs จะได้ค่าออกมา 2 แบบคือ 
# 1. list ที่เก็บเส้นทางของแต่ละ vertice ที่มันเดินทางไป 
# 2. None ไม่มีเส้นทาง
path = dfs(graph, start, end)

# เช็คถ้าค่า path เป็น None ให้แสดงข้อความว่า "ไม่พบเส้นทาง"
if path is None:
    print("ไม่พบเส้นทาง")
else:
    print(f"เส้นทางจาก {start} ไปยัง {end} คือ")
    print( " -> ".join(path))