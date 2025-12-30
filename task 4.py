import tkinter as tk
from tkinter import messagebox

PUZZLE = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def is_valid(board, r, c, n):
    for i in range(9):
        if board[r][i] == n or board[i][c] == n:
            return False

    br, bc = (r // 3) * 3, (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[br + i][bc + j] == n:
                return False
    return True

def solve(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                for n in range(1, 10):
                    if is_valid(board, r, c, n):
                        board[r][c] = n
                        if solve(board):
                            return True
                        board[r][c] = 0
                return False
    return True

def get_board():
    board = []
    for r in range(9):
        row = []
        for c in range(9):
            v = cells[r][c].get()
            row.append(int(v) if v else 0)
        board.append(row)
    return board

def solve_game():
    board = get_board()
    if solve(board):
        for r in range(9):
            for c in range(9):
                cells[r][c].delete(0, tk.END)
                cells[r][c].insert(0, board[r][c])
    else:
        messagebox.showerror("Error", "No solution exists")

root = tk.Tk()
root.title("Sudoku Game")
root.geometry("460x560")
root.resizable(False, False)

tk.Label(root, text="Sudoku", font=("Arial", 20, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

cells = []

for r in range(9):
    row_cells = []
    for c in range(9):
        e = tk.Entry(
            frame,
            width=3,
            font=("Arial", 14, "bold"),
            justify="center",
            relief="solid",
            bd=1
        )
        e.grid(
            row=r,
            column=c,
            padx=(4 if c % 3 == 0 else 1),
            pady=(4 if r % 3 == 0 else 1)
        )

        if PUZZLE[r][c] != 0:
            e.insert(0, PUZZLE[r][c])
            e.config(state="disabled", disabledforeground="black")
        row_cells.append(e)
    cells.append(row_cells)

tk.Button(
    root,
    text="Solve Puzzle",
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
    width=18,
    command=solve_game
).pack(pady=20)

root.mainloop()
