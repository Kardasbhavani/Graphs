class Solution:
	def isCycle(self, V, edges):
		#Code here
		#V:-total no of nodes
		def dfs(node,parent):
            vis[node]=1
            for adjNode in adj[node]:
                if(vis[adjNode]==0):
                    if(dfs(adjNode,node)):
                        return True
                elif(vis[adjNode]==1):
                    if(adjNode!=parent):
                        return True
            return False
        adj=[]
        for _ in range(V):
            adj.append([])
        for u,v in edges:
            adj[v].append(u)
            adj[u].append(v)
        vis=[0]*V
        for n in range(0,V):
            if(vis[n]==0):
                if(dfs(n,-1)):
                    return True
        return False

