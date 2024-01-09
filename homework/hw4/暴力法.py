def solve_quadratic_equation(a, b, c):
    solutions = []

    for x in range(-1000, 1001):  # 假設 x 的範圍在 -1000 到 1000 之間
        if a * x**2 + b * x + c == 0:
            solutions.append(x)

    return solutions

# 例子: x^2 - 3x + 1 = 0
a = 1
b = -3
c = 1

result = solve_quadratic_equation(a, b, c)

if result:
    print(f"Solutions: {result}")
else:
    print("No real solutions.")
