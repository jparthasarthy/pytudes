"""My solution to the coin flip puzzle (https://github.com/norvig/pytudes/blob/master/ipynb/Coin%20Flip.ipynb).
Explanation of data structures:
Coins: Representation of coin structure. Implemented as a string (e.g. 'HHHT')
State: Representation of belief state: A set of coins, representing possible states coins are in.
Move: A move is a set of positions to flip (e.g. {0, 1})
Position: A tuple of (State, List[Move]).
Possible Moves: list

Discussion of problem:

My solution was very similar to Norvig's because he followed a design pattern prevalent in CS212, a Udacity
course he taught that I took. However, I made some mistakes in the design of my BFS.
1. Chose data structure set instead of frozenset to represent belief state. I didn't realize that
elements of a python set needed to be hashable.
2. Misdesigned my all_moves() and all_coins(), suprisingly.
3. Did NOT implement an explored set in my BFS, which lead my search not to terminate.
4. Frozenset constructor requires an iterable, so frozenset("HHHH") == frozenset({H}). This caused my BFS
to not terminate.
Time taken: 4-5 hrs?
"""

from itertools import *


def shortest_path_search():
    """BFS for coin search problem."""
    frontier = [(frozenset(all_coins()), [])]
    possible_moves = [set(m) for m in powerset(range(4))]
    possible_moves.remove(set())
    explored = set()
    while frontier:
        current_state = frontier.pop(0)
        current_belief, current_moves = current_state[0], current_state[1]
        if current_belief == frozenset({"HHHH"}):
            return current_moves
        else:
            for move in possible_moves:
                new_belief = frozenset(state for coins in current_belief for state in make_move(coins, move))
                if new_belief not in explored:
                    frontier.append((new_belief, current_moves + [move]))
                    explored.add(new_belief)


def flip_coins(coins, move):
    swap = {'H': 'T', 'T': 'H'}
    if coins == "HHHH":
        return coins
    # new = ''
    # for i, c in enumerate(coins):
    #     new = new + swap[c] if i in move else new + c
    return ''.join([swap[c] if i in move else c for i, c in enumerate(coins)])


def rotations(coins):
    # new = []
    # for i in range(4):  # offset counter
    #     new_string = ''
    #     for j in range(4):  # iterate through characters
    #         new_string += coins[(i + j) % 4]
    #     new.append(new_string)
    # return new
    return frozenset(''.join([coins[(i + j) % 4] for j in range(4)]) for i in range(4))


def make_move(coins, move):
    return frozenset(flip_coins(c, move) for c in rotations(coins))


def powerset(iterable):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def all_coins():
    "The belief set consisting of all possible coin sequences."
    return set(map(''.join, product('HT', repeat=4)))


if __name__ == "__main__":
    # possible_moves = [set(m) for m in powerset(range(4))]
    # current_belief = frozenset(("HHHT", "HHHH", "HTHT"))
    # for move in possible_moves:
    #     new_belief = {state for coins in current_belief for state in make_move(coins, move)}
    #     print(new_belief)
    print(shortest_path_search())
    # print([set(m) for m in powerset(range(4))])
    # print(rotations('HHHT'))
    # print(make_move("HHHT", {0}))
    # print(flip_coins('HHHT', {0}))
