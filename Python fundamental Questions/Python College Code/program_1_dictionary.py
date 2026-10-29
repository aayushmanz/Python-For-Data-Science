

def create_dict():
    
    k = input("Enter the key name : ")
    choice = int(input("Enter the choice ( 1 for number value and 2 for string value : )"))
    match choice:
        case 1:
            v = int(input("Enter the number as a value : "))
        case 2: 
            v = input("Enter string value : ")
        case _:
            print("invaild choice !")    
            
    data = {
        k : v
    }   
    

def display(): 
    print(f'{data.items}')         
    
            
if __name__ == "__main__":
    
    result = create_dict()
    
   if result is none:
    display()

    