num1 = int(input("enter a number "))
num2 = int(input("enter a number "))
opp = input("enter a sign ")

def calculate_addition(a,b):
    return a + b 
def calculate_sub(a,b):
    return a - b
def calculate_mul(a,b):
    return a * b 
def calculate_div(a,b):
    try:
        return a/b
    except:
        print("can't divide by 0")
        return "not defined"

if opp == '+':
    print(num1 , opp , num2 , "=" , calculate_addition(num1,num2))
elif opp == '-':
    print(num1 , opp , num2 , "=" , calculate_sub(num1,num2))
elif opp == '*':
    print(num1 , opp , num2 , "=" , calculate_mul(num1,num2))
elif opp == '/':
    print(num1 , opp , num2 , "=" , calculate_div(num1,num2))
else:
    print('invalid sign')
