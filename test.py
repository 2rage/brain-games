def gcd(a, b):
    if a < b:
        a, b = b, a
    
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


num1 = 4
num2 = 3
result = gcd(num1, num2)
print(f"НОД чисел {num1} и {num2} равен {result}")


def arithmetic_progression(first_num, difference, n):
    progression = []
    current_item = first_num
    for _ in range(n):
        progression.append(current_item)
        current_item += difference
    return progression

import random
first_num = random.randint(1, 100)
difference = random.randint(1, 100)
n = random.randint(5, 15)

print(first_num, difference, n)

progression = arithmetic_progression(first_num, difference, n)
print(progression)