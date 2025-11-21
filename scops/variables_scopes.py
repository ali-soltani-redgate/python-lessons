b = 10


def change_local_b():
    b = 30  # This creates a new local variable 'b', does not affect the global 'b'

change_local_b()
print(b)  # Output: 10

def change_b():
    global b # This tells Python to use the global 'b'
    b = 20

change_b()
print(b)  # Output: 20 


def change_b_nonlocal():
    c = 5

    def inner_function_with_nonlocal():
        nonlocal c # This tells Python to use the 'c' from the enclosing scope
        c = 15
    inner_function_with_nonlocal()
    print("Inner c:", c)  # Output: Inner c: 15
    
    def inner_function_without_nonlocal():
        c = 25
        print("Inner c without nonlocal:", c)  # Output: Inner c without nonlocal: 25
        

    inner_function_without_nonlocal()
    print("Outer c after inner without nonlocal:", c)  # Output: Outer c after inner without nonlocal: 15
    
