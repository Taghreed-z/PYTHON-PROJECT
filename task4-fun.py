
def print_range(num1,num2):
    for x in range(0,num1+1):
        if x % num2 == 0:
            print (x)
    

num1=int(input('Enter end number1 :'))
num2=int(input('Enter end number 2:'))
print_range(num1,num2)
