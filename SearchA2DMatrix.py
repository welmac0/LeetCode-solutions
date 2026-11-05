class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        consolidated = []
        for l in matrix:
            consolidated += l

        L = 0
        R = len(consolidated) - 1
        while L <= R:
            mid = (L + R) // 2
            if consolidated[mid] > target:
                R = mid - 1
            elif consolidated[mid] < target:
                L = mid + 1
            else:
                return True

        return False
