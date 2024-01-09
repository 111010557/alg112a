import random

def neighbor(f, p, h=0.01):
    """返回鄰居點 p1 和其對應的高度 f1"""
    p1 = [x + random.uniform(-h, h) for x in p]
    f1 = f(p1)
    return p1, f1

def hillClimbing(f, p, h=0.01):
    failCount = 0  # 失敗次數歸零
    while failCount < 10000:  # 如果失敗次數小於一萬次就繼續執行
        f_now = f(p)  # f_now 為目前高度
        p1, f1 = neighbor(f, p, h)
        
        if f1 >= f_now:  # 如果移動後高度比現在高
            p = p1
            f_now = f1
            print('p=', p, 'f(p)=', f_now)
            failCount = 0  # 失敗次數歸零
        else:  # 若沒有更高
            failCount += 1  # 那就又失敗一次

    return p, f_now  # 結束傳回（已經失敗超過一萬次了）

def vector_function(v):
    # 可以根據需要修改
    return -sum(x**2 for x in v)

# 初始點 [2, 1, 3]
result = hillClimbing(vector_function, [2, 1, 3])
print("Final Result:", result)
