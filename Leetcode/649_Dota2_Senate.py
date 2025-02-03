from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        n = len(senate)
        #represent senators from the senate in r and d
        for i,s in enumerate(senate):
            if s == 'R':
                r.append(i)
            else:
                d.append(i)
        #Till any queue between r and d becomes empty
        while r and d:
            r_index = r.popleft()
            d_index = d.popleft()

            #smaller index bans the other
            if r_index < d_index:
                #r wins this round
                r.append(r_index + n)
            else:
                d.append(d_index + n)
            
        return "Radiant" if r else "Dire"

'''
TC = O(n)
SC = O(n)
'''