
class game :
    def __init__(self):
        while True:
           print('''Welcome , Enter Game Number :
                1-odd and even numbers
                2-no duplication
                3-print numbers (0-n)
                4-print number accept division on num 2
                5-print number accept division on num 1 and 2 (0-100)
                6- exit
                ''')
           user_choice=int(input('Enter Game Number:'))
           if user_choice == 1:
               n = int(input("Enter number of list : "))
               self.odd_even(n)
           if user_choice == 2:
               sentence=input('Enter your sentence :')
               self.np_dup(sentence)
           if user_choice == 3:
               end=int(input('Enter end number :'))
               self.print_range(end)
           if user_choice == 4:
               num1=int(input('Enter end number1 :'))
               num2=int(input('Enter end number 2:'))
               self.print_div_2(num1,num2)
           if user_choice == 5:
               num1=int(input('Enter end number1 :'))
               num2=int(input('Enter end number 2:'))
               self.print_div(num1,num2)
           if user_choice == 6:
               print('Good Bye')
               break
           play_again=input('Do you want play again n to exit')
           if play_again=='n':
              print('Good Bye')
              break

    def print_div_2(self,num1,num2):
        for x in range(0,num1+1):
            if x % num2 == 0:
                print (x)
            

    def print_div(self,num1,num2):
        for x in range(0,100+1):
            if x % num1 == 0 and x % num2 ==0:
                print (x)
            
    def print_range(self,end):
        for x in range(0,end+1):
            print (x)


    def np_dup(self,sentence):
        not_duplicat=[]
        for word in sentence.split(' '):
            if word not in not_duplicat :
                not_duplicat.append(word)
        print(len(not_duplicat))


    def odd_even(self,n):
        n_list=[]
        for i in range(0, n):
            l_num = int(input( ))
            n_list.append(l_num)
        even_list=[]
        odd_list=[]
        for number in n_list:
            if  number % 2 == 0 :
                even_list.append(number)
            else :
                odd_list.append(number)
        print(f'''even list = {even_list} odd list = {odd_list}''')
        

g=game()  
    
