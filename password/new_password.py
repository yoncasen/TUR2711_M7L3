import random
import string
import os

characters_low = string.ascii_letters
characters_medium = string.ascii_letters + string.digits
characters_high = string.ascii_letters + string.digits + string.punctuation

def generate_password(length=12, password_strongness = 2):
    """Belirtilen uzunlukta rastgele bir şifre oluşturur."""

    password = ''
    for i in range(length):
        if password_strongness == 1:
            password += random.choice(characters_low)
        elif password_strongness == 2:
            password += random.choice(characters_medium)
        elif password_strongness == 3:
            password += random.choice(characters_high)
    return password

# // CONFIG
password_length     =  10*10
password_strongness =  3

# // LOGIC
generated_password = generate_password(password_length, password_strongness)

print("Yeni şifreniz:", generated_password)
