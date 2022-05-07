"""
Problem: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
Topics: Stack, String
Difficulty: Medium
Youtube Explanation: https://www.youtube.com/watch?v=t19uzr2N21U
"""
class Solution:
    def removeDuplicates(self, s, k):
        stk = []

        for c in s:
            if stk and stk[-1][0] == c:
                stk[-1] = (stk[-1][0], stk[-1][1] + 1)
                if stk[-1][1] == k:
                    stk.pop()
            else:
                stk.append((c, 1))

        res = ""
        while stk:
            c, count = stk.pop()
            res = c * count + res
        return res

    def removeDuplicatesSol2(self, s, k):
        stk = [('$', 0)]

        for c in s:
            if stk[-1][0] == c:
                stk[-1][1] += 1
            else:
                stk.append([c, 1])
            if stk[-1][1] == k:
                stk.pop()

        return "".join(c * count for c, count in stk)