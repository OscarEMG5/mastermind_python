
number = int(input('Select a number to show the multiplying table\n'))
range_multiplying = range(1,11)

for line in range_multiplying:
    if line % 2 == 0:
        print('{} x {} = {}'.format(number, line, number*line))
