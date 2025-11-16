def specify_argument_return_type(value: int) -> bool:
    return isinstance(value, int)

value = specify_argument_return_type("Hello")  # We can pass a string instead of an int even though the type hint specifies int
print(value)  # Output: False