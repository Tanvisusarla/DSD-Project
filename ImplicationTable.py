from tabulate import tabulate
import numpy as np 
import itertools

# number of elements
nu = int(input("Enter number of minterms : "))
if nu > 15 :
  raise Exception("Error: enter values in range [0,15]")
# Below line read inputs from user using map() function
q= list(map(int, 
	input("\nEnter the min or max terms 0-15: ").strip().split()))[:nu]
for i in q:
        if i > 15:
          raise Exception("Error: enter values in range [0,15]")


du = int(input("Enter number of dont cares : "))

dont_cares = list(map(int, 
	input("\nEnter the dont care terms 0-15: ").strip().split()))[:du]

q.extend(dont_cares)
print("\nThe Min/Maxterm List is - ", q)


def bin4(grpn):
    for i in range(len(grpn)):
         grpn[i]= f'{grpn[i]:04b}'
    return grpn


z=[] #to store binary values of minterms

for i in range(len(q)):
    z.append(f'{q[i]:04b}')

#print(" minterms  : ", z) 

#column1 grouping convert to def
grp0= []
grp1= []
grp2= []
grp3= []
grp4= []
for i in range(len(q)):
    c= z[i].count('1')
    if (c==0):
        grp0.append(q[i])
    elif (c==1):
        grp1.append(q[i])
    elif (c==2):
        grp2.append(q[i])
    elif (c==3):
        grp3.append(q[i])
    else:
        grp4.append(q[i])
    



#column2

def unite(grpM,grpN):
    ref=[]
    for i in grpM:
        for j in grpN:
            strRef = i ^ j
            Str2= f'{strRef:04b}'
            f= Str2.count('1')
            if (f==1):
                Str2= Str2.replace("1", "-")
                x = Str2.find("-")
                temp = list(f'{j:04b}') 
                temp[x] = '-'
                Str2 = "".join(temp)
                ref.append(Str2)   

    return ref

grp21=list(unite(grp0,grp1))
grp22=list(unite(grp1,grp2))
grp23=list(unite(grp2,grp3))
grp24=list(unite(grp3,grp4))
column2= [grp21,grp22,grp23,grp24]  

#def unite2(grpM,grpN)
def unite2(grpM,grpN):
        ref=[]
        for w in grpM :
                for z in grpN:
                        x = w.find("-")
                        y = z.find("-")
                        if(x==y):
                                temp1=list(w)
                                temp2=list(z)
                                for i in range(len(temp1)):
    	                                if(temp1[i]!=temp2[i]):
                                                temp1[i]='*'
                                
                                a = "".join(temp1)
                                c = a.count('*')                       
                                if c == 1:
                                        rep=a.replace('*','-')
                                        if rep not in ref:
                                            ref.append(rep)
                                       
                                                                        

                
        return ref
                        


grp31=unite2(grp21,grp22,)
grp32=unite2(grp22,grp23)
grp33=unite2(grp23,grp24)

column3=[grp31,grp32,grp33]

mint=[grp0,grp1,grp2,grp3,grp4]
c_names=["column1","column2","column3"]
column1=[bin4(grp0),bin4(grp1),bin4(grp2),bin4(grp3),bin4(grp4)]

imp_val=list((column1,column2,column3))

#print ('column 1 \n ',column1)
#print ("*********\n  column2 \n ", column2)
#print ("*********\n  column3 \n ", column3)

table=list(itertools.zip_longest(*imp_val, fillvalue=" "))

print(tabulate(table,headers=c_names))

#######find prime implicants in each row