
def get_next_number():
    yield 1
    yield 2
        
print(next(get_next_number()))
print(next(get_next_number()))