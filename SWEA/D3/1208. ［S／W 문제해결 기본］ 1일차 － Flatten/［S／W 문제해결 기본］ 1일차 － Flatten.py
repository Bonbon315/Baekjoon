for test_case in range(1, 11):
    dumpnum = int(input())
    boxes = list(map(int, input().split()))
    
    while dumpnum:
        max_box = max(boxes)
        max_idx = boxes.index(max_box)
        min_box = min(boxes)
        min_idx = boxes.index(min_box)

        boxes[max_idx] -= 1
        boxes[min_idx] += 1
        dumpnum -= 1

    dif = max(boxes) - min(boxes)
    print(f'#{test_case} {dif}')