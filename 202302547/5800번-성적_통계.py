n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))
    del arr[i][0]
    arr[i].sort(reverse=True)
    
lagest_gap = lambda arr: max([arr[i]-arr[i+1] for i in range(len(arr)-1)])

for i in range(n):
    print("Class {0}".format(i+1))
    print("Max {0}, Min {1}, Largest gap {2}".format(max(arr[i]), min(arr[i]), lagest_gap(arr[i])))