n = int(input())
arr = []
max = 0
result = ""

for _ in range(n):
   arr.append(input())

book = list(set(arr))
book.sort()

for i in book:
   if max == arr.count(i):
      continue
   elif max < arr.count(i):
      result = i
      max = arr.count(i)
      
print(result)