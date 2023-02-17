import random
import string
def password(lenght):
    symbols = list(string.digits + string.ascii_letters + '!@#$%^&*()<>?/')
    random.shuffle(symbols)
    x = []
    for i in range (lenght):
        x.append(random.choice(symbols))
    print(''.join(x))
          
answer = input('Do you want to create a new password?Yes/No ')    
if answer.lower() == 'yes':
    x = int(input('What is your password lenght? '))
    password(x)
else: print('Good bye!')

