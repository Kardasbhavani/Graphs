#codestudio360
from typing import List  #by using this if we get a error that ('list' is not defined) then we can use this line
from collections import deque
def getAlienLanguage(dictionary, k) :
    adj=[]
    for _ in range(k):
        adj.append([])
    #step1:-find edges
    #k:-no of characters
    n=len(dictionary)
    #n:-total words
    inDegre=[0]*k
    for ind in range(0,n-1):
        w1=dictionary[ind] #w1=word1
        w2=dictionary[ind+1] #w2=word2
        for i in range(0,min(len(w1),len(w2))): 
            #e.g:-w1[i]=b,w2[i]=a
            if(w1[i]!=w2[i]):
                inDegre[ord(w2[i])-ord('a')]+=1 #calculate inDegre
                adj[ord(w1[i])-ord('a')].append(ord(w2[i])-ord('a'))
                break
    q=deque([])
    for i in range(0,k):
        if(inDegre[i]==0):
            q.append(i)
    ans=[]
    while(len(q)>0):
        node=q.popleft()
        ans.append(node)
        for adjNode in adj[node]:
            inDegre[adjNode]-=1
            if(inDegre[adjNode]==0):
                q.append(adjNode)
    result=[]
    for num in ans:
        result.append(chr(ord('a')+num))
    return result
