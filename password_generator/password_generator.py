import random

upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_upper_letters = int(input("How many upper case letters would you like in your password?\n"))
nr_lower_letters = int(input("How many lower case letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
pass_len = nr_upper_letters + nr_lower_letters + nr_symbols + nr_numbers

def generate_password():
    password = [''] * pass_len
    for _ in range(nr_upper_letters):
        password[random.randint(0, pass_len - 1)] = random.choice(upper_letters)
    for _ in range(nr_lower_letters):
        password[random.randint(0, pass_len - 1)] = random.choice(lower_letters)
    for _ in range(nr_symbols):
        password[random.randint(0, pass_len - 1)] = random.choice(symbols)
    for _ in range(nr_numbers):
        password[random.randint(0, pass_len - 1)] = random.choice(numbers)
    return ''.join(password)

print(generate_password())




