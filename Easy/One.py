# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: [int], target: int):
        checkTarget = {}
        for ind, num in enumerate(nums):
            if checkTarget.get(target - num) is None:
                checkTarget.update({num: ind})
            else:
                return(checkTarget.get(target - num), ind)


if __name__ == "__main__":
    Solution.twoSum(Solution, [2,4,5,8], 6)
