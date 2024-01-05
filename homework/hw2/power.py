# 方法 1
def power2n(n):
    return 2**n

# 方法 2a：用遞迴
def power2n_2a(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2

    return power2n_2a(n-1)+power2n_2a(n-1)

# 方法2b：用遞迴
def power2n_2b(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2

    return 2*power2n_2b(n-1)


# 方法 3不會