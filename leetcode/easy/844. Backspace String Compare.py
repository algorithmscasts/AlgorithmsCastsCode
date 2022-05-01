"""
Problem: https://leetcode.com/problems/backspace-string-compare/
Topics: Two pointers, Stack, String, Simulation
Difficulty: Easy
Youtube Explanation: https://www.youtube.com/watch?v=kXVDXmICRa0
"""
class Solution:
    # recursive solution going backwards to apply backspace
    def backspaceCompare(self, s, t):
        def apply(s, i, skip=0):
            if i < 0:
                return ""
            if s[i] != "#":
                if skip > 0:
                    return apply(s, i - 1, skip - 1)
                else:
                    return apply(s, i - 1) + s[i]
            else:
                return apply(s, i - 1, skip + 1)

        return apply(s, len(s) - 1) == apply(t, len(t) - 1)

    def backspaceCompareSol2(self, s, t):
        # using stack
        def apply(s):
            st = []
            for c in s:
                if c == "#":
                    if st:
                        st.pop()
                else:
                    st.append(c)
            return "".join(st)

        return apply(s) == apply(t)

    # solution using reduce, using stack, traversing from front to apply backspace
    def backspaceCompareSol3(self, S, T):
        # reduce function gets passed, reduced res so far and current element we're looking at in the iterable
        def apply(res, c):
            if c == "#":
                if res:
                    res.pop()
            else:
                res.append(c)
            return res

        return reduce(apply, s, []) == reduce(apply, t, [])