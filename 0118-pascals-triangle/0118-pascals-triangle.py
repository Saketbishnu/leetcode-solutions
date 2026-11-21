class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1]]
        
        for i in range(1, numRows):
            prev_row = triangle[i - 1]
            # Start and end are always 1
            current_row = [1] * (i + 1)
            
            # Fill the inner elements
            for j in range(1, i):
                current_row[j] = prev_row[j - 1] + prev_row[j]
                
            triangle.append(current_row)
            
        return triangle
