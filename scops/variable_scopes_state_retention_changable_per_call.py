
def outer(start):
        state = start                  # Each call gets its own state
        def inner(label):
            nonlocal state             # Remembers state in enclosing scope
            state += 1                 # Allowed to change it if nonlocal
            print(label, state)
        return inner

counter_a = outer(0)               # Create a counter starting at 0
counter_b = outer(100)             # Create a counter starting at 100
counter_a('A')                    # Output: A 1
counter_a('A')                    # Output: A 2
counter_b('B')                    # Output: B 101
counter_a('A')                    # Output: A 3
counter_b('B')                    # Output: B 102