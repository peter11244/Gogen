# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 00:36:31 2018

@author: Peter
"""


from collections import Counter
import pprint as pp
import random

candidateList = []

for z in range(25):
    for i in range(5):
        for j in range(5):
                candidateList.append((chr(z+65),i,j))

initialGrid=[
        ('X',0,0),
        ('W',2,0),
        ('K',4,0),
        ('M',0,2),
        ('F',2,2),
        ('N',4,2),
        ('Q',0,4),
        ('P',4,4),
        ('Y',2,4)
        ]

wordlist= [
        'BOW',
        'BOX',
        'DOLE',
        'FLOAT',
        'HALVE',
        'JUT',
        'LAMB',
        'NECK',
        'QUALITY',
        'SPRING',
        'STILE',
        'TRICK'
        ]

bigr=[list(zip(x, x[1:])) for x in wordlist]


#RULE OUT INITIAL POSITIONS
cl2 = [x for x in candidateList if (x[0] not in [y[0] for y in initialGrid]) or x in initialGrid ]

fix = Counter([x[0] for x in cl2])
solved = [x for x in cl2 if fix.get(x[0]) == 1]

#PRECALCULATE ADJACENCY VALUES
adj=[]
for wrd in bigr:
    for bi in wrd:
      adj.append((bi[0],bi[1]))
      adj.append((bi[1],bi[0]))
adj = list(set(adj))
adjfix=Counter([x[0] for x in adj])
fiadj =  [ ( x[0], adjfix.get(x[0]) ) for x in adjfix]


magiccandidate=[]
giveupflag=0
statehist=[candidateList,]
solvedhist=[[],]
giveupcount=0

for count in range(1000):
    lensolved=len(solved)
    
    solvedcount=0
    
    
    
    # IF SOMETHING IS OCCUPYING A SPACE OF A SOLVED ITEM IT IS REMOVED AS CANDIDATE
    for i in solved:
        for n,j in enumerate(cl2):
            if i[0] != j[0] and i[1]==j[1] and i[2]==j[2]:
                cl2.pop(n)
    
    fix = Counter([x[0] for x in cl2])
    solved = [x for x in cl2 if fix.get(x[0]) == 1]   
    
    
    
    #IF A LOCATION HAS ONLY 1 VALID LETTER IT IS SOLVED
    for i in range(5):
        for j in range(5):
            #IF FOR POSITION THERE IS ONLY 1 VALUE
            valid2 = [x for x in cl2 if x[1] == i and x[2] == j]
            #print(valid2)
            if len(valid2) == 1:
                cl2 = [x for x in cl2 if ((x[0]) not in [(y[0]) for y in valid2]) or x in valid2 ]
                
        
    fix = Counter([x[0] for x in cl2])
    solved = [x for x in cl2 if fix.get(x[0]) == 1]        
    
    
    
    #IF TWO LETTERS NEED TO BE TOGETHER TO COMPLETE A WORD AND ONE IS SOLVED, LIMIT OTHER
    for i in bigr:
        for j in i:
            for z,n,m in [(x[0],x[1],x[2]) for x in solved]:
                if j[0] == z:
                    valid=[]
                    
                    u=j[1]
                    valid.append((u,n-1,m-1))
                    valid.append((u,n-1,m))
                    valid.append((u,n,m-1))
                    valid.append((u,n+1,m))
                    valid.append((u,n,m+1))
                    valid.append((u,n+1,m+1))
                    valid.append((u,n-1,m+1))
                    valid.append((u,n+1,m-1))
                    
                    cl2 = [x for x in cl2 if (x[0] not in [y[0] for y in valid]) or x in valid ]
                if j[1] == z:
                    valid=[]
                   
                    u=j[0]
                    valid.append((u,n-1,m-1))
                    valid.append((u,n-1,m))
                    valid.append((u,n,m-1))
                    valid.append((u,n+1,m))
                    valid.append((u,n,m+1))
                    valid.append((u,n+1,m+1))
                    valid.append((u,n-1,m+1))
                    valid.append((u,n+1,m-1))
                    
                    cl2 = [x for x in cl2 if (x[0] not in [y[0] for y in valid]) or x in valid ]
    
    
    fix = Counter([x[0] for x in cl2])
    solved = [x for x in cl2 if fix.get(x[0]) == 1]
    
    #print(cl2)
    
    #IF A LETTER NEEDS X OTHER LETTERS NEXT TO IT, IT CANNOT OCCUPY A SPACE WITH LESS THAN X SPARE POSITIONS

    
    for n,i in enumerate(cl2):
        for j in fiadj:
            if i[0] == j[0]:
                if i[1]==0 or i[1]==4 or i[2]==0 or i[2]==4:
                    if j[1] > 5:
                        cl2.pop(n)
                        
    fix = Counter([x[0] for x in cl2])
    solved = [x for x in cl2 if fix.get(x[0]) == 1]
    
    #FOR EACH CANDIDATE MOVE, ASSES IF PUTTING THE LETTER THERE WILL LIMIT THE ADJACENCIES TO -ve
    
    for z,i in enumerate(cl2):
        if i[1] == 0 or i[2]== 0 or i[1]==4 or i[2]==4:
            #WORK OUT HOW MANY FREE SPACES ARE LEFT
            
            tstmtx = []
            
            n = i[1] 
            m = i[2]
            
            tstmtx.append((n-1,m-1))
            tstmtx.append((n-1,m))
            tstmtx.append((n,m-1))
            tstmtx.append((n+1,m))
            tstmtx.append((n,m+1))
            tstmtx.append((n+1,m+1))
            tstmtx.append((n-1,m+1))
            tstmtx.append((n+1,m-1))
            
            tstmtx2 = [x for x in solved if (x[1],x[2]) in tstmtx]
            
            freespace=5-len(tstmtx2)
            
            #WORK OUT HOW MANY LETTER STILL NEED TO BE SOLVED NEXT TO THE CANDIDATE
            stillleft=[x for x in adj if x[0]<x[1] and (
                       
                                   (i[0]==x[0] and x[1] not in [y[0] for y in solved]) 
                                or (i[0]==x[1] and x[0] not in [y[0] for y in solved]))]
        
        
            if freespace<len(stillleft):
                cl2.pop(z)
                
    fix = Counter([x[0] for x in cl2])
    solved = [x for x in cl2 if fix.get(x[0]) == 1]

    
    
    
    solvedcount = len(solved) - lensolved

    if solvedcount == 0 :
        giveupcount  += 1
        if len(cl2) == 25:
            print('success')
            break
            
    else:
        giveupcount = 0
    
    
    
    
    #Sometimes Computers just have to guess....
    
    if giveupcount > 3:
        if giveupflag == 0:
            #Save State. Pick Random Candidate. 
            giveupflag = 1
            giveupcount = 0
            
            
            
            cl3 = [x for x in cl2 if x[0] not in [y[0] for y in solved]]
            
            if len(cl3) == 0:
                cl2=[x for x in statehist.pop() if x != magiccandidate]
                solved = solvedhist.pop()
                cl3 = [x for x in cl2 if x[0] not in [y[0] for y in solved]]
            
            
            random.shuffle(cl3)
            statehist.append(cl2)
            solvedhist.append(solved)
            magiccandidate = cl3[0]
            solved.append(magiccandidate)
            print(magiccandidate)
            
                
        
        
        else:
            giveupflag = 0
            giveupcount = 0
            
            cl2=[x for x in statehist.pop() if x != magiccandidate]
            solved = solvedhist.pop()
            
            
            
            #RevertState, Destroy Random Candidate.
            
            
            