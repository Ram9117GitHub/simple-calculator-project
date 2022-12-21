# Program make a simple calculator

#This function adds two numbers
def add(x,y):
    return x+y
# This function subtracts two numbers
def subtract(x,y):
    return x-y
# This function multiplies two numbers
def multiply(x,y):
    return x*y
# This function divides two numbers
def divide(x,y):
    return x/y
# This function LCM two numbers
def lcm(x,y):
    L=x if x>y else y
    while L<=x*y:
        if L%x==0 and L%y==0:
            return L
        L+=1
# This function HCF two numbers
def hcf(x,y):
    H=x if x<y else y
    while H>=1:
        if x%H==0 and y%H==0:
            return H
        H-=1
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.LCM")
print("6.HCF")
while True:
    #take input from the user
    choice=input("Enter choice(1/2/3/4/5/6):")
    #take if choice is one of the six options
    if choice in ('1','2','3','4','5','6'):
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        if choice=='1':
            print(num1,"+",num2,"=",add(num1,num2))

        elif choice=='2':
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif choice=='3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice=='4':
            print(num1,"/",num2,"=",divide(num1,num2))
        elif choice=='5':
            print(num1,"LCM",num2,"=",lcm(num1,num2))
        elif choice=='6':
            print(num1,"HCF",num2,"=",hcf(num1,num2))
        #check if user wants another calculation
        #break the while loop if answer is no
        next_calculation=input("Let's do next calculation?(yes/no):")
        if next_calculation=="no":
            break
        else:
            print("Invalid Input")


    







            
    
