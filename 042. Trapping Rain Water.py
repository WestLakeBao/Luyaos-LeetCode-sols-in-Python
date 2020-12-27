# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

class Solution(object):
    def trap(self, height):
        lmax, rmax = 0, 0
        left, right = 0, len(height)-1
        result = 0
        while left < right:
            if height[left] < height[right]:
                lmax = max(lmax, height[left])
                result += lmax - height[left]
                left += 1
            else:
                rmax = max(rmax, height[right])
                result += rmax - height[right]
                right -= 1
        return result

if __name__ == '__main__':
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])) # 6