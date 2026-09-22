class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix), len(matrix[0])
        l,r = 0, n-1
        while l<=r:
            mid = (l+r)//2
            if target>=matrix[mid][0] and target<=matrix[mid][m-1]:
                break
            elif target<matrix[mid][0]:
                r = mid-1
            else:
                l = mid+1

        row = (l+r)//2
        a,b = 0, m-1
        while a<=b:
            mid = (a+b)//2
            if matrix[row][mid] == target:
                return True
            elif target<matrix[row][mid]:
                b = mid-1
            else:
                a = mid+1
        return False