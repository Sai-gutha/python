def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print('select operation:')
print('1.add')
print('2.sub')
print('3.mul')
print('4.div')

while True:
    choice = input('Enter a choice(1/2/3/4):')
    
    if choice in ('1','2','3','4'):
        num1 = int(input('Enter a first_number:'))
        num2 = int(input('Enter a second_number:'))
    
    if choice == '1':
        print(add(num1, num2))
    elif choice == '2':
        print(sub(num1, num2))
    elif choice == '3':
        print(mul(num1, num2))
    elif choice == '4':
        print(div(num1, num2))
    next_calculation = input('if you want to continue calulation(yes/no):')
    if next_calculation == 'no':
        break;
    else:
        print('Invalid Input')