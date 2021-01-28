# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
            result = 0
            if x < 0:
                # print("False")
                return False
            else:
                result = Solution.inverse(Solution, x)
                if(result == x):
                    # print("True")
                    return True
                else:
                    # print("False")
                    return False
                # return result

    def inverse(self, x: int) -> int:
        rev = 0
        while x > 0:
            inp = x % 10
            x = x // 10
            rev = (rev * 10) + inp
        if abs(rev) < (2 ** 31 - 1):
            return rev

if __name__ == "__main__":
    Solution.isPalindrome(Solution, 121)
    Solution.isPalindrome(Solution, -121)
    Solution.isPalindrome(Solution, 10)
    Solution.isPalindrome(Solution, 101)