class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros= 0
        ones = 0
        l = 0
        ans = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros+=1
            else:
                ones+=1
            
            while zeros > k:
                if nums[l] == 1:
                    ones-=1
                else:
                    zeros-=1
                
                l+=1
            
            ans = max(ans, r - l +1)
        return ans