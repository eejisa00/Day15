st=input()
li=[]
Li=[]
em=[]
emp=""
alpha=[]
alpha2=[]
lo=st.lower()

for j in range(97,123):
    alpha.append(chr(j))
   
for i in lo:
    li.append(ord(i))
    Li.append(i)

c=0
for k in li:
    if(k>c):
        c=k
ma=c

ind=li.index(ma)
let=Li[ind]
oo=int(alpha.index(let))+1
emp=emp+str(oo)+let

if(let in st):
    print(emp)
else:
    print(emp.upper())
