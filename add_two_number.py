def add(x,y):
        return x+y
def subtract(x,y):
        return x-y
def calculator():
        print("select option")
        print("1. add")
        print("2. sabtract")
        while True:
                choice = input("enter choice (1,2):")
                if choice in ('1','2'):
                    num1 = float(input("enter the first number :"))
                    num2 = float(input("enter the second number ;"))
                    if choice == '1':
                        print(num1+num2)
                    elif choice == '2':
                        print(num1-num2)
                else :
                    print("invalide input")

calculator()                    
                    

        
    
    