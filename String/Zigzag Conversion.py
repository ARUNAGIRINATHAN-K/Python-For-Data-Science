class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # Create an array of strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char
            # Flip direction when you reach the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        # Combine rows
        return ''.join(rows)
