"""My solution to the coin flip puzzle (https://github.com/norvig/pytudes/blob/master/ipynb/Coin%20Flip.ipynb).
Explanation of data structures:
Coins: Representation of coin structure. Implemented as a string (e.g. 'HHHT')
State: Representation of belief state: A set of coins, representing possible states coins are in.
Move: A move is a set of positions to flip (e.g. {0, 1})
Position: A tuple of (State, List[Move]).
Possible Moves: """

from itertools import *
import random


def shortest_path_search():
    """BFS for coin search problem."""
    frontier = [({'HHHH', "HHHT"}, [])]
    possible_moves = [{0}, {1}, {1, 2}]
    while frontier:
        current_state = frontier.pop(0)
        current_belief, current_moves = current_state[0], current_state[1]

        if current_belief is {"HHHH"}:
            return current_moves
        else:
            for move in possible_moves:
                new_belief = {flip_coins(coins, move) for coins in current_belief}
                frontier.append((new_belief, current_moves + [move]))


def flip_coins(coins, move):
    """Applies the move to a set of coin."""
    swap = {'H': 'T', 'T': 'H'}
    if coins == "HHHH":
        return coins
    new = ''  # wow this is ugly, probably better off as a generator expression
    for i, c in enumerate(coins):
        new = new + swap[c] if i in move else new + c


#  TODO: Fix this
# def rotations(coins):
#     coins = list(coins)
#     possible_coins = set()
#     for i in range(4):
#         possible_coins |= {''.join(coins[(i + j) % 4]) for j in range(4)}
#     return possible_coins


def rotations(coins):
    """A set of all possible rotations of a coin sequence."""
    return {coins[r:] + coins[:r] for r in range(4)}


def make_move(state, move):
    for coins in state:
        return {flip_coins(c, move) for c in rotations(coins)}


def powerset(iterable):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


if __name__ == "__main__":
    print(rotations("THHH"))
