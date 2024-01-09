import micrograd as mg

def df(f, p, k):
    x = [mg.Tensor(xi, True) for xi in p]
    y = f(x)
    y.backward()
    return p[k].grad()

def grad(f, p):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return gp

def Gradient(f, p, step=0.01):
    p = [mg.Tensor(pi, True) for pi in p]

    while True:
        last_h = f(p).item()
        d = grad(f, p)
        cur = [pi - d[i] * step for i, pi in enumerate(p)]
        p = [mg.Tensor(pi.item(), True) for pi in cur]
        cur_h = f(p).item()

        if cur_h < last_h:
            print("p=", [pi.item() for pi in p], "\t", "f(p)=", cur_h)
        else:
            break

# 測試
def f(p):
    return sum(xi**2 for xi in p)

Gradient(f, [2.0, 1.0, 3.0])
