class Solution:

    def maxScore(self, arr: List[int], k: int) -> int:
        n = len(arr)
        size = n - k 
        start, curr, min_window = 0, 0, float('inf')
        
        for end, v in enumerate(arr):
            curr += v 
            if end - start + 1 > size:
            curr -= arr[start]
            start += 1  
            if end - start + 1 == size:
            min_window = min(min_window, curr)
            
        return sum(arr) - min_window

    def maxScoreSol2(self, arr: List[int], k: int) -> int:
      n = len(arr)
      size = n - k 
      curr = min_window = sum(arr[:size])
      
      for i in range(len(arr) - size):
          curr += arr[size + i] - arr[i]
          min_window = min(min_window, curr)
          
      return sum(arr) - min_window

    def maxScoreSol3(self, arr: List[int], k: int) -> int:
      p = [0 for _ in range(len(arr) + 1)]
      for i in range(1, len(arr) + 1):
        p[i] = p[i - 1] + arr[i - 1]
      
      i, j = 0, 0 
      n = len(arr)
      self.min_window = float('inf')
      while i < n and j < n: 
        size = j - i + 1
        if size == n - k:
          self.min_window = min(self.min_window,  p[j + 1] - p[i])
          if i + 1 < n:
            i += 1
          else:
            j += 1
        elif size > n - k:
          i += 1
        else:
          j += 1
          
      return p[-1] - self.min_window 

    