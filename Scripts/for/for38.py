# for38 Прохоренков Егор ИСП-211.
n = int(input())
p = n
_sum = 0.0

for i in range(1, n + 1):
    _sum += i ** p
    p -= 1
    
print(_sum)