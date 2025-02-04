class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Can there be negative numbers
        # Can there be multiple solutions

        l = 0
        r = len(numbers)-1

        while l<r:
            add = numbers[l] + numbers[r]

            if add>target:
                r-=1
                
            elif add<target:
                l+=1
            
            else:
                return [l+1,r+1]
            
        return []