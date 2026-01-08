# problem link https://leetcode.com/problems/remove-element/

class Solution:
  def removeElement(self,nums,val):
    n = len(nums) 
    if n == 0:
      return 0 
    k = 0
    for i in range(n):
      if nums[i] != val:
        nums[k] = nums[i] 
        k = k + 1 
    return k
    
    
nums = [1,1,2,3,4]
val = 1 
result = Solution()
print(result.removeElement(nums,val))
