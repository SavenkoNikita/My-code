a = int(input())
if (a % int(4) == int(0)) and a % int(100) != int(0) or a % int(400) == int(0):
    print("YES")
else:
    print("NO")
