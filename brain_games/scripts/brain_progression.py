#!/usr/bin/env python
from brain_games.games import brain_progression_game
from brain_games.engine import start_game


def main():
    """Runs Brain GCD game"""
    start_game(brain_progression_game)


if __name__ == '__main__':
    main()
