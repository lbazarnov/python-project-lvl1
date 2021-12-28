#!/usr/bin/env python
from brain_games.games import brain_even
from brain_games.engine import start_game


def main():
    """Runs Brain Even game"""
    start_game(brain_even)


if __name__ == '__main__':
    main()
