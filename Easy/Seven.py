# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x < 0:
            result = Solution.inverse(Solution, abs(x))
            # print(result * -1)
            return result * -1
        else:
            result = Solution.inverse(Solution, x)
            # print(result)
            return result

    def inverse(self, x: int) -> int:
        rev = 0
        while x > 0:
            inp = x % 10
            x = x // 10
            rev = (rev * 10) + inp

        if abs(rev) < (2 ** 31 - 1):
            return rev
        else:
            return 0


if __name__ == "__main__":
    Solution.reverse(Solution, 123)
    Solution.reverse(Solution, -123)
    Solution.reverse(Solution, 120)
    Solution.reverse(Solution, 0)