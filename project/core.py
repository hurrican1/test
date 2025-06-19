"""Core game logic and leaderboard handling."""

from dataclasses import dataclass
from datetime import datetime
import random
from typing import List, Dict


def generate_nickname() -> str:
    """Generate a random player nickname."""
    digits = ''.join(random.choices('0123456789', k=2))
    return f"Player-{digits}"


@dataclass
class Record:
    """Player result record."""

    name: str
    attempts: int
    dt: datetime


class Leaderboard:
    """Leaderboard storing results in memory."""

    def __init__(self) -> None:
        self.records: List[Record] = []

    def add_record(self, name: str, attempts: int) -> None:
        """Add a new result to the leaderboard."""
        self.records.append(Record(name, attempts, datetime.now()))

    def top_best(self, n: int = 10) -> List[Record]:
        """Return top results with fewest attempts."""
        return sorted(self.records, key=lambda r: r.attempts)[:n]

    def top_worst(self, n: int = 10) -> List[Record]:
        """Return worst results with most attempts."""
        return sorted(self.records, key=lambda r: r.attempts, reverse=True)[:n]


class Game:
    """Number guessing game."""

    def __init__(self) -> None:
        self.secret = 0
        self.attempts = 0
        self.reset()

    def reset(self) -> None:
        """Start a new game by generating a new secret number."""
        self.secret = random.randint(0, 100)
        self.attempts = 0

    def guess(self, number: int) -> bool:
        """Check the guessed number.

        Returns True if guessed correctly, otherwise False.
        """
        self.attempts += 1
        return number == self.secret
