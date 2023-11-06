while True:
    num = int(input())
    if num == 0:
        break
    else:
        max_height = 0.0
        max_names = []

        for _ in range(num):
            name, height = input().split()
            height = float(height)
            if height > max_height:
                max_height = height
                max_names = [name]
            elif height == max_height:
                max_names.append(name)
        
        print(" ".join(max_names))
