class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        row = -1
        if(rows == 1 and cols == 1):
            if(target == matrix[0][0]): return True
            else: return False

        if(rows == 1):
            for i in range(cols):
                if(target == matrix[0][i]): return True
            return False
        elif(cols == 1):
            for i in range(rows):
                if(target == matrix[i][0]): return True
            return False
        else:
            for i in range(rows):
                if(target < matrix[i][0]):
                    row = i-1
                    break
                else:
                    row = i

                if(target == matrix[i][0]): return True
                    
            for i in range(cols):
                if(matrix[row][i] == target):
                    return True
       
        return False