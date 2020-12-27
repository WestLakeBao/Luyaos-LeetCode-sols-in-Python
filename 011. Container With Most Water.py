# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Example
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

# time: O(N)
# space: O(1)

class Solution(object):
    def maxArea(self, height):
        maxArea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            pivot = min(height[left], height[right])
            maxArea = max(maxArea, (right - left) * pivot)

            while height[left] <= pivot and left < right:
                left += 1
            while height[right] <= pivot and left < right:
                right -= 1

        return maxArea

if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])) # 49