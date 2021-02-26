n = input()
a = int(n) // 1000
b = int(n) // 100 % 10
c = int(n) // 10 % 10
d = int(n) % 10
print(int(a - d) + int(b - c) + int(1))
