def gcd(a, b):
    if a < b:
        a, b = b, a
    
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


num1 = 12
num2 = 18
result = gcd(num1, num2)
print(f"НОД чисел {num1} и {num2} равен {result}")