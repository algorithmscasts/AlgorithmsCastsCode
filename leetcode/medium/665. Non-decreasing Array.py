
class Solution:

    def checkPossibilitySol2(self, nums: List[int]) -> bool:
        cnt, n = 0, len(nums)
        for i in range(1, n):
          if nums[i - 1] > nums[i]:
            cnt += 1
            if i - 2 >= 0 and nums[i - 2] > nums[i]:
              nums[i] = nums[i - 1]
            else:
              nums[i - 1] = nums[i]
              
          if cnt > 1:
            return False
            
        return cnt <= 1

    def checkPossibilitySol2(self, nums: List[int]) -> bool:
        mx, mn = float('-inf'), float('inf')
        left, right = 0, 0
        n = len(nums)
        for i in range(n):
          if nums[i] < mx:
            left += 1  
          mx = max(mx, nums[i])
          
        for i in range(n - 1, -1, -1):
          if nums[i] > mn:
            right += 1  
          mn = min(mn, nums[i])
        
        return left <= 1 or right <= 1
      
