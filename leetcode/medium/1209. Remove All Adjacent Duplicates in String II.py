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