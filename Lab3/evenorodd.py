def check_even_odd():
    number = int(input("Enter a number: "))
    
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

if _name_ == "_main_":
    check_even_odd()