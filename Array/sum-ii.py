# problem link https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
  def twoSum(self,numbers,target):
    n = len(numbers) 
    left = 0 
    right = len(numbers) - 1 
    while left < right:
      if n <= 0:
        break 
      add = numbers[left] + numbers[right]
      if add == target:
        return [left + 1,right + 1]
      if add < target:
        left += 1
      else:
        right -= 1
    return -1 

numbers = [1,2,3,4]
target = 3 
result = Solution()
print(result.twoSum(numbers,target))
