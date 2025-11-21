# A closure happens when: 
# 1. A function is defined inside another function
# 2. The inner function remembers and can use the variables from the outer function
#       —even after the outer function has finished running.

def outer():
    x = 10   # a variable in the outer function

    def inner():
        print(x)  # inner function uses variable from outer function

    return inner  # return the inner function


# The key concept:
# outer() → returns the inner function
# outer()() → calls outer, gets inner, then calls inner
func = outer()
func()   # prints 10

