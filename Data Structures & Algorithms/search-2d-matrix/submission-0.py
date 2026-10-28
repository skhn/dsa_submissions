class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            m = (l+r)//2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] < target:
               isFound = self.searchSelected(matrix[m], target)
               if isFound:
                    return True;
               else:
                    l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
        return False


    def searchSelected(self, matrix, target):
        l = 0
        r = len(matrix) - 1

        while l <= r:
            m = (l+r)//2
            if matrix[m] == target:
                return True
            elif matrix[m] < target:
                l = m + 1
            elif matrix[m] > target:
                r = m - 1
        return False


            
        