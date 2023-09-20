score = []
for _ in range(8) :
    score.append(int(input()))

sorted_score = sorted(score, reverse=True)

print(sum(sorted_score[:5]))

problem_number = []
for i in sorted_score[:5] :
    problem_number.append(score.index(i))
problem_number.sort()
for i in problem_number :
    print(i + 1, end=' ')