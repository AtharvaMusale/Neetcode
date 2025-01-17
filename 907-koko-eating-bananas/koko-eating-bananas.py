class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [3,6,7,11] [1, 2, 2, 3]
        # HOURS = INT(PILE[I]/K) <= h if greater then increase k
        
        l, r = 1 ,  max(piles)
        res = r

        while l<=r:
            k = l + (r-l)//2
            
            total = 0
            for p in piles:
                total += math.ceil(float(p)/k)

            if total > h:
                l = k + 1
            else:
                res = k
                r = k - 1

        return res            