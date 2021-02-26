time = int(input())
day = time // 1440
hour = time // 60 - (day * 24)
min = time % 60
print(str(hour), str(min))
