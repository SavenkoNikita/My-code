n = input()

if (int(n) % 10) == 1 and int(n) != 11:
    print('На лугу пасется ' + n + ' корова')
#elif :
#    print('На лугу пасется ' + n + ' коровы')
elif int(n) == 0 or int(n) >= 5 and int(n) <= 20 or (int(n) % 10) >=5 and (int(n) % 10) <= 10:
    print('На лугу пасется ' + n + ' коров')
else:
    print('error')

