class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        pop_map = defaultdict(int)
        logs.sort(key= lambda x: x[0])
        max_year = 0

        for log in logs:
            start = log[0]
            end = log[1]

            pop_map[start] += 1
            pop_map[end] -= 1

            max_year = max(max_year, end)
        

        # print(f"{pop_map}=")
        
        min_year = logs[0][0]
        populn = 0
        max_pop = 0
        earliest = min_year

        for year in range(min_year, max_year+1):
            populn += pop_map[year]

            if populn > max_pop:
                max_pop = populn
                earliest = year

        
        return earliest
                


        

        
