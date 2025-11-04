class NQueens:
    def __init__(self, size):
        self.size = size
        self.board = [0] * size
        self.count = 0
        
        self.cols = set()
        self.pos_diag = set()
        self.neg_diag = set()

    def print_board(self):
        for row in range(self.size):
            line = ""
            queen_col = self.board[row]
            for col in range(self.size):
                if col == queen_col:
                    line += "Q "
                else:
                    line += "X "
            print(line)
        print() 

    def is_safe(self, row, col):
        if col in self.cols:
            return False
        if (row + col) in self.pos_diag:
            return False
        if (row - col) in self.neg_diag:
            return False
        
        return True

    def solve(self, row):
        if row == self.size:
            self.count += 1
            self.print_board()
            return

        for col in range(self.size):
            if self.is_safe(row, col):
                
                self.board[row] = col
                self.cols.add(col)
                self.pos_diag.add(row + col)
                self.neg_diag.add(row - col)
                
                self.solve(row + 1)
                
                self.cols.remove(col)
                self.pos_diag.remove(row + col)
                self.neg_diag.remove(row - col)

try:
    size = int(input("Enter size of chessboard: "))
    if size <= 0:
        print("Size must be a positive integer.")
    else:
        solver = NQueens(size)
        solver.solve(0)
        print(f"Found {solver.count} total solutions for a {size}x{size} board.")

except ValueError:
    print("Invalid input. Please enter a number.")