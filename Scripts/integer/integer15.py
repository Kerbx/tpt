a = int(input())
print(int(str(a % 100 // 10) + str(a // 100) + str(a % 10)))