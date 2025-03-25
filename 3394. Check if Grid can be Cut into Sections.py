class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        xRange, yRange = [], []
        for x1,y1,x2,y2 in rectangles:
            xRange.append([x1,x2])
            yRange.append([y1,y2])
        
        def tryCut(arr):
            arr.sort()
            i=1
            while i<len(arr):
                if arr[i-1][1] > arr[i][0]:
                    if arr[i-1][1] > arr[i][1]:
                        arr[i] = [arr[i-1][0], arr[i-1][1]]
                    else:
                        arr[i] = [arr[i-1][0], arr[i][1]]

                    del arr[i-1]
                else:
                    i += 1

            return True if len(arr) >= 3 else False

        return tryCut(xRange) or tryCut(yRange)
