from scipy.optimize import newton

# 定義方程
def equation(x):
    return x**5 + 1

# 初始猜測值
initial_guess = 0.0

# 使用牛頓法求解方程
solution = newton(equation, initial_guess)

# 顯示結果
print(f"解 x：{solution}")
