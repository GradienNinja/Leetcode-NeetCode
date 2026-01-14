# problem link https://leetcode.com/problems/contains-duplicate/

class Solution:
  def containsDuplicate(self,nums):
    n = len(nums) - 1
    for i in range(n):
      if nums[i] == nums[i+1] or nums[i] == nums[n]:
        return True 
      
    return False
result = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
print(result.containsDuplicate(nums))
