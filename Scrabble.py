import random
from itertools import permutations


class TileSet(object):
    """Represents the tile set of a scrabble game"""
    def __init__(self):
        self.tiles = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "b",
                      "b", "c", "c", "d", "d", "d", "d", "e",
                      "e", "e", "e", "e", "e", "e", "e", "e", "e", "e",
                      "e", "f", "f", "g", "g", "g", "h", "h", "i", "i",
                      "i", "i", "i", "i", "i", "i", "i", "j", "k", "l",
                      "l", "l", "l", "m", "m", "n", "n", "n", "n", "n",
                      "n", "o", "o", "o", "o", "o", "o", "o", "o", "p",
                      "p", "q", "r", "r", "r", "r", "r", "r", "s", "s",
                      "s", "s", "t", "t", "t", "t", "t", "t", "u", "u",
                      "u", "u", "v", "v", "w", "w", "x", "y", "y", "z"]
        self.tile_values = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
                            "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
                            "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
                            "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
                            "y": 4, "z": 10}

    def __str__(self):
        lst = []
        for k, v in self.tile_values.items():
            lst += [k + ' = ' + str(v)]
        return '\n'.join(lst)

    def num_of_tiles(self):
        return len(self.tiles)

    def shuffle_tiles(self):
        random.shuffle(self.tiles)

    def take_tile(self, num=7):
        """Randomly choose tiles and remove tiles from set"""
        choice = []
        if len(self.tiles) >= num:
            for i in range(num):
                ch = random.choice(self.tiles)
                choice.append(ch)
                self.tiles.remove(ch)
        elif 0 < len(self.tiles) < num:
            for i in range(len(self.tiles)):
                ch = random.choice(self.tiles)
                choice.append(ch)
                self.tiles.remove(ch)
        elif len(self.tiles) == 0:
            choice.append('None')
        return choice

    def first_hand_out(self, n_hands=4, num=7):
        """add to x hands and remove tiles from set"""
        hands = []
        for n in range(1, n_hands + 1):
            hand = Hand()
            hand.label = 'Player ' + str(n)
            hand.tiles = self.take_tile(num)
            hands += [hand]
        return hands

    def hand_out(self, hand, num):
        """Add x tiles to one hand and remove tiles from set"""
        hand.tiles += self.take_tile(num)

    def get_tile_values(self):
        return self.tile_values


class Hand(TileSet):
    """Represents a hand of playing scrabble."""

    def __init__(self, label=''):
        super().__init__()
        self.tiles = []
        self.label = label
        self.score = 0
        self.words = []

    def __str__(self):
        return self.label + ': ' + ', '.join(self.words) + '; Score: ' + str(self.score)

    def get_tiles(self):
        return self.tiles

    def __provide_words(self):
        with open("words.txt") as fin:
            for line in fin:
                yield line.strip()

    def __find_permutations(self, tiles):
        p_lst = []
        for i in range(2, len(tiles) + 1):
            perm = [''.join(p) for p in permutations(tiles, i)]
            for e in perm:
                p_lst += [e]
        return p_lst

    def find_words(self, score_dct):
        perm = list(set(self.__find_permutations(self.tiles)))
        w_dct = {}
        for w in self.__provide_words():
            w_dct[w] = 0

        lst = []
        for p in perm:
            for k in w_dct.keys():
                if k == p:
                    lst += [k]

        dct = {}
        for w in lst:
            score = 0
            for c in w:
                score += score_dct[c]
            dct[w] = score

        score_lst = sorted([(v, k) for k, v in dct.items()], reverse=True)
        if len(score_lst) != 0:
            self.score += score_lst[0][0]
            self.words += [score_lst[0][1]]
            for c in score_lst[0][1]:
                self.tiles.remove(c)
