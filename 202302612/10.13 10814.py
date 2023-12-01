a= int(input())
data = []

for _ in range(a):

    Age, Name =input().split()
    age = int (Age)
    data.append((age,Name))

sort = sorted(data, key=lambda x: x[0])
for age, Name in sort:
    print(f"{age} {Name}")