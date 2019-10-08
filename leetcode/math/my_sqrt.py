# """
# 题目：Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
#
# Example 1:
#
# Input: 4
# Output: 2
# Example 2:
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.
#
# url:https://leetcode.com/problems/sqrtx/
# """


class Solution:
    def mySqrt(self, x: int) -> int:
        small = 0
        big = x

        # 使用二分查找
        while small != big and small+1 != big:
            mid = (big + small) // 2
            if mid*mid > x:
                big = mid
            else:
                small = mid

        return small


if __name__ == '__main__':
    a = 4

    solution = Solution()
    result = solution.mySqrt(a)
    print(result)

# """
# 分析:
#
# """