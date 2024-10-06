from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        # keep a track of number of stops remaining
        # Do not store global optimum paths for each node rather, put all of them in the heap. 
        # because there could be a route which is cheaper but takes more number of stops
        # if we store this global optimum, then we will ignore other paths which are within k stops 
        # and is one of the correct answers.

        # adj = defaultdict(list)

        # for u, v, w in flights:
        #     adj[u].append((v, w))
        
        # pq = []
        # pq.append((0, src, k+1))

        # while pq:

        #     (cd, cn, k) = heapq.heappop(pq)
            
        #     # tremendous, check your notes for why this is brilliant
        #     if cn == dst:
        #         return cd
            
        #     if k > 0:
        #         for (v, w) in adj[cn]:
        #             dv = cd + w

        #             # send all the paths into the q as long as we have stops left
        #             heapq.heappush(pq, (dv, v, k-1))


        # return -1

        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        
        # Best prices for each node and remaining stops
        best = {}
        
        pq = [(0, src, k + 1)]
        
        while pq:
            price, node, stops = heapq.heappop(pq)
            
            # If we've reached the destination, return the price
            if node == dst:
                return price
            
            if stops > 0:
                for neighbor, weight in adj[node]:
                    new_price = price + weight
                    
                    # Only consider this path if it's better than what we've seen before
                    if (neighbor, stops - 1) not in best or new_price < best[(neighbor, stops - 1)]:
                        best[(neighbor, stops - 1)] = new_price
                        heapq.heappush(pq, (new_price, neighbor, stops - 1))
        
        return -1