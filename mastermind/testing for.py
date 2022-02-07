

count_space = 0
count_dots = 0
count_commas = 0
user_text = input('What are you thinking about?')

for each in user_text:
    if " " == each:
        count_space += 1
    if "." == each:
        count_dots += 1
    if "," == each:
        count_commas += 1

input('Number of spaces: {}\n'
      'Number of dots:   {}\n'
      'Number of commas: {}\n'
      'Press ENTER to finish'.format(count_space, count_dots, count_commas))

exit()
