
print('Supermarket list')

import os

supermarket_list = []
product = ()
add_product = ()


while 'Q' not in product:

    print(supermarket_list)
    product = input('What would you like to buy? ([Q to exit]')
    add_product = ()

    if product == 'Q':
        input('The supermarket list is:\n\n {}'.format(supermarket_list))
        exit()

    elif product not in supermarket_list:

        while add_product not in ['Yes', 'No']:
            add_product = None
            add_product = input('Do you want to add {} to the list? (Yes or No)'.format(product))

            if add_product == 'Yes':
                supermarket_list.append(product)
                print('{} Added to the list!'.format(product))
                os.system('cls')

    else:
        print('{} is already in the list'.format(product))
        os.system('cls')

exit()