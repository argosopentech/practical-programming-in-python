print('Grocery list:')
print('"add" to add items and "view" to view list')
grocery_list = []
while True:
    command = input('Enter command: ')
    if command == 'add':
        to_add = input('Enter new item: ')
        grocery_list.append(to_add)
    # elif stands for "else if"
    elif command == 'view':
        for i in range(len(grocery_list)):
            print(grocery_list[i])
    else:
        print('Invalid command')
