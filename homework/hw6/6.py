# 函數 f 對變數 p[k] 的偏微分: df / dp[k]
def df(f, p, k,step=0.01):
    p1 = p.copy()
    p1[k] = p[k]+step
    return (f(p1) - f(p)) / step

# 梯度：函數 f 在點 p 上的梯度
def grad(f, p):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return gp

def Gradient(f,p,step=0.01):
    while 1:
        last_h=f(p)
        d=grad(f,p)
        cur=p.copy()
        for i in range(len(cur)):
            cur[i]-=d[i]*step
        cur_h=f(cur)
        if cur_h<last_h:
            p=cur
            print("p=",p,"\t","f(p)=",cur_h)
        else:
            break

def f(p):
    sum=0
    for i in p:
        sum+=i**2
    return sum

Gradient(f,[2,1,3])