# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 00:36:31 2018

@author: Peter
"""

# Gogen Solver
# A gogen puzzle is a grid of interconnected letters. The objective is to put all the letters a-y in a 5x5 grid that the words can be created
#
#
#  X -  ?  -  W -  ?  -  K
#  |
#  ? -  ?  -  ? -  ?  -  ? 
#  |
#  M -  ?  -  F -  ?  -  N
#  |
#  ? -  ?  -  ? -  ?  -  ?
#  |
#  Q -  ?  -  P -  ?  -  Y
#



from collections import Counter


candidateList = []

# Candidate List is the entire set of possible locations for final letters, it starts [A-Z, 0-4 , 0-4]
for z in range(25):
    for i in range(5):
        for j in range(5):
                candidateList.append((chr(z+65),i,j))

# This is an array of the initial state as taken from the Paper
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

#This is the list of words that we need to make sure exist in the grid
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

#Bigrams are combinations of a duo of letters that need to be next to each other (B,O) (O,X)
bigrams=[list(zip(x, x[1:])) for x in wordlist]


#CandidateList2 
candidateList2 = [x for x in candidateList if (x[0] not in [y[0] for y in initialGrid]) or x in initialGrid ]

fix = Counter([x[0] for x in candidateList2])
solved = [x for x in candidateList2 if fix.get(x[0]) == 1]

#PRECALCULATE ADJACENCY VALUES
adj=[]
for wrd in bigrams:
    for bi in wrd:
      adj.append((bi[0],bi[1]))
      adj.append((bi[1],bi[0]))
adj = list(set(adj))
adjfix=Counter([x[0] for x in adj])
fiadj =  [ ( x[0], adjfix.get(x[0]) ) for x in adjfix]



for count in range(20):

    
    
    
    # IF SOMETHING IS OCCUPYING A SPACE OF A SOLVED ITEM IT IS REMOVED AS CANDIDATE
    for i in solved:
        for n,j in enumerate(candidateList2):
            if i[0] != j[0] and i[1]==j[1] and i[2]==j[2]:
                candidateList2.pop(n)
    
    fix = Counter([x[0] for x in candidateList2])
    solved = [x for x in candidateList2 if fix.get(x[0]) == 1]   
    
    
    
    #IF A LOCATION HAS ONLY 1 VALID LETTER IT IS SOLVED
    for i in range(5):
        for j in range(5):
            #IF FOR POSITION THERE IS ONLY 1 VALUE
            valid2 = [x for x in candidateList2 if x[1] == i and x[2] == j]
            #print(valid2)
            if len(valid2) == 1:
                candidateList2 = [x for x in candidateList2 if ((x[0]) not in [(y[0]) for y in valid2]) or x in valid2 ]
                
        
    fix = Counter([x[0] for x in candidateList2])
    solved = [x for x in candidateList2 if fix.get(x[0]) == 1]        
    
    
    
    #IF TWO LETTERS NEED TO BE TOGETHER TO COMPLETE A WORD AND ONE IS SOLVED, LIMIT OTHER
    for i in bigrams:
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
                    
                    candidateList2 = [x for x in candidateList2 if (x[0] not in [y[0] for y in valid]) or x in valid ]
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
                    
                    candidateList2 = [x for x in candidateList2 if (x[0] not in [y[0] for y in valid]) or x in valid ]
    
    
    fix = Counter([x[0] for x in candidateList2])
    solved = [x for x in candidateList2 if fix.get(x[0]) == 1]
    
    #print(cl2)
    
    #IF A LETTER NEEDS X OTHER LETTERS NEXT TO IT, IT CANNOT OCCUPY A SPACE WITH LESS THAN X SPARE POSITIONS

    
    for n,i in enumerate(candidateList2):
        for j in fiadj:
            if i[0] == j[0]:
                if i[1]==0 or i[1]==4 or i[2]==0 or i[2]==4:
                    if j[1] > 5:
                        candidateList2.pop(n)
                        
    fix = Counter([x[0] for x in candidateList2])
    solved = [x for x in candidateList2 if fix.get(x[0]) == 1]
    
    #FOR EACH CANDIDATE MOVE, ASSES IF PUTTING THE LETTER THERE WILL LIMIT THE ADJACENCIES TO -ve
    
    for z,i in enumerate(candidateList2):
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
                candidateList2.pop(z)
                
    fix = Counter([x[0] for x in candidateList2])
    solved = [x for x in candidateList2 if fix.get(x[0]) == 1]

    
    
  
            

            
            