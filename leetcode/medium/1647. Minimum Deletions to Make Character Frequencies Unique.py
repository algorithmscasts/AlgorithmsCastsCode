class Solution:

    def minDeletions(self, s: str) -> int:
        occ = collections.Counter(s)
        vals = sorted(occ.items(), key=lambda x: x[1])
        
        exist = set()
      
        res = 0
        for c, count in vals:
          while count in exist and count > 0: 
            count -= 1
            res += 1
          exist.add(count)
        return res