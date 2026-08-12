class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adjMap = defaultdict(list)
        for i,equ in enumerate(equations):
            a,b = equ[0], equ[1]
            adjMap[a].append((values[i],b))
            adjMap[b].append((1/values[i],a))
        # print(adjMap)


        def dfs(node, target, cur):
            # print(vis)
            if node not in adjMap or target not in adjMap:
                return -1
            if node in vis:
                return -1
            if node==target:
                return cur
            vis.add(node)
            for weight, adj in adjMap[node]:
                nei = dfs(adj, target,weight*cur)
                if nei!=-1:
                    return nei
            return -1
        
        ans= []
        for q in queries:
            vis = set()
            ans.append(dfs(q[0],q[1],1))

        return ans
        