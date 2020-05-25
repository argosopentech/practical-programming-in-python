def is_even(x):
    return x % 2 == 0

user_input = int(input('Is even? '))
if is_even(user_input):
    print('This is even')
else:
    print('This is not even')
