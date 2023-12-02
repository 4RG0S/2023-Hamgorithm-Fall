def count_intersecting_circles():
    num_testcases = int(input())

    for _ in range(num_testcases):
        circle_count = 0
        x1, y1, x2, y2 = map(int, input().split())
        num_circles = int(input())

        for i in range(num_circles):
            cx, cy, cr = map(int, input().split())
            dist1 = (x1 - cx) ** 2 + (y1 - cy) ** 2
            dist2 = (x2 - cx) ** 2 + (y2 - cy) ** 2
            if (dist1 < cr ** 2 and dist2 > cr ** 2) or (dist1 > cr ** 2 and dist2 < cr ** 2):
                circle_count += 1

        print(circle_count)

count_intersecting_circles()
