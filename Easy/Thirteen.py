# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 isRoman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together.' \
#                                                               ' 12 is written as XII, which is simply X + II. ' \
#                                                               'The number 27 is written as XXVII, which is XX + V + II.
# #
# # Roman numerals are usually written largest to smallest from left to right.
# # However, the numeral for four is not IIII. Instead, the number four is written as IV.
# # Because the one is before the five we subtract it making four. The same principle applies to the number nine,
# # which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        num_map = {'I':1, 'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
        rom_num = [char for char in s]
        rom_num.reverse()
        # print(rom_num)
        int_num = 0
        for i,x in enumerate(rom_num):
            # print(i, num_map.get(rom_num[i]), num_map.get(rom_num[i - 1]), int_num)
            if i and (num_map.get(rom_num[i]) < num_map.get(rom_num[i-1])):
                int_num = int_num - num_map.get(x)
            else:
                int_num = int_num + num_map.get(x)
        return abs(int_num)
        # print(abs(int_num))

if __name__ == "__main__":
    Solution.romanToInt(Solution, "III")
    Solution.romanToInt(Solution, "IV")
    Solution.romanToInt(Solution, "IX")
    Solution.romanToInt(Solution, "LVIII")
    Solution.romanToInt(Solution, "MCDLXXVI")