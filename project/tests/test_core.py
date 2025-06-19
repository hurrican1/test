from project.core import generate_nickname, Game, Leaderboard
import re


def test_generate_nickname():
    name = generate_nickname()
    assert re.match(r"Player-\d{2}", name)


def test_game_guess_and_reset():
    game = Game()
    secret = game.secret
    assert not game.guess(secret - 1)
    assert game.attempts == 1
    assert game.guess(secret)
    assert game.attempts == 2
    game.reset()
    assert game.attempts == 0


def test_leaderboard_sorting():
    lb = Leaderboard()
    lb.add_record("A", 5)
    lb.add_record("B", 2)
    lb.add_record("C", 7)
    best = lb.top_best()
    worst = lb.top_worst()
    assert best[0].name == "B"
    assert worst[0].name == "C"
