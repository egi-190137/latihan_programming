from itertools import groupby, product


K, M = list(map(int, input().split()))

def f(x):
    return (int(x)**2)%M #since (a+b)mod(c) = a mod(c) + b mod(c)
        
Nels, vals= [], []
for i in range(K):
    ipt = input().split()
    newval = [k for k, g in groupby(map(f, ipt[1:]))] #The groupby is to get rid of redundant values 
    Nels.append(len(newval))
    vals.append(newval)
prd = product(*vals)
resum = [sum(list(sub))%M for sub in prd]
print(max(resum))