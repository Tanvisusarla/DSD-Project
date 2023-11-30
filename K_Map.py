import re
from tabulate import tabulate
import numpy as np
def karnaughmap(minterms):
    import copy
    min_max=input("Enter 'min' for minterms and 'max' for maxterm : ")
    #all_terms=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    #m_terms=[]
    #if min_max=='min':
    #    m_terms=minterms
    #elif min_max=='max':
    #    for i in range(len(all_terms)):
    #        if all_terms[i] not in list(all_terms):
    #            m_terms.append(all_terms[i])

    table=[]
    (tmp,flag)=(0,0)
    op=''

    for i in range(4):
        table.append([0]*4)
    for i in range(4):
        for j in range(4):
            if i<2:
                bi='0'+bin(i)[2:]
            else:
                bi=bin(i)[2:]
            if j<2:
                bj='0'+bin(j)[2:]
            else:
                bj=bin(j)[2:]
            p=int('0b'+bi+bj,2)
            if p in minterms:
                table[i][j]=1
    for i in range(4):
        (table[i][2],table[i][3])=(table[i][3],table[i][2])
    for i in range(4):
        (table[2][i],table[3][i])=(table[3][i],table[2][i])


    print("The Karnaugh-map is : ")
    table=list(table)
    top_bin_array=['00', '01', '11', '10']
    left_bin_array=['00', '01', '11', '10']
    table1=np.append(np.transpose(left_bin_array),table)
    print(tabulate(table1,headers=top_bin_array))
  

    #print("\n array", table)

    octa=[]
    qrd=[]
    qrd_ref=[]
    qrd_rep=[]
    dul=[]
    sngl=[]
    
    octa_val=[["C' ","D ","C ","D' "],["A' ","B ","A ","B' "]]  
    qrd_val=[["C'D' ","C'D ","CD ","CD' "],["A'B' ","A'B ","AB ","AB' "]]  
    qrd_val_4=[["A'C' ","A'D ","A'C ","A'D' "],["BC' ","BD ","BC ","BD' "],["AC' ","AD ","AC ","AD' "],["B'C' ","B'D ","B'C ","B'D' "]]
    dul_vert=[["A'C'D' ","A'C'D ","A'CD ","A'CD' "],["BC'D' ","BC'D ","BCD ","BCD' "],["AC'D' ","AC'D ","ACD ","ACD' "],["B'C'D' ","B'C'D ","B'CD ","B'CD' "]]
    dul_horz=[["A'B'C' ","A'B'D ","A'B'C ","A'B'D' "],["A'BC' ","A'BD ","A'BC ","A'BD' "],["ABC' ","ABD ","ABC ","ABD' "],["AB'C' ","AB'D ","AB'C ","AB'D' "]]
    sngl_val=[["A'B'C'D' ","A'B'C'D ","A'B'CD ","A'B'CD' "],["A'BC'D' ","A'BC'D ","A'BCD ","A'BCD' "],["ABC'D' ","ABC'D ","ABCD ","ABCD' "],["AB'C'D' ","AB'C'D ","AB'CD ","AB'CD' "]]
    if table==[[1]*4,[1]*4,[1]*4,[1]*4]:
        op='1'
    else:
        for i in range(-1,3):
            if table[i][0]==1 and table[i][1]==1 and table[i][2]==1 and table[i][-1]==1 and table[i+1][0]==1 and table[i+1][1]==1 and table[i+1][2]==1 and table[i+1][-1]==1:
                op=op+octa_val[1][i]
                octa.append([(i,0),(i,1),(i,2),(i,-1)])
                if i<2:
                    octa.append([(i+1,0),(i+1,1),(i+1,2),(i+1,-1)])
                else:
                    octa.append([(-1,0),(-1,1),(-1,2),(-1,-1)])
                if i<2:
                    octa.append([(i,0),(i+1,0),(i,1),(i+1,1)])
                    octa.append([(i,1),(i+1,1),(i,2),(i+1,2)])
                    octa.append([(i,2),(i+1,2),(i,-1),(i+1,-1)])
                    octa.append([(i,-1),(i+1,-1),(i,0),(i+1,0)])
                else:
                    octa.append([(i,0),(-1,0),(i,1),(-1,1)])
                    octa.append([(i,1),(-1,1),(i,2),(-1,2)])
                    octa.append([(i,2),(-1,2),(i,-1),(-1,-1)])
                    octa.append([(i,-1),(-1,-1),(i,0),(-1,0)])

        for i in range(-1,3):
            if table[0][i]==1 and table[1][i]==1 and table[2][i]==1 and table[-1][i]==1 and table[0][i+1]==1 and table[1][i+1]==1 and table[2][i+1]==1 and table[-1][i+1]==1:
                op=op+octa_val[0][i]    
                octa.append([(0,i),(1,i),(2,i),(-1,i)])
                if i<2:
                    octa.append([(0,i+1),(1,i+1),(2,i+1),(-1,i+1)])
                else:
                    octa.append([(0,-1),(1,-1),(2,-1),(-1,-1)])
                if i<2:
                    octa.append([(0,i),(1,i),(0,i+1),(1,i+1)])
                    octa.append([(1,i),(2,i),(1,i+1),(2,i+1)])
                    octa.append([(2,i),(-1,i),(2,i+1),(-1,i+1)])
                    octa.append([(-1,i),(0,i),(-1,i+1),(0,i+1)])
                else:
                    octa.append([(0,i),(1,i),(0,-1),(1,-1)])
                    octa.append([(1,i),(2,i),(1,-1),(2,-1)])
                    octa.append([(2,i),(-1,i),(2,-1),(-1,-1)])
                    octa.append([(-1,i),(0,i),(-1,-1),(0,-1)])

        for i in range(-1,3):
            if table[i][0]==1 and table[i][1]==1 and table[i][2]==1 and table[i][-1]==1:
                qrd_ref.append([(i,0),(i,1),(i,2),(i,-1)])
            if table[0][i]==1 and table[1][i]==1 and table[2][i]==1 and table[-1][i]==1:
                qrd_ref.append([(0,i),(1,i),(2,i),(-1,i)])

        for i in range(-1,3):
            for j in range(-1,3):
                if table[i][j]==1 and table[i][j+1]==1 and table[i+1][j]==1 and table[i+1][j+1]==1:
                    if i==2 and j==2:
                        temp=[(i,j),(-1,j),(i,-1),(-1,-1)]
                    elif i==2 and j<2:
                        temp=[(i,j),(-1,j),(i,j+1),(-1,j+1)]
                    elif j==2 and i<2:
                        temp=[(i,j),(i+1,j),(i,-1),(i+1,-1)]
                    else:
                        temp=[(i,j),(i+1,j),(i,j+1),(i+1,j+1)]
                    qrd_ref.append(temp)
        
            
        for i in range(-1,3):
            if table[i][0]==1 and table[i][1]==1 and table[i][2]==1 and table[i][-1]==1:
                if [(i,0),(i,1),(i,2),(i,-1)] not in octa:
                    op=op+qrd_val[1][i]
                    qrd.append([(i,0),(i,1)])
                    qrd.append([(i,1),(i,2)])
                    qrd.append([(i,2),(i,-1)])
                    qrd.append([(i,-1),(i,0)])

        for i in range(-1,3):
            if table[0][i]==1 and table[1][i]==1 and table[2][i]==1 and table[-1][i]==1:
                if [(0,i),(1,i),(2,i),(-1,i)] not in octa:
                    op=op+qrd_val[0][i]
                    qrd.append([(0,i),(1,i)])
                    qrd.append([(1,i),(2,i)])
                    qrd.append([(2,i),(-1,i)])
                    qrd.append([(-1,i),(0,i)])

        for i in range(-1,3):
            for j in range(-1,3):
                if table[i][j]==1 and table[i][j+1]==1 and table[i+1][j]==1 and table[i+1][j+1]==1:
                    if i==2 and j==2:
                        temp=[(i,j),(-1,j),(i,-1),(-1,-1)]
                    elif i==2 and j<2:
                        temp=[(i,j),(-1,j),(i,j+1),(-1,j+1)]
                    elif j==2 and i<2:
                        temp=[(i,j),(i+1,j),(i,-1),(i+1,-1)]
                    else:
                        temp=[(i,j),(i+1,j),(i,j+1),(i+1,j+1)]
                    if temp not in octa:
                        op=op+qrd_val_4[i][j]
                        if i<2 and j<2:
                            qrd.append([(i,j),(i,j+1)])
                            qrd.append([(i+1,j),(i+1,j+1)])
                            qrd.append([(i,j),(i+1,j)])
                            qrd.append([(i,j+1),(i+1,j+1)])
                        if j==2 and i<2:
                            qrd.append([(i,j),(i,-1)])
                            qrd.append([(i+1,j),(i+1,-1)])
                            qrd.append([(i,j),(i+1,j)])
                            qrd.append([(i,-1),(i+1,-1)])
                        if j<2 and i==2:
                            qrd.append([(i,j),(i,j+1)])
                            qrd.append([(-1,j),(-1,j+1)])
                            qrd.append([(i,j),(-1,j)])
                            qrd.append([(i,j+1),(-1,j+1)])
                        if i==2 and j==2:
                            qrd.append([(i,j),(i,-1)])
                            qrd.append([(-1,j),(-1,-1)])
                            qrd.append([(i,j),(-1,j)])
                            qrd.append([(i,-1),(-1,-1)])
                    
        for i in range(-1,3):
            for j in range(-1,3):
                if table[i][j]==1 and table[i][j+1]==1:
                    if j==2:
                        temp=[(i,j),(i,-1)]
                    else:
                        temp=[(i,j),(i,j+1)]
                    if temp not in qrd:
                        op=op+dul_horz[i][j]
                        if j==2:
                            dul.append([(i,j),(i,-1)])
                        else:
                            dul.append([(i,j),(i,j+1)])
                if table[i][j]==1 and table[i+1][j]==1:
                    if i==2:
                        temp=[(i,j),(-1,j)]
                    else:
                        temp=[(i,j),(i+1,j)]
                    if temp not in qrd:
                        op=op+dul_vert[i][j]
                        if i==2:
                            dul.append([(i,j),(-1,j)])
                        else:
                            dul.append([(i,j),(i+1,j)])

        for each in octa:
            sngl.extend(each)
        for each in qrd:
            sngl.extend(each)
        for each in dul:
            sngl.extend(each)
        for i in range(-1,3):
            for j in range(-1,3):
                if table[i][j]==1:
                    if (i,j) not in sngl:
                        op=op+sngl_val[i][j]

        op=op.strip()
        opl=op.split(" ")
        for i in range(len(opl)):
            opl[i]=opl[i]+" "
    
        dulref=copy.deepcopy(dul)

        for each in dul:
            (d1,d2)=(each[0],each[1])
            (cntd1,cntd2)=(0,0)
            for each in dulref:
                if d1 in each:
                    cntd1+=1
                if d2 in each:
                    cntd2+=1
            for each in qrd_ref:
                if d1 in each:
                    cntd1+=1
                if d2 in each:
                    cntd2+=1   
            if cntd1>1 and cntd2>1:
                try:
                    if d1[0]==d2[0]:
                        opl.remove(dul_horz[d1[0]][d1[1]])
                    if d1[1]==d2[1]:
                        opl.remove(dul_vert[d1[0]][d1[1]])
                    dulref.remove([(d1[0],d1[1]),(d2[0],d2[1])])
                except ValueError:
                    continue
    
        for each in qrd_ref:
            (d1,d2,d3,d4)=(each[0],each[1],each[2],each[3])
            (d1cnt,d2cnt,d3cnt,d4cnt)=(0,0,0,0)
            for each1 in dul:
                if d1 in each1:
                    d1cnt+=1
                if d2 in each1:
                    d2cnt+=1
                if d3 in each1:
                    d3cnt+=1
                if d4 in each1:
                    d4cnt+=1
            for each2 in qrd_ref:
                if each!=each2:
                    if d1 in each2:
                        d1cnt+=1
                    if d2 in each2:
                        d2cnt+=1
                    if d3 in each2:
                        d3cnt+=1
                    if d4 in each2:
                        d4cnt+=1
            if d1cnt>0 and d2cnt>0 and d3cnt>0 and d4cnt>0:
                try:
                    if d1[0]!=d2[0] and d1[1]!=d3[1]:
                        opl.remove(qrd_val_4[d1[0]][d1[1]])
                except ValueError:
                    continue

        for each in qrd_ref:
            (d1,d2,d3,d4)=(each[0],each[1],each[2],each[3])
            (d1cnt,d2cnt,d3cnt,d4cnt)=(0,0,0,0)
            for each1 in qrd_ref:
                if each1!=each:
                    if d1 in each1:
                        d1cnt+=1
                    if d2 in each1:
                        d2cnt+=1
                    if d3 in each1:
                        d3cnt+=1
                    if d4 in each1:
                        d4cnt+=1
                if d1cnt>0 and d2cnt>0 and d3cnt>0 and d4cnt>0:
                    try:
                        if d1[0]==d2[0]==d3[0]==d4[0]:
                            opl.remove(qrd_val[1][d1[0]])
                        elif d1[1]==d2[1]==d3[1]==d4[1]:
                            opl.remove(qrd_val[0][d1[1]])
                    except ValueError:
                        continue
                    
        op=''.join(opl)

    #print('op',type(op))
    #op=op.strip(" ")
    #print('op strip',op)
    op=re.sub("\s", "+", op)
    #print(op)
    op1=op.replace("'+", "0+")
    op1=op1.replace("'", "'.")
    op1=op1.replace("0", "'")
    op1=op1.replace("A", "A.")
    op1=op1.replace("B", "B.")
    op1=op1.replace("C", "C.")
    op1=op1.replace("D", "D.")
    op1=op1.replace(".'", "'")
    op1=op1.replace(".+", "+")
    op1=op1.rstrip('.')
    if min_max=='min':
            print("Minimized boolean SOP expression is:",op1)
    elif min_max=='max':
            op2=op1.replace("+","]*[")
            op2=op2.replace(".","+")
            op2="["+op2+"]"
            print("Minimized boolean POS expression is:",op2)
            

print('\n')

minterms=list(map(int,input("Enter terms with in 0 to 15 : ").split())) #input

karnaughmap(minterms) #kmap function call
