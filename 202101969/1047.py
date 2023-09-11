people, party = map(int, input().split())
true_people = set(input().split()[1:])
tr = []
for i in range(party):
    tr.append(set(input().split()[1:]))
for _ in range(party):
    for p in tr:
        if p & true_people:
            true_people = true_people.union(p)
c = 0
for p in tr:
    if p & true_people:
        continue
    c +=1
print(c)






