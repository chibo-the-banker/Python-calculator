# Calculator
def calculator():
        x= int(input("Pick a number, any number🙂: "))
        y= int(input("Now pick another number🙂: "))
        operator = input("Great, now let's do a liitle bit more. Choose an operater. You can \n add (+) \n subtract(-) \n multiply(*) \n divide(/) ")
    
        if operator == '+':
            print(f"The sum of the two numbers is {x+y}")
        
        elif operator == '-' :
            print(f'The difference between the two numbers {x-y}')
        
        elif operator == '*' :
            print(f'The multiplication of the two numbers {x*y}')
        
        elif operator == '/':
            print(f'The result of {x} divided by {y} is {x/y}')
        
        else:
            print("That is an invalid operator. Choose another")

        answer = input("Shall we calculate again (yes/no): ")
        if answer == 'yes':
             calculator()

        else:
             print("Phew 😮‍💨 no integration.")

calculator()
