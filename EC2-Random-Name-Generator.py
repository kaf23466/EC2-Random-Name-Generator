import random
import string

def generate_name(department):
    """Generate a name using department and random characters/numbers."""
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"{department}-{random_part}"

num_instances = int(input("Number of EC2 names needed? "))
department = input("Department name: ")

for _ in range(num_instances):
    print(generate_name(department))
