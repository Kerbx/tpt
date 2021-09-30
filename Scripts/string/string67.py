s = input()

for i in range(1, len(s) // 2):
    print(s[len(s) - i + 1] + s[i])

    if len(s) % 2 == 0:
        print(s[len(s) // 2 + 1])