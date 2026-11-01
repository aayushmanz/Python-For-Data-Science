# datatypes :



# 1. None Type : 
def welcome (name=None):
    if name is None or name is "":
        print(f"hello , Guest")
    else:
        print(f"hello , {name}")
    
    
if __name__ == "__main__":
    name = input("Enter Your Name : ")
    welcome(name)    


# 2. Numeric Type :

def numtype(value):
    match value :
        case 1:
            val = map(int,input().split())
            integer(*val)
            
        case 2:
            val = map(float, input().split())
            floated(*val)
            
        case _:
            print("Invalid Choice !")


def  integer(*args):
    
    value = 0
    
    for i in args:
        value += i
        
    print(f"Your added values are : {value}")    


def floated(*args):
    
    value = 0
    
    for i in args:
        value += i
        
    print(f"the sum of float values : {value}")           
        
        
if __name__ == "__main__":
    a = int(input("Enter the choice 1 for int and 2 for float : "))
    numtype(a)
    
        
    
    
    
            
        