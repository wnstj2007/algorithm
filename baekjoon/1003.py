def fibo(n):
    zero = [1,0]
    one = [0,1]
    for i in range(2,n+1):
        zero.append(zero[i-1]+zero[i-2])
        one.append(one[i-1]+one[i-2])
    return str(zero[n])+" "+str(one[n])

n = int(input())
ans = []
for i in range(n):
    m = int(input())
    ans.append(fibo(m))
for i in ans:
    print(i)