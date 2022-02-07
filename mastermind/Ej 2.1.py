
import os

numbers_list = []
number = ()
question_continue = 'Yes'

while question_continue == 'Yes':
    number = int(input('please enter a number to create a list:'))
    numbers_list.append(number)
    question_continue = ()

    while question_continue not in ['Yes', 'No']:
        question_continue = input('Do you want to enter a new number? (Yes or No)\n')
        os.system('cls')

min_number = numbers_list[0]
max_number = numbers_list[0]

for min in numbers_list:
    if min < min_number:
        min_number = min
for max in numbers_list:
    if max > max_number:
        max_number = max

print('Your maximum number is: {} \n'
      'Your minimum number is: {} \n'.format(max_number, min_number))

input('Press ENTER to finish')
