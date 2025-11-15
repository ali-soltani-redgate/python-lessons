a = 10 # a is an integer, which is immutable
def change_mutable(a):
     a = 20  # This modifies the local copy of 'a', does not affect the original 'a'

change_mutable(a)
print(a)  # Output: 10

b = [1, 2, 3]  # b is a list, which is mutable
def change_mutable_list(b):
    b.append(4)  # This modifies the original list 'b'

change_mutable_list(b)
print(b)  # Output: [1, 2, 3, 4]