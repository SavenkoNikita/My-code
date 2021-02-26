a = int(input())
b = int(input())
c = a % b
try:
    d = c / c
    print('No')
except:
    print('YES')
