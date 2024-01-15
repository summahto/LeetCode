class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        n = len(matches)
        
        winners = {match[0] for match in matches}
        losers = [match[1] for match in matches]

        # print(winners)
        cl = Counter(losers)
        # print(cl.keys())

        ans = []
        winNoLosses = []
        win1Loss = []

        for winner in winners:
            
            if winner not in cl.keys():
                # print(winner)
                winNoLosses.append(winner)
                # print(winNoLosses)
            
        for (key, value) in cl.items():
            if value == 1:
                win1Loss.append(key)

        ans.append(sorted(winNoLosses))
        ans.append(sorted(win1Loss))

        return ans