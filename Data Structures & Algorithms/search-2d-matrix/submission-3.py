class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first search first column to determine which row
        # second search for specific row

        rows, columns = len(matrix), len(matrix[0])
        
        def search_rows(front, end):
            medium = (front+end) // 2 + 1 if (front+end) % 2 == 1 else (front+end) // 2
            if front == end:
                return front
            elif target >= matrix[medium][0]:
                return search_rows(medium, end)
            elif target < matrix[medium][0]:
                return search_rows(front, medium-1)

        def search_columns(front, end, row):
            medium = (front+end) // 2 + 1 if (front+end) % 2 == 1 else (front+end) // 2
            if target == matrix[row][medium]:
                return True
            elif front == end and matrix[row][front] != target:
                return False
            elif target > matrix[row][medium]:
                return search_columns(medium, end, row)
            elif target < matrix[row][medium]:
                return search_columns(front, medium-1, row)
        
        row = search_rows(0, rows-1)
        return search_columns(0, columns-1, row)
      

            
