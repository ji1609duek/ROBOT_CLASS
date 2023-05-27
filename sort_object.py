obj_detected = {'bottle': [110, 30], 'glass': [60, 35], 'book': [310, 23], 'phone': [260, 33], 'dice': [155, 38], 'mouse': [200, 45], 'keyboard': [298, 65], 'fan': [250, 36]}

sorted_objects = sorted(obj_detected.items(), key=lambda x: x[1][0], reverse=True)

for obj, pos in sorted_objects:
    print(obj, pos)
