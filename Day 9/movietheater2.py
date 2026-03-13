points = []
filename = "movietheater.txt"

with open(filename, 'r', encoding="utf-8") as file:
    linije = file.readlines()
    for linija in linije:
        parts = linija.split(",")
        points.append((int(parts[0]), int(parts[1])))

edges = []
n = len(points)
for k in range(n):
    p1 = points[k]
    p2 = points[(k + 1) % n]
    edges.append((p1, p2))

max_area = 0

for i in range(n):
    for j in range(i + 1, n):
        p1 = points[i]
        p2 = points[j]
        
        min_x = min(p1[0], p2[0])
        max_x = max(p1[0], p2[0])
        min_y = min(p1[1], p2[1])
        max_y = max(p1[1], p2[1])
        
        width = (max_x - min_x) + 1
        height = (max_y - min_y) + 1
        area = width * height
        
        if area <= max_area:
            continue
            
        is_valid_rect = True
        
        for (v1, v2) in edges:
            if v1[0] == v2[0]: 
                edge_x = v1[0]
                edge_y_min, edge_y_max = min(v1[1], v2[1]), max(v1[1], v2[1])
                
                if min_x < edge_x < max_x:
                    overlap_y1 = max(min_y, edge_y_min)
                    overlap_y2 = min(max_y, edge_y_max)
                    if overlap_y1 < overlap_y2:
                        is_valid_rect = False
                        break
            
            else: 
                edge_y = v1[1]
                edge_x_min, edge_x_max = min(v1[0], v2[0]), max(v1[0], v2[0])
                if min_y < edge_y < max_y:
                    overlap_x1 = max(min_x, edge_x_min)
                    overlap_x2 = min(max_x, edge_x_max)
                    if overlap_x1 < overlap_x2:
                        is_valid_rect = False
                        break
        if not is_valid_rect:
            continue

        mid_x = (min_x + max_x) / 2
        mid_y = (min_y + max_y) / 2
        intersections = 0
        for (v1, v2) in edges:
            if v1[0] == v2[0]:
                edge_x = v1[0]
                edge_y_min, edge_y_max = min(v1[1], v2[1]), max(v1[1], v2[1])
                
                if edge_x > mid_x:
                    if edge_y_min < mid_y < edge_y_max:
                        intersections += 1
        if intersections % 2 == 1:
            max_area = area

print(f"Largest Valid Area: {max_area}")