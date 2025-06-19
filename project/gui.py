"""Tkinter GUI for the guessing game."""

import tkinter as tk
from tkinter import ttk

from core import Game, Leaderboard, generate_nickname

ACCENT = "#4CAF50"
FONT = ("Courier New", 14)

leaderboard = Leaderboard()
name = generate_nickname()

game = Game()


def update_tables():
    """Refresh the leaderboard tables."""
    for tree, data in ((tree_best, leaderboard.top_best()), (tree_worst, leaderboard.top_worst())):
        tree.delete(*tree.get_children())
        for idx, rec in enumerate(data, 1):
            dt_str = rec.dt.strftime("%Y-%m-%d %H:%M:%S")
            tree.insert("", "end", values=(idx, rec.name, rec.attempts, dt_str))
        for idx in range(len(data) + 1, 11):
            tree.insert("", "end", values=(idx, "—", "—", "—"))


def check_number() -> None:
    """Handle number checking."""
    value = entry.get()
    if not value.isdigit():
        label_status.config(text="Пожалуйста, введите число")
        return
    guess = int(value)
    if game.guess(guess):
        msg = f"Верно! Число попыток — {game.attempts}"
        leaderboard.add_record(name, game.attempts)
        game.reset()
        entry.delete(0, tk.END)
        update_tables()
    else:
        msg = "Неверно"
    label_status.config(text=msg)


root = tk.Tk()
root.title("Угадай число")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="white")

# Left frame: input and button
frame_left = tk.Frame(root, bg="white")
frame_left.pack(side=tk.LEFT, padx=10, pady=10)

entry = tk.Entry(frame_left, font=FONT)
entry.pack(pady=5)

btn = tk.Button(frame_left, text="Проверить", command=check_number, bg=ACCENT, fg="white", font=FONT)
btn.pack(pady=5, fill=tk.X)

label_status = tk.Label(frame_left, text="", bg="white", fg="black", font=FONT)
label_status.pack(pady=5)

# Right frame: leaderboards
frame_right = tk.Frame(root, bg="white")
frame_right.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

columns = ("#", "Имя", "Попытки", "Дата/время")

label_best = tk.Label(frame_right, text="Top-10 лучших", bg="white", fg=ACCENT, font=FONT)
label_best.pack()

tree_best = ttk.Treeview(frame_right, columns=columns, show="headings", height=5)
for col in columns:
    tree_best.heading(col, text=col)
    tree_best.column(col, width=90, anchor=tk.CENTER)
tree_best.pack(pady=5)

label_worst = tk.Label(frame_right, text="Top-10 худших", bg="white", fg=ACCENT, font=FONT)
label_worst.pack()

tree_worst = ttk.Treeview(frame_right, columns=columns, show="headings", height=5)
for col in columns:
    tree_worst.heading(col, text=col)
    tree_worst.column(col, width=90, anchor=tk.CENTER)
tree_worst.pack(pady=5)

update_tables()

root.mainloop()
