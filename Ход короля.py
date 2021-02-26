line_1 = int(input())
column_1 = int(input())
line_2 = int(input())
column_2 = int(input())
r_line = line_1 - line_2
r_column = column_1 - column_2
if r_line <= 1 and r_line >= -1 and r_column <= 1 and r_column >= -1:
    print('YES')
else:
    print('NO')
