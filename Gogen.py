import pprint as pp
import random

success=False
testruns=0

initialState = [
        ['X','-','W','-','K'],
        ['-','-','-','-','-'],
        ['M','-','F','-','N'],
        ['-','-','-','-','-'],
        ['Q','-','Y','-','P']
        ]

remainingLetters = ['A','B','C','D','E','G','H','I','J','L','O','R','S','T','U','V']

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
        'STYLE',
        'TRICK'
        ]

#GENERATE COMPLETE MATRIX
random.shuffle(remainingLetters)
rli = remainingLetters
isi = initialState

for n,i in enumerate(isi):
    for m,j in enumerate(i):
        if j == '-':
            isi[n][m] = rli.pop()
            
#LETTER PAIRS TO CHECK
tst = []
for word in wordlist:
    for i in range(len(word)-1):
        tst.append((word,word[i],word[i+1]))


while success==False and testruns<100000:
    #FIND VALUES FOR LETTERS
    lps=[]
    for n,i in enumerate(isi):
        for m,j in enumerate(i):
            lps.append((j,n,m))
    
    
    for c,d in enumerate(tst):
        j=d[1]
        k=d[2]
        for l,n,m in lps:
    
    
    
    
    
       
    #FOR X in TEST. FIND N,M for X[1] FIND N,M FOR X[2] are they within 1,1 of each other? 
    
    for c,d in enumerate(tst):
        j=d[1] # LETTER 1
        k=d[2] # LETTER 2
        
        for l,n,m in lps:
            if j==l:
                jn = n
                jm = m
            if k==l:
                kn = n
                km = m
        if abs(jn-kn)<=1 and abs(jm-km)<=1:
            tst.pop(c)
        
    
    # pp.pprint(tst)
    # pp.pprint(lps)
    # pp.pprint(isi)
    
    res = round(len(tst)/ltst,2)
    
    
   
    testruns+=1




























