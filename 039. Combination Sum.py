class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.combinationSum_backtracking(candidates, target, 0, [], result)
        return result

    def combinationSum_backtracking(self, candidates, target, index, path, result):
        if target < 0:
            return
        if target==0:
            result.append(path)
            return
        for i in range(index, len(candidates)):
            self.combinationSum_backtracking(candidates, target-candidates[i], i, path+[candidates[i]], result)