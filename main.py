products = {"Bubblegum": 202, "Toffee": 118, "Ice cream": 2250, "Milk chocolate": 1680, "Doughnut": 1075, "Pancake": 80}
income = 0.0
print("Earned amount:")
for key, value in products.items():
    print(f"{key}: ${value}")
    income += value
print(f"Income: ${income}")

print("Staff expenses:")
staff_expenses = int(input())
print("Other expenses:")
other_expenses = int(input())
print(f"Net income: ${income - (staff_expenses + other_expenses)}")