'''
7. Shortest Path 
- 무기: 
    - 개념적으로 아예 이해가 안될 건 아니니까 매일 다시 풀어보면서 암기를 하자 
'''
import re
from typing import List, Optional
import collections

# - 문제
#     - (Medium) Leetcode 743. Network Delay Time: (https://leetcode.com/problems/network-delay-time/)
#     - 풀이: 최단경로찾기) bfs (or 다익스트라) 구현한다고 생각하면서 접근 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # creating a graph 
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w)) 

        # creating a queue that initialize as 0 for starting point k
        # also create an empty dict that will contain (node, distance from k) 
        Q = [(0, k)]
        dist = collections.defaultdict(int)
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        
        # if dist has same length as n, it means that every node can get signal
        # then we return max value among other values
        if len(dist) == n:
            return max(dist.values())
        
        # if not, it means that not every node got signals, so return -1
        return -1


#     - (Medium) Leetcode 787. Cheapest Flights Within K Stops: (https://leetcode.com/problems/cheapest-flights-within-k-stops/)
#     - 풀이: 최단경로찾기) 다익스트라가 안됨(TLE), 안될경우의 대안을 생각해보기
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # we will be replacing prices for every nodes
        # for init point, set to 0
        prices = [float('inf')] * n
        prices[src] = 0

        # iterate k times to update prices
        # we use tmp price to make sure that for given i stop, we don't update original price more than i stops
        for i in range(k+1):
            # we copy prices to tmp
            tmpPrices = prices.copy()

            # for s->d, we update p
            for s, d, p in flights:
                # if price for starting node is inf, we don't need to even check this node
                if prices[s] == float('inf'):
                    continue
                
                # if price is smaller, then update tmp price
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p

            # after checking all nodes, we update original price
            prices = tmpPrices

        # return -1 if final node is not updated, else return final node price 
        return -1 if prices[dst] == float('inf') else prices[dst] 
