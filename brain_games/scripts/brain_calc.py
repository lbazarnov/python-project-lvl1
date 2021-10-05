#!/usr/bin/env python
from brain_games.games import brain_calc_game
from brain_games.engine import start_game


def main():
    """Runs Brain Calc game"""
    start_game(brain_calc_game)


if __name__ == '__main__':
    main()
