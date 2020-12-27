# Given four lists A, B, C, D of integer values,
# compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        from collections import Counter
        sum1 = [a + b for a in A for b in B]
        sum2 = [c + d for c in C for d in D]
        map = Counter(sum2)
        result = 0
        for sum in sum1:
            result += map.get(-sum, 0)
        return result