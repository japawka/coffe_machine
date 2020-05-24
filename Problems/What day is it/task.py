time = int(input())
if time + 10.5 > 24:
    print('Wednesday')
elif 10.5 + time < 0:
    print('Monday')
else:
    print('Tuesday')
