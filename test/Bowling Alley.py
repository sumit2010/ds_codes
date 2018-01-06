import random

import operator
from enum import Enum


class Player:
    def __init__(self, name):
        self.name = name

    def assignBallSet(self, set):
        self.ballSet = set

    def play(self, pins_left):
        return Pin.hit_pin(pins_left)


class BowlingGame:
    SET = 10
    MAXPINS = 10

    def __init__(self, players_list):
        self.players = [Player(player) for player in players_list]
        self.scorecalculator = ScoreCalculator.getInstance()
        self.scoreBoard = ScoreBoard(self.players)

    def startGame(self):
        for set in range(BowlingGame.SET):
            for player in self.players:
                hit = player.play(BowlingGame.MAXPINS)
                score = hit
                if hit == BowlingGame.MAXPINS:
                    score += self.scorecalculator.add_bonus(Bonus.STRIKE_BONUS)
                else:
                    score += player.play(BowlingGame.MAXPINS - hit)
                    if score == BowlingGame.MAXPINS:
                        score += self.scorecalculator.add_bonus(Bonus.SPARE_BONUS)
                self.scoreBoard.update(player, score)
                # self.scoreBoard.showBoard()
        print self.scoreBoard.winner()

    def allocateSet(self):
        Player.assignBallSet(BallSet(2))


class ScoreBoard:
    def __init__(self, players_list):
        self.players_score = dict((player, list()) for player in players_list)

    def update(self, player, score):
        self.players_score[player].append(score)

    def showBoard(self):
        print "NAME    |   SCORE"
        for (p, score_set) in self.players_score.iteritems():
            print p.name + "  =>>   " + ",".join(str(i) for i in score_set)

    def winner(self):
        print self.showBoard()
        winner = max(self.players_score, key=lambda p: sum(self.players_score.get(p)))
        return winner.name


class Bonus(Enum):
    SPARE_BONUS = 5
    STRIKE_BONUS = 10


class ScoreCalculator:
    instance = None

    @staticmethod
    def getInstance():
        if ScoreCalculator.instance == None:
            ScoreCalculator.instance = ScoreCalculator()
        return ScoreCalculator.instance

    @staticmethod
    def add_bonus(bonus):
        score = 0
        if bonus == Bonus.SPARE_BONUS:
            score += Bonus.SPARE_BONUS
        elif bonus == Bonus.STRIKE_BONUS:
            score += Bonus.STRIKE_BONUS
        return score


class Pin:
    @staticmethod
    def hit_pin(pins_left):
        # Returning random
        return random.randint(1, pins_left)


class BallSet:
    def __init__(self, balls):
        self.balls = balls


if __name__ == '__main__':
    players = ["Sumit", "Mayank", "Swapnil"]
    game = BowlingGame(players)
    game.startGame()
