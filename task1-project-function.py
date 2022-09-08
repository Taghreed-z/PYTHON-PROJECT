
def odd_even(list):
    even_list=[]
    odd_list=[]
    for number in n_list:
        if  number % 2 == 0 :
            even_list.append(number)
        else :
            odd_list.append(number)
    print(f'''even list = {even_list}
odd list = {odd_list}''')
        

n = int(input("Enter number of list : "))
n_list=[]
for i in range(0, n):
    l_num = int(input( ))
    n_list.append(l_num)  

odd_even(n_list)  
    
