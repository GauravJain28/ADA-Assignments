import random
import matplotlib.pyplot as plt

random.seed(10)
n=100
M=10000
listset=[]
X=[]
Y1=[]
Yr=[]
p=16747
for i in range(1,n+1):
    r = random.randint(1,p-1)
    set1 = set()
    dic = {}
    X.append(i)
    for j in range(i):
        set1.add(j*n)
    for j in range(n-i):
        set1.add(random.randint(0,M-1))
    for k in set1:
        x = k%n
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1
    
    Keymax = max(zip(dic.values(), dic.keys()))[1]
    Y1.append(dic[Keymax])

    dic={}
    for k in set1:
        x = ((r*k)%p)%n
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1
    Keymax = max(zip(dic.values(), dic.keys()))[1]
    Yr.append(dic[Keymax])
plt.plot(X,Y1, label = 'H()')
plt.plot(X,Yr, label = 'Hr()')
plt.grid()
#plt.title("")
plt.legend()
plt.xlabel('k')
plt.ylabel('Maxchain length')
#plt.title('PMF')
plt.savefig('plot5.png')
print("Plot saved")

