"""
Problem: https://leetcode.com/problems/max-number-of-k-sum-pairs/
Topics: Two pointers, Hashtable, Sorting, Array
Difficulty: Medium
Youtube Explanation: https://www.youtube.com/watch?v=kp8hdby56PQ
"""
import collections

class Solution:
    def maxOperations(self, nums, k):
        occ = collections.defaultdict(int)
        count = 0
        for num in nums:
            if occ[k - num] > 0:
                occ[k - num] -= 1
                count += 1
            else:
                occ[num] += 1
        return count

    def maxOperationsSol2(self, nums, k):
        occ = collections.Counter(nums)
        count = 0
        for x in occ:
            count += min(occ[x], occ[k - x])
        return count // 2

    def maxOperationsSol3(self, nums, k):
        nums.sort()
        s, e = 0, len(nums) - 1
        count = 0
        while s < e:
            if nums[s] + nums[e] == k:
                count += 1
                s += 1
                e -= 1
            elif nums[s] + nums[e] > k:
                e -= 1
            else:
                s += 1
        return count

    def maxOperationsSol4(self, nums, k):
        nums.sort()
        s, e = 0, len(nums) - 1
        count = 0
        while s < e and nums[s] < k:
            if nums[s] + nums[e] == k:
                count += 1
                s += 1
                e -= 1
            elif nums[s] + nums[e] > k:
                e -= 1
            else:
                s += 1
        return count