class Solution:
    def largestGoodInteger(self, num):
        n = len(num)
        res = ""
        for i in range(n - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                res = max(res, num[i:i + 3])
        return res

    def largestGoodIntegerSol2(self, num):
        n = len(num)
        res = ""
        for i in range(n - 2):
            sub = num[i:i + 3]
            if len(set(sub)) == 1:
                res = max(res, sub)

        return res

    def largestGoodIntegerSol3(self, num):
        for d in range(9, -1, -1):
            sub = str(d) * 3
            if sub in num:
                return sub
        return ""
