class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i, val in enumerate(nums):
            if i>0 and val == nums[i-1]:
                continue
            
            l, r  = i+1, len(nums) - 1
            while l<r:
                threesum = val + nums[l] + nums[r]
                if threesum > 0:
                    r-=1
                
                elif threesum < 0:
                    l+=1
                
                else:
                    res.append([val,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                
        return res



































        # res = []
        # nums.sort()
        
        # for i,j in enumerate(nums):
        #     if j>0:
        #         break

        #     if i>0 and j == nums[i-1]:
        #         continue
            
        #     l,r = i+1, len(nums)-1
        #     while l<r:
        #         threeSum = j + nums[l] + nums[r]
        #         if threeSum>0:
        #             r-=1
        #         elif threeSum<0:
        #             l+=1
                
        #         else:
        #             res.append([j,nums[l],nums[r]])
        #             l+=1
        #             r-=1
        #             while nums[l] == nums[l-1] and l<r:
        #                 l+=1
        # return res

