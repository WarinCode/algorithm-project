import graphs as all_graphs


# function สำหรับการเช็ค vertices ใน graph ว่าถ้ามีจะ return True ไม่มีจะ return False
def has_vertices(graph, start, goal):
    # เก็บเป็น set เพื่อให้ไม่มี vertices ที่มีค่าซ้ำกัน
    vertices = set()

    # วนลูปรอบแรกของ graph ให้ดึง key และ value ใน dict ออกมา
    for key, values in graph.items():
        # เพิ่มค่า key ลงใน vertices
        vertices.add(key)
        # วนลูปรอบที่สองของ values เพราะ value ที่ได้มาตอนแรกใน dict เป็น list
        # ต้องวน loop อีกรอบเพื่อได้ค่า element
        for value in values:
            # เพิ่มค่า value
            vertices.add(value)

    # เขียน condition return ออกมาว่าถ้า start และ goal อยู่ใน vertices
    # ให้ return True ไม่อยู่ให้ return False
    return start in vertices and goal in vertices


# Algorithm: Depth-Firth-Search
def dfs(graph, start, goal, path=None):
    # เช็คว่าถ้าค่า path เป็น None ให้ทำเงื่อนไขต่อไปนี้ (สำหรับรัน algorithm นี้ในครั้งแรก)
    if path is None:
        # กำหนดค่า path ให้เป็น list
        path = []
        # เช็ค condition นี้ว่าถ้า vertices ที่รับค่ามาจาก paramters ไม่มีอยู่ใน graph ให้ throw exception นี้ออกไป
        if not has_vertices(graph, start, goal):
            raise Exception(f"ไม่มี vertices {start} หรือ {goal} ที่อยู่ใน graph!")
        
    # เพิ่มค่า start ลงใน path
    path.append(start)

    # ถ้าพบเส้นทางเป้าหมายแล้วให้ return ค่า path ออกมา
    if start == goal:
        return path

    # วน loop หาเส้นทางของ goal เมื่อวน loop ค่าของตัวแปร neighbor จะเป็นค่า value ของ dict
    for neighbor in graph[start]:
        # ถ้าค่า neighbor ไม่อยู่ใน path ให้เรียกใช้ dfs ตัวมันเองอีกครั้ง(recursive)
        # และ หลีกเลี่ยงปัญหาเกิดการเก็บค่าเดิมของ path ที่เราเคยเดินมาแล้ว
        if neighbor not in path:
            # ส่ง arguments ไปใหม่เปลี่ยนจาก start -> neightbor ที่เหลือเหมือนเดิม
            result = dfs(graph, neighbor, goal, path.copy())
            # เช็คถ้ามีผลลัพธ์(มี elemnet ใน list) ให้ return ผลลัพธ์นั้นออกมา
            if result:
                return result  # Return the first found path


# กำหนดค่า start และ goal
# start คือจุดเริ่มต้นใน graph
start = "A"
# goal คือจุดเป้าหมายที่ต้องไปให้ถึงใน graph
goal = "I"

# เขียน try catch เพื่อดักจับอาจจะมีการเกิด exception จาก dfs นี้ไว้
try:
    # เรียกใช้ algorithm: dfs เพื่อหาเส้นทาง
    path = dfs(all_graphs.graph3, start, goal)
    # แสดงผลลัพธ์
    print(f"เส้นทางจาก {start} ไปยัง {goal} คือ")
    print(" -> ".join(path))
except Exception as e:
    # แสดงข้อความของ exception
    print(e.__str__())
