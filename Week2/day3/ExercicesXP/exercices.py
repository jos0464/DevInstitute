# =========================================
# Exercise 1: Currency class with dunder methods
# =========================================
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        return f"{self.amount} {self.currency}s"

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        elif isinstance(other, int):
            return self.amount + other
        else:
            raise TypeError("Unsupported type for addition")

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        elif isinstance(other, int):
            self.amount += other
        else:
            raise TypeError("Unsupported type for addition")
        return self

# Test Currency
print("=== Currency Tests ===")
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)            # 5 dollars
print(int(c1))       # 5
print(repr(c1))      # 5 dollars
print(c1 + 5)        # 10
print(c1 + c2)       # 15
c1 += 5
print(c1)            # 10 dollars
c1 += c2
print(c1)            # 20 dollars
try:
    print(c1 + c3)   # TypeError
except TypeError as e:
    print(e)

# =========================================
# Exercise 3: Random string
# =========================================
import string
import random

print("\n=== Random String Test ===")
letters = string.ascii_letters
random_string = ''.join(random.choice(letters) for _ in range(5))
print("Random string:", random_string)

# =========================================
# Exercise 4: Current Date
# =========================================
from datetime import datetime

def show_current_date():
    today = datetime.now().date()
    print(f"Today's date: {today}")

print("\n=== Current Date ===")
show_current_date()

# =========================================
# Exercise 5: Time left until Jan 1
# =========================================
def time_until_january():
    now = datetime.now()
    next_year = datetime(now.year + 1, 1, 1)
    diff = next_year - now
    print(f"Time left until January 1st: {diff}")

print("\n=== Time until January 1st ===")
time_until_january()

# =========================================
# Exercise 6: Minutes lived since birthday
# =========================================
def minutes_lived(birthdate_str, fmt="%Y-%m-%d"):
    birthdate = datetime.strptime(birthdate_str, fmt)
    now = datetime.now()
    diff = now - birthdate
    minutes = int(diff.total_seconds() / 60)
    print(f"You have lived {minutes} minutes.")

print("\n=== Minutes Lived Test ===")
minutes_lived("2000-01-01")

# =========================================
# Exercise 7: Faker Module
# =========================================
from faker import Faker

fake = Faker()
users = []

def generate_users(n):
    for _ in range(n):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user)

print("\n=== Faker Users ===")
generate_users(5)
for u in users:
    print(u)
