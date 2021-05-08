from random_strategy import RandomStrategy
from q_strategy import QStrategy
from player import Player
import constants
from board import Board
from game import Game
import matplotlib.pyplot as plt
import time

if __name__=="__main__":

    print ("Game 1 - Random vs Random")
    player1Strategy = RandomStrategy()
    player2Strategy = RandomStrategy()
    player1 = Player(constants.PLAYER_X_VAL, player1Strategy)
    player2 = Player(constants.PLAYER_O_VAL, player2Strategy)
    board1 = Board()
    game1 = Game(player1, player2, board1)
    start = time.perf_counter()
    df = game1.playManyGames(10000)
    stop = time.perf_counter()
    print(f"Time taken to execute {stop - start:0.4f} seconds")
    df.plot(x="Games", y=["X", "O", "Draws"], title="X-Player - Random; O-Player - Random")

    print("Game 2 - Q vs Random")
    player3Strategy = QStrategy()
    player3 = Player(constants.PLAYER_X_VAL, player3Strategy)
    board2 = Board()
    game2 = Game(player3, player2, board2)
    start = time.perf_counter()
    df = game2.playManyGames(10000)
    stop = time.perf_counter()
    print(f"Time taken to execute {stop - start:0.4f} seconds")
    df.plot(x="Games", y=["X", "O", "Draws"], title="X-Player - Q; O-Player - Random")

    print("Game 3 - Random vs Q")
    player4Strategy = QStrategy()
    player4 = Player(constants.PLAYER_O_VAL, player4Strategy)
    board3 = Board()
    game3 = Game(player1, player4, board3)
    
    start = time.perf_counter()
    df = game3.playManyGames(10000)
    stop = time.perf_counter()
    print(f"Time taken to execute {stop - start:0.4f} seconds")

    df.plot(x="Games", y=["X", "O", "Draws"], title="X-Player - Random; O-Player - Q")
    
    print("Game 4 - Q vs Q")
    player5Strategy = QStrategy()
    player5 = Player(constants.PLAYER_X_VAL, player5Strategy)
    board4 = Board()
    game4 = Game(player5, player4, board4)
    
    start = time.perf_counter()
    df = game4.playManyGames(10000)
    stop = time.perf_counter()
    print(f"Time taken to execute {stop - start:0.4f} seconds")
    
    df.plot(x="Games", y=["X", "O", "Draws"], title="X-Player - Q: O-Player - Q")

    game1.printFinalStatistics()
    game2.printFinalStatistics()
    game3.printFinalStatistics()
    game4.printFinalStatistics()
    plt.show()







