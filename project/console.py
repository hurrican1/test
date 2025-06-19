"""Console interface for the guessing game."""

from core import Game, Leaderboard, generate_nickname

leaderboard = Leaderboard()
name = generate_nickname()
print(f"Ваш псевдоним: {name}")

game = Game()

while True:
    user_input = input("Введите число от 0 до 100: ")
    if not user_input.isdigit():
        print("Пожалуйста, введите число")
        continue
    guess = int(user_input)
    if game.guess(guess):
        print("Верно!")
        leaderboard.add_record(name, game.attempts)
        break
    else:
        print("Неверно, попробуйте ещё раз")


def print_table(title: str, records: list) -> None:
    """Print leaderboard table."""
    print("\n" + title)
    for i in range(10):
        if i < len(records):
            r = records[i]
            dt_str = r.dt.strftime("%Y-%m-%d %H:%M:%S")
            print(f"{i + 1:>2}. {r.name} - {r.attempts} попыток - {dt_str}")
        else:
            print(f"{i + 1:>2}. —")


print_table("Top-10 лучших", leaderboard.top_best())
print_table("Top-10 худших", leaderboard.top_worst())
