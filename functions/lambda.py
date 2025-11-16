users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

def sort_users_by_age(user):
    return sorted(users, key=lambda x: x['age'])

sorted_users = sort_users_by_age(users)
print(sorted_users)

# Why use lambda here?

# sorted() needs a function to tell it how to sort.
# The lambda function provides a quick way to define that function inline,
# without needing to create a separate named function.