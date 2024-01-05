n=int(input("number:"))
print("\n")
fib=[0,1]
for i in range(n):
    if i<2:
        print(fib[i],end=",")
    if i>=2:
        fib.append(fib[i-1]+fib[i-2])
        print(fib[i],end=",")