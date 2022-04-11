"""
Problem: https://leetcode.com/problems/baseball-game/
Topics: Stack, Simulation
Difficulty: Easy
Youtube Explanation: https://www.youtube.com/watch?v=NCIE_XlV0QY
"""
class Solution:
    def calPoints(self, ops) :
        stack = []
        for op in ops:
            if op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))

        return sum(stack)