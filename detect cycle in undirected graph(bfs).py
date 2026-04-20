from collections import deque
class Solution:
	def isCycle(self, V, edges):
		#Code here
		#V:-total no of nodes
		adj=[]
		for _ in range(V):
		    adj.append([])
		for u,v in edges:
		    adj[u].append(v)
		    adj[v].append(u)
		vis=[0]*V
		for n in range(0,V): #Disconnected graphs
		    if(vis[n]==0):
		        vis[n]=1
		        q=deque([(n,-1)]) #node,parent
		        while(len(q)>0):
		            node,parent=q.popleft()
		            for adjNode in adj[node]:
		                if(vis[adjNode]==0):
		                    vis[adjNode]=1
		                    q.append((adjNode,node))
		                elif(vis[adjNode]==1):
		                    if(adjNode!=parent):
		                        return True
		return False
