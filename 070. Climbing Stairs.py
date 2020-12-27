# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        steps = [0 for _ in range(n)]
        steps[0] = 1
        steps[1] = 2
        for i in range(2, n):
            steps[i] = steps[i-1] + steps[i-2]
        return steps[-1]

if __name__ == '__main__':
    print(Solution().climbStairs(3))